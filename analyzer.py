"""
analyzer

This module contains two classes for analyzing text data
from WhatsApp chats: LexicalAnalyzer and WhatsappAnalyzer.

LexicalAnalyzer extracts relevant information from WhatsApp messages,
such as date, time, author, message text, and emojis. 
It processes a text file containing a WhatsApp chat and 
stores the messages in a Chat object, 
which can be retrieved with the get_chat() method.

WhatsappAnalyzer uses LexicalAnalyzer to analyze a WhatsApp chat
and compute various metrics such as the number of messages
and the most frequent words and emojis used by each author.
The results are then displayed using a WhatsappResult object.

Dependencies: standard python modules (collections, datetime, os, re),
downloaded packages (nltk), own module (models, results).

Author: Christopher Villamarín (xeland314)
"""

from collections import Counter
from datetime import datetime
from os.path import exists
import re

from nltk.probability import FreqDist

from models import Chat, Message
from results import WhatsappResult

class LexicalAnalyzer(object):

    """
    LexicalAnalyzer recognizes message patterns in one chat.

    Parameters:
        - filename: str

    Returns:
        - chat: Chat
    """

    author_pattern = \
        re.compile(r'(\d{1,2}/\d{1,2}/\d{2}) (\d{1,2}:\d{2}) - (?P<author>.+?):')
    date_pattern = \
        re.compile(r'(?P<date>\d{1,2}/\d{1,2}/\d{2}) (?P<time>\d{1,2}:\d{2})')
    message_pattern = \
        re.compile(r'(\d{1,2}/\d{1,2}/\d{2}) (\d{1,2}:\d{2}) - (.+?):(?P<message>.+?)(\n|$)')

    def __init__(self) -> None:
        self.__chat = Chat()

    def extract_author(self, text) -> str:
        """
        Extracts the author name from a given text. 
        It uses a regular expression pattern to search for a match in the text.
        """
        match = self.author_pattern.search(text)
        if match:
            return match.group('author')
        return ''

    def extract_datetime(self, text: str) -> datetime:
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
            for line in file:
                date_time = self.extract_datetime(line)
                author = self.extract_author(line)
                if date_time is None and author == "":
                    message = self.__chat.get_last_message()
                    message.add_more_text(line)
                    self.__chat.update_last(message)
                    continue
                if author == "":
                    # This could be a Whatsapp message.
                    continue
                text_message = self.extract_message(line)
                self.__chat.append(Message(date_time, author, text_message))

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

class WhatsappAnalyzer(object):

    """
    The WhatsappAnalyzer class processes a WhatsApp chat log file,
    extracts relevant data (such as the number of messages,
    emojis and words used by each author) and generates a summary report.

    Args:
        - __chat (list): A list of Message objects extracted from the chat log file.
        - __authors (Counter): A Counter object with the number of messages
        written by each author.
        - __emojis_by_person (Counter): A Counter object with the number of
        emojis used by each author.
        - __words_by_person (Counter): A Counter object with the number of
        words used by each author.
        - __summary (WhatsappResult): A WhatsappResult object that represents 
        the summary report generated by the print_summary method.
        - __summary_parameters (dict): A dictionary with the configuration
        parameters for the summary report, such as the number of words and emojis to show.
    """

    def __init__(self, file: str, words: int, emojis: int) -> None:
        if not exists(file):
            raise FileNotFoundError(f"El archivo {file} no existe.")
        lanalyzer = LexicalAnalyzer()
        lanalyzer.process_file(file)
        self.__chat = lanalyzer.get_chat()
        self.__authors = Counter()
        self.__emojis_by_person = Counter()
        self.__words_by_person = Counter()
        self.__summary: WhatsappResult = None
        self.__summary_parameters = {}
        self.__summary_parameters["words"] = words if words > 0 else 20
        self.__summary_parameters["emojis"] = emojis if emojis > 0 else 10

    def __count_messages(self) -> None:
        """
        Counts the number of messages written by each author in the chat log file.
        """
        for message in self.__chat:
            self.__authors[message.author] += 1

    def __extract_relevant_data(self) -> None:
        """
        Extracts relevant data (such as the number of emojis
        and words used by each author) from the chat log file.
        """
        for author in list(self.__authors.keys()):
            # Create a emojis Counter per each author
            self.__emojis_by_person[author] = FreqDist()
            # Create a words FreqDist per each author
            self.__words_by_person[author] = FreqDist()
        for message in self.__chat:
            # Append and count emojis used per each author
            self.__emojis_by_person[message.author] += message.emojis
            # Append and count words used per each author
            self.__words_by_person[message.author] += message.words

    def print_summary(self) -> None:
        """
        Generates a summary report of the chat log file and prints
        it to the console. The report includes the number of messages,
        emojis and words used by each author,
        as well as a lexical richness score.
        """
        self.__count_messages()
        self.__extract_relevant_data()
        self.__summary = WhatsappResult(
            self.__authors,
            self.__emojis_by_person,
            self.__words_by_person,
            self.__summary_parameters
        )
        self.__summary.print_results()
