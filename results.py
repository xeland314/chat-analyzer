"""
results

Author: Christopher Villamarín (xeland314)

Dependencies: standard python modules (collections),
downloaded packages (emoji, nltk, rich).
"""

from collections import Counter

from emoji import demojize
from nltk.probability import FreqDist
from rich import print as rprint
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

class WhatsappResult(object):
    """
    Class for storing and printing results of WhatsApp analysis.

    Args:
        - authors (collections.Counter): A Counter object
        containing the message count for each author.
        - emojis_by_person (collections.Counter): A Counter
        object containing the most frequent emojis used by each author.
        - words_by_person (collections.Counter): A Counter
        object containing the most frequent words used by each author.
        - parameters (dict): A dictionary containing the parameters used for analysis.
    """

    def __init__(self,
        authors: Counter,
        emojis_by_person: Counter,
        words_by_person: Counter,
        parameters: dict
    ) -> None:
        self.__set_title(authors)
        self.__set_emojis_panel(emojis_by_person, parameters["emojis"])
        self.__set_words_panel(words_by_person, parameters["words"])

    def __set_title(self, authors: Counter) -> None:
        title_content = ""
        for author in list(authors.keys()):
            title_content += f"[bold blue]{author}[/bold blue] ha enviado "
            title_content += f"[bold green]{authors[author]}[/bold green] mensajes.\n"
        self.__title_panel = \
            Panel(title_content, title="Whatsapp Analyzer Results")

    def __set_emojis_panel(self, emojis_by_person: Counter, n_most_common: int) -> None:
        self.__emoji_tables = []
        people = list(emojis_by_person.keys())
        for person in people:
            table = \
                Table(title=f"[bold blue]Emojis más usados por {person}[/bold blue]")
            table.add_column("Emoji", justify="center")
            table.add_column("Descripción", justify="center", style="cyan")
            table.add_column("Frecuencia", justify="center", style="green")
            emojis: FreqDist = emojis_by_person[person]
            for emoji, count in emojis.most_common(n_most_common):
                demoji = demojize(emoji, delimiters=("_", "_"), language="es")
                table.add_row(emoji, demoji.replace("_", " "), str(count))
            self.__emoji_tables.append(table)

    def __calculate_lexical_richness(self, words: FreqDist) -> float:
        """
        Calculate the lexical richness of a text based on the frequency distribution of its words.
        """
        return words.B() / words.N()

    def __set_words_panel(self, words_by_person: Counter, n_most_common: int) -> None:
        self.__word_tables = []
        self.__word_panels = []
        people = list(words_by_person.keys())
        for person in people:
            # Create a new table per person
            table = \
                Table(title=f"[bold blue]Palabras más usadas por {person}[/bold blue]")
            table.add_column("Palabra", justify="right")
            table.add_column("Frecuencia", justify="center", style="green")
            words: FreqDist = words_by_person[person]
            for word, count in words.most_common(n_most_common):
                table.add_row(word, str(count))
            self.__word_tables.append(table)
            # Create the summary word panel:
            lexical_richness = self.__calculate_lexical_richness(words)
            word_panel_content = \
                f"Cantidad de palabras únicas: [bold green]{words.B()}[/bold green]\n"
            word_panel_content += f"Total de palabras: [bold green]{words.N()}[/bold green]\n"
            word_panel_content += f"Riqueza léxica: [bold green]{lexical_richness}[/bold green]"
            self.__word_panels.append(
                Panel(word_panel_content, title=f"Palabras empleadas por {person}")
            )

    def print_results(self) -> None:
        """
        Prints the analysis results to the console.
        """
        rprint(self.__title_panel)
        console = Console()
        for table in self.__emoji_tables:
            console.print(table, justify="center")
        for panel, table in zip(self.__word_panels, self.__word_tables):
            rprint(panel)
            console.print(table, justify="center")
