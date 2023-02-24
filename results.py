"""
results

Author: Christopher Villamarín (xeland314)

Dependencies: standard python modules (abc),
downloaded packages (emoji, nltk, rich).
"""

from abc import ABCMeta, abstractmethod

from emoji import demojize
from nltk.probability import FreqDist
from rich import print as rprint
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from models import Chat

class ResultBuilder(metaclass=ABCMeta):
    """
    The ResultBuilder abstract class specifies methods
    for creating the different parts of the Result objects.
    """

    def __init__(self) -> None:
        self._chat = None
        self._authors = None
        self._parameters = {}

    @abstractmethod
    def build_titles(self) -> None:
        """
        This method should be implemented
        to build the titles to show 
        as a result of the analysis.
        """
        raise NotImplementedError("Should implement build_titles()")

    @abstractmethod
    def build_emojis_panel(self) -> None:
        """
        This method should be implemented
        to build the emojis panel to show 
        as a result of the analysis.
        """
        raise NotImplementedError("Should implement build_emojis_panel()")
    
    @abstractmethod
    def build_words_panel(self) -> None:
        """
        This method should be implemented
        to build the words panel to show 
        as a result of the analysis.
        """
        raise NotImplementedError("Should implement build_words_panel()")
    
    @abstractmethod
    def build_images(self) -> None:
        """
        This method should be implemented
        to build the images as a result of the analysis.
        """
        raise NotImplementedError("Should implement build_images()")

    @abstractmethod
    def build_all(self) -> None:
        """
        This method should be implemented
        to build all the results of the analysis.
        """
        raise NotImplementedError("Should implement build_all()")     

    def reset(self) -> None:
        "This method resets the _chat attribute to None."
        self._chat = None

    def set_chat(self, chat: Chat) -> None:
        "This method sets the chat to be analyzed."
        self._chat = chat
        self._authors = chat.authors

    def set_parameters(self, parameters: dict) -> None:
        """
        This method sets the _parameters attribute to a dictionary
        that contains the parameters of the chat analysis.
        """
        self._parameters = parameters

class ConsoleBuilder(ResultBuilder):
    """
    This class provides a way to print/display
    the analysis results to the console.
    """

    def __init__(self) -> None:
        super().__init__()
        self.__title_panel = None
        self.__emoji_tables = list[Table]()
        self.__word_tables = list[Table]()
        self.__word_panels = list[Panel]()

    def build_titles(self) -> None:
        title_content = ""
        for author in list(self._authors):
            title_content += f"[bold blue]{author.name}[/bold blue] ha enviado "
            title_content += f"[bold green]{author.messages}[/bold green] mensajes.\n"
        self.__title_panel = \
            Panel(title_content, title="Whatsapp Analyzer Results")

    def build_emojis_panel(self) -> None:
        for author in self._authors:
            table = \
                Table(title=f"[bold blue]Emojis más usados por {author.name}[/bold blue]")
            table.add_column("Emoji", justify="center")
            table.add_column("Descripción", justify="center", style="cyan")
            table.add_column("Frecuencia", justify="center", style="green")

            emojis: FreqDist = author.get_emoji_frequency()
            for emoji, count in emojis.most_common(self._parameters["emojis"]):
                demoji = demojize(emoji, delimiters=("_", "_"), language="es")
                table.add_row(emoji, demoji.replace("_", " "), str(count))
            self.__emoji_tables.append(table)

    def build_words_panel(self) -> None:
        for author in self._authors:
            # Create a new table per person
            table = \
                Table(title=f"[bold blue]Palabras más usadas por {author.name}[/bold blue]")
            table.add_column("Palabra", justify="right")
            table.add_column("Frecuencia", justify="center", style="green")

            words: FreqDist = author.get_word_frequency()
            for word, count in words.most_common(self._parameters["words"]):
                table.add_row(word, str(count))
            self.__word_tables.append(table)
            
            # Create the summary word panel:
            word_panel_content = \
                f"Cantidad de palabras únicas: [bold green]{words.B()}[/bold green]\n"
            word_panel_content += f"Total de palabras: [bold green]{words.N()}[/bold green]\n"
            # word_panel_content += f"Riqueza léxica: [bold green]{lexical_richness}[/bold green]"
            self.__word_panels.append(
                Panel(word_panel_content, title=f"Palabras empleadas por {author.name}")
            )

    def build_images(self) -> None:
        for author in self._authors:
            author.generate_word_cloud()

    def build_all(self) -> None:
        self.build_titles()
        self.build_emojis_panel()
        self.build_words_panel()
        self.build_images()

    def print_results(self) -> None:
        "Prints the analysis results in the console."
        rprint(self.__title_panel)
        console = Console()
        for table in self.__emoji_tables:
            console.print(table, justify="center")
        for panel, table in zip(self.__word_panels, self.__word_tables):
            rprint(panel)
            console.print(table, justify="center")
