from collections import Counter
from datetime import datetime
from emoji import demojize
from models import Chat, Message
from nltk.probability import FreqDist
from re import compile
from rich import print as rprint
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

class LexicalAnalyzer(object):

    """
    LexicalAnalyzer recognizes message patterns in one chat.
    
    Parameters:
        - filename: str
    
    Returns:
        - chat: Chat
    """
    
    author_pattern = compile(r'(\d{1,2}/\d{1,2}/\d{2} \d{1,2}:\d{2}) - (?P<author>.+?):')
    date_pattern = compile(r'(?P<date>\d{1,2}/\d{1,2}/\d{2}) (?P<time>\d{1,2}:\d{2})')
    message_pattern = compile(r'(?P<date>\d{1,2}/\d{1,2}/\d{2}) (?P<time>\d{1,2}:\d{2}) - (?P<author>.+?):(?P<message>.+?)(\n|$)')

    def __init__(self) -> None:
        self.__chat = Chat()

    def extract_author(self, text) -> str:
        match = self.author_pattern.search(text)
        if match:
            return match.group('author')
        return ''

    def extract_datetime(self, text) -> datetime:
        match = self.date_pattern.search(text)
        if match:
            date_str = match.group("date")
            time_str = match.group("time")
            datetime_str = f'{date_str} {time_str}'
            return datetime.strptime(datetime_str, "%d/%m/%y %H:%M")
        return None

    def extract_message(self, text) -> str:
        match = self.message_pattern.search(text)
        if match:
            return match.group("message")
        return ""

    def process_file(self, filename) -> None:
        with open(filename, "r") as file:
            for line in file:
                date_time = self.extract_datetime(line)
                author = self.extract_author(line)
                if date_time is None and author == "":
                    message = self.__chat.get_last_message()
                    message.add_more_text(line)
                    self.__chat.update_last(message)
                    continue
                elif author == "":
                    # This could be a Whatsapp message.
                    continue
                text_message = self.extract_message(line)
                self.__chat.append(Message(date_time, author, text_message))

    def get_chat(self) -> Chat:
        chat = self.__chat
        self.__chat = Chat()
        return chat

class WhatsappResult(object):

    def __init__(self,
        authors: Counter,
        emojis_by_person: Counter,
        words_by_person: Counter
    ) -> None:
        self._set_title(authors)
        self._set_emojis_panel(emojis_by_person)
        self._set_words_panel(words_by_person)

    def _set_title(self, authors: Counter) -> None:
        title_content = ""
        for author in list(authors.keys()):
            title_content += f"[bold blue]{author}[/bold blue] ha enviado "
            title_content += f"[bold green]{authors[author]}[/bold green] mensajes.\n"
        self.__title_panel = Panel(title_content, title="Whatsapp Analyzer Results")

    def _set_emojis_panel(self, emojis_by_person: Counter) -> None:
        self.__emoji_tables = []
        people = list(emojis_by_person.keys())
        for person in people:
            table = Table(title=f"[bold blue]Emojis más usados por {person}[/bold blue]")
            table.add_column("Emoji", justify="center")
            table.add_column("Type", justify="center", style="cyan")
            table.add_column("Frecuencia", justify="center", style="green")
            emojis: FreqDist = emojis_by_person[person]
            for emoji, count in emojis.most_common(10):
                demoji = demojize(emoji, delimiters=("_", "_"), language="es")
                table.add_row(emoji, demoji.replace("_", " "), str(count))
            self.__emoji_tables.append(table)

    def __calculate_lexical_richness(self, words: FreqDist) -> float:
        return words.B() / words.N()

    def _set_words_panel(self, words_by_person: Counter) -> None:
        self.__word_tables = []
        self.__word_panels= []
        people = list(words_by_person.keys())
        for person in people:
            # Create a new table per person
            table = Table(title=f"[bold blue]Palabras más usadas por {person}[/bold blue]")
            table.add_column("Palabra", justify="right")
            table.add_column("Frecuencia", justify="center", style="green")
            words: FreqDist = words_by_person[person]
            for word, count in words.most_common(25):
                table.add_row(word, str(count))
            self.__word_tables.append(table)
            # Create the summary word panel:
            lr = self.__calculate_lexical_richness(words)
            word_panel_content = f"Cantidad de palabras únicas: [bold green]{words.B()}[/bold green]\n"
            word_panel_content += f"Total de palabras: [bold green]{words.N()}[/bold green]\n"
            word_panel_content += f"Riqueza léxica: [bold green]{lr}[/bold green]"
            self.__word_panels.append(
                Panel(word_panel_content, title=f"Palabras empleadas por {person}")
            )

    def print_results(self) -> None:
        rprint(self.__title_panel)
        console = Console()
        for table in self.__emoji_tables:
            console.print(table, justify="center")
        for panel, table in zip(self.__word_panels, self.__word_tables):
            rprint(panel)
            console.print(table, justify="center")

class WhatsappAnalyzer(object):

    def __init__(self, *args) -> None:
        if len(args) > 1 or len(args) == 0:
            raise NotImplementedError()
        else:
            if isinstance(args[0], str):
                lanalyzer = LexicalAnalyzer()
                lanalyzer.process_file(args[0])
                self.__chat = lanalyzer.get_chat()
            elif isinstance(args[0], Chat):
                self.__chat = args[0]
            else:
                NotImplementedError()

    def search_authors(self) -> None:
        self.__authors = Counter()
        for message in self.__chat:
            self.__authors[message.author] += 1

    def search_emojis(self) -> None:
        self.__emojis_by_person = Counter()
        for author in list(self.__authors.keys()):
            # Create a emojis Counter per each author
            self.__emojis_by_person[author] = FreqDist()
        for message in self.__chat:
            # Append and count emojis used per each author
            self.__emojis_by_person[message.author] += message.emojis

    def search_words(self) -> None:
        self.__words_by_person = Counter()
        for author in list(self.__authors.keys()):
            # Create a words FreqDist per each author
            self.__words_by_person[author] = FreqDist()
        for message in self.__chat:
            # Append and count words used per each author
            self.__words_by_person[message.author] += message.words

    def print_summary(self) -> None:
        self.search_authors()
        self.search_emojis()
        self.search_words()
        self.__summary = WhatsappResult(
            self.__authors,
            self.__emojis_by_person,
            self.__words_by_person
        )
        self.__summary.print_results()
