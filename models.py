"""
models

Author: Christopher Villamarín (xeland314)

Dependencies:
- collections
- datetime
- itertools
- os
- re
- emoji
- nltk
- wordcloud
- stopwords (own module)
"""

from collections import Counter
from datetime import datetime, date
from itertools import chain
import os
import re

from emoji import distinct_emoji_list
from nltk.probability import FreqDist
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud

from stopwords import STOPWORDS, FIRST_LANGUAGE

es_word_pattern = re.compile(r"^[A-Za-záéíóúÁÉÍÓÚüÜñÑ]+$")
multimedia_pattern = re.compile(r"\<Multimedia omitido\>")
hahaha_pattern = re.compile(r"(?:[ahjk]?(ja|je|ji|jo|js|ha|ka|xa)+[hjksx]?)")

sentiment_analyzer = SentimentIntensityAnalyzer()

class Message:

    """
    Message format:
        <date> - <author>: <content>

    Parameters:
        - date: datetime
        - message: str

    Returns:
        - emojis: Counter
        - words: Counter
    """

    def __init__(self, date_time: datetime, message: str) -> None:
        self.__date_time = date_time
        self.__message = message

    @property
    def date_time(self) -> datetime:
        "Returns the date when the message was writed."
        return self.__date_time

    @property
    def emojis(self) -> Counter:
        "Returns a list with the unique emojis present in the message."
        emojis = distinct_emoji_list(self.__message)
        return Counter(emojis)

    @property
    def is_multimedia(self) -> bool:
        "Determines if the message is multimedia and not text."
        return multimedia_pattern.search(self.__message)

    @property
    def text(self) -> str:
        "Returns the message content."
        return self.__message

    @property
    def words(self) -> Counter:
        """
        Returns a Counter object containing the words of the message,
        filtered to remove unnecessary words like STOPWORDS, specific
        regex patterns, and emojis.
        """
        if self.is_multimedia:
            return Counter()
        words = word_tokenize(self.__message, language=FIRST_LANGUAGE)
        filtered_words = Counter()
        for word in words:
            word = word.lower()
            if word in STOPWORDS or hahaha_pattern.search(word):
                continue
            if es_word_pattern.search(word):
                filtered_words[word] += 1
        return filtered_words

    def get_word_count(self) -> int:
        "Returns the number of words in the message."
        return len(word_tokenize(self.__message))

    def get_character_count(self) -> int:
        "Returns the number of characters in the message."
        return len(self.__message)

    def get_sentiment(self) -> float:
        """
        Returns a float between -1 and 1 indicating
        the overall sentiment of the message.
        """
        sentiment_scores = sentiment_analyzer.polarity_scores(self.__message)
        return sentiment_scores["compound"]

    def __len__(self) -> int:
        "Returns the number of characters in the message."
        return len(self.__message)

    def __str__(self) -> str:
        return self.__message

class Author:
    """
    A class that represents an author of messages in a chat.

    Attributes:
        - name : str
        - messages : dict
    """

    def __init__(self, name: str) -> None:
        self.__name = name
        self.__messages_count = 0
        self.__emojis = FreqDist()
        self.__words = FreqDist()
        self.__messages = dict[date, list[Message]]()

    @property
    def days(self) -> list[date]:
        "Returns a day list which at least one message was sent."
        return list(self.__messages.values())

    @property
    def active_days(self) -> int:
        "Returns the number of days in which the author sent at least one message."
        return len(self.days)

    @property
    def messages(self) -> int:
        "Returns the total number of messages sent by this author."
        return self.__messages_count

    @property
    def name(self) -> str:
        "Returns the name of the author."
        return self.__name

    def get_messages_from_day(self, day: date) -> list[Message]:
        "Returns a list of Message objects sent on the specified day."
        return self.__messages[day]

    def get_message_list(self) -> list[Message]:
        " Returns a list of all Message objects sent by this author."
        short_lists = self.__messages.values()
        return list(chain.from_iterable(short_lists))

    def get_word_frequency(self) -> FreqDist:
        """
        Returns a dictionary of all the words that
        the author has used and their frequency.
        """
        if self.__words.B() == 0:
            for message_list in self.__messages.values():
                for message in message_list:
                    self.__words += message.words
        return self.__words

    def get_emoji_frequency(self) -> FreqDist:
        """
        Returns a dictionary of all the words that
         the author has used and their frequency.
        """
        if self.__emojis.B() == 0:
            for message_list in self.__messages.values():
                for message in message_list:
                    self.__emojis += message.emojis
        return self.__emojis

    def generate_word_cloud(self) -> None:
        """
        Generates a wordcloud image from the words that
        the author wrote in the chat.
        """
        words = dict(self.get_word_frequency())
        word_cloud = WordCloud(
            width=800, height=400,
            background_color='white',
            max_words=2000
        )
        word_cloud.generate_from_frequencies(words)
        if not os.path.isdir("results"):
            os.mkdir("results")
        now = datetime.now()
        date_time = now.strftime("%m-%d-%Y_%H-%M-%S")
        word_cloud.to_file(f"results/{self.name}_{date_time}_word_cloud.jpg")

    def get_average_words_per_message(self) -> float:
        "Calculates the average of words per message."
        total_words = 0
        for message_list in self.__messages.values():
            for message in message_list:
                total_words += message.get_word_count()
        return total_words / self.messages

    def get_most_common_words(self, n: int) -> FreqDist:
        "Returns the n most common words used by the current author."
        return self.get_word_frequency().most_common(n)

    def get_most_common_emojis(self, n: int) -> FreqDist:
        "Returns the n most common emojis used by the current author."
        return self.get_emoji_frequency().most_common(n)

    def save_message(self, new_message: Message) -> None:
        "Registers a new message sent by this author."
        day = new_message.date_time.date()
        if not self.__messages.get(day):
            self.__messages[day] = []
        self.__messages[day].append(new_message)
        self.__messages_count += 1

    def __str__(self) -> str:
        return f"{self.__name}: {self.__messages_count} messages, {self.active_days} active days"

    def __repr__(self) -> str:
        return f"<Author '{self.__name}' with {self.__messages_count} messages sent>"

class Chat:
    """
    A class that represents a chat conversation.

    Attributes:
        __authors (dict): A dictionary of Author objects indexed by their name.
    """
    def __init__(self) -> None:
        self.__authors = dict[str, Author]()

    @property
    def authors(self) -> list[Author]:
        "Returns a list with all the authors in the chat."
        return list(self.__authors.values())

    def register_message(self, author_name: str, new_message: Message) -> None:
        """
        Registers a new message for a given author. If the author does not
        exist, creates a new Author object and adds it to the chat's list of
        authors.
        """
        # Check if author already exists in chat's list of authors.
        author = self.__authors.get(author_name)

        # If not, create a new Author object and add it to the list.
        if author is None:
            author = Author(author_name)
            self.__authors[author_name] = author

        # Add the new message to the author's message list.
        author.save_message(new_message)
