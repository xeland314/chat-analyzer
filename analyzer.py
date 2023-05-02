"""
analyzer

This module contains two classes for analyzing text data
from WhatsApp chats: LexicalAnalyzer and WhatsappAnalyzer.

LexicalAnalyzer extracts relevant information from WhatsApp messages,
such as date, time, author, message text, and emojis. 
It processes a text file containing a WhatsApp chat and 
stores the messages in a Chat object, 
which can be retrieved with the get_chat() method.

WhatsappAnalyzer uses LexicalAnalyzer to analyze a WhatsApp chat.
The results are then displayed using a WhatsappResult object.

Dependencies: standard python modules (datetime, os, re),
downloaded packages (nltk), own module (models, results).

Author: Christopher Villamarín (xeland314)
"""

from datetime import datetime
from os.path import exists
import re
from typing import Optional

from models import Chat, Message
from results import ConsoleBuilder

class WhatsappLexicalAnalyzer:

    """
    LexicalAnalyzer recognizes message patterns in one chat.

    Parameters:
        - filename: str

    Returns:
        - chat: Chat
    """

    author_pattern = \
        re.compile(r'(\d{1,2}/\d{1,2}/\d{2})(,)? (\d{1,2}:\d{2}) - (?P<author>.+?)(\s)?:')
    date_pattern = \
        re.compile(r'(?P<date>\d{1,2}/\d{1,2}/\d{2})(,)? (?P<time>\d{1,2}:\d{2})')
    message_pattern = \
        re.compile(r'(\d{1,2}/\d{1,2}/\d{2})(,)? (\d{1,2}:\d{2}) - (.+?)(\s)?:(\s)?(?P<message>.+?)(\n|$)')

    def __init__(self) -> None:
        self.__chat = Chat()

    def extract_author(self, text) -> str:
        """
        Extracts the author name from a given text. 
        It uses a regular expression pattern to search for a match in the text.
        """
        match = self.author_pattern.search(text)
        if match:
            return match.group("author")
        return ""

    def extract_datetime(self, text: str) -> Optional[datetime]:
        """
        Extracts a datetime object from the given
        text string using a regular expression pattern.
        """
        match = self.date_pattern.search(text)
        if match:
            date_str = match.group("date")
            time_str = match.group("time")
            datetime_str = f'{date_str} {time_str}'
            return datetime.strptime(datetime_str, "%d/%m/%y %H:%M")
        return None

    def extract_message(self, text) -> str:
        """
        Extracts the message content from a given text. 
        It uses a regular expression pattern to search for a match in the text.
        """
        match = self.message_pattern.search(text)
        if match:
            return match.group("message")
        return ""

    def process_file(self, filename) -> None:
        """
        Reads a text file and extracts the relevant data to create a Chat object.

        Args:
            filename (str): The name of the file to process.

        Raises:
            FileNotFoundError: If the file does not exist.

        Notes:
            - The file must be in UTF-8 encoding.
            - The function iterates through each line of the file.
            - For each line, it extracts the date/time, author, and message.
            - If the date/time and author are not present, it is 
            considered a continuation of the previous message.
            - The extracted data is used to create Message objects 
            that are appended to the Chat object.
        """
        with open(filename, "r", encoding="utf8") as file:
            current_author = ""
            current_date_time = None
            current_text = ""
            for line in file:
                date_time = self.extract_datetime(line)
                author = self.extract_author(line)
                if date_time is None and author == "":
                    current_text += line
                    continue
                if author == "":
                    continue
                if current_text:
                    self.__chat.register_message(
                        current_author, Message(current_date_time, current_text)
                    )
                current_author = author
                current_date_time = date_time
                current_text = self.extract_message(line)
            if current_text:
                self.__chat.register_message(
                    current_author, Message(current_date_time, current_text)
                )

    def get_chat(self) -> Chat:
        """
        This function returns the current state of the chat,
        which is an instance of the Chat class. It also resets 
        the current state of the chat to an empty Chat object.
        This function can be used to obtain the chat after 
        processing it with the LexicalAnalyzer.

        Returns:
            - A Chat object that contains the messages that were processed by the LexicalAnalyzer.

        Example:
            ```python
            analyzer = LexicalAnalyzer()
            analyzer.process_file("chat.txt")
            chat = analyzer.get_chat()
            print(chat)
            ```
        """
        chat = self.__chat
        self.__chat = Chat()
        return chat

class WhatsappStatisticalAnalyzer:

    """
    The WhatsappAnalyzer class processes a 
    WhatsApp chat log file and generates a summary report.
    """

    def __init__(self, file: str, words: int, emojis: int) -> None:
        if not exists(file):
            raise FileNotFoundError(f"El archivo {file} no existe.")

        self.__parameters = {}
        self.__parameters["words"] = words if words > 0 else 20
        self.__parameters["emojis"] = emojis if emojis > 0 else 10

        self.__lanalyzer = WhatsappLexicalAnalyzer()
        self.__lanalyzer.process_file(file)

        self.__console_builder = ConsoleBuilder()

    def print_summary(self) -> None:
        """
        Generates a summary report of the chat log file
        and prints it to the console.
        """
        self.__console_builder.set_chat(self.__lanalyzer.get_chat())
        self.__console_builder.set_parameters(self.__parameters)
        self.__console_builder.build_all()
        self.__console_builder.print_results()
