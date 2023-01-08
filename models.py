from collections import Counter
from datetime import datetime
from emoji import distinct_emoji_list
from nltk.tokenize import word_tokenize
from re import compile
from stopwords import STOPWORDS, FIRST_LANGUAGE

es_word_pattern = compile(r"^[A-Za-záéíóúÁÉÍÓÚüÜñÑ]+$")
multimedia_pattern = compile(r"\<Multimedia omitido\>")

class Message(object):

    """
    Message format:
        <date> - <author>: <content>

    Parameters:
        - date
        - author
        - message

    Returns:
        - emojis
        - words
    """

    def __init__(self, date_time, author, message) -> None:
        self.__date_time = date_time
        self.__author = author
        self.__message = message

    @property
    def author(self) -> str:
        return self.__author

    @property
    def date_time(self) -> datetime:
        return self.__date_time

    @property
    def emojis(self) -> Counter:
        emojis = distinct_emoji_list(self.__message)
        return Counter(emojis)

    @property
    def is_multimedia(self) -> bool:
        return multimedia_pattern.search(self.__message)

    @property
    def words(self) -> Counter:
        if self.is_multimedia:
            return Counter()
        words = word_tokenize(self.__message, language=FIRST_LANGUAGE)
        filtered_words = [word for word in words if es_word_pattern.match(word)]
        del(words)
        return Counter([word.casefold() for word in filtered_words if word.casefold() not in STOPWORDS])

    def add_more_text(self, text) -> None:
        self.__message += "\n" + text

    def __str__(self) -> str:
        return self.__message

class EmptyChat(Exception):

    def __init__(self) -> None:
        super().__init__("Empty chat")

class Chat(object):

    """
    The Chat class allows to manage and manipulate messages.
    """

    def __init__(self) -> None:
        self.__messages = list[Message]()
        self.index = 0

    def append(self, new_message: Message) -> None:
        "Append a new mwssage to the message list."
        self.__messages.append(new_message)

    def get_last_message(self) -> Message:
        "Return the last message of the message list."
        if len(self.__messages) == 0:
            raise EmptyChat()
        return self.__messages[-1]

    def update_last(self, message: Message) -> None:
        "Update the last message with more text founded in the file."
        self.__messages[-1] = message

    def __iter__(self):
        self.index = 0
        return self
  
    def __len__(self) -> int:
        "Return the total number of messages in the chat"
        return len(self.__messages)

    def __next__(self) -> Message:
        if self.index >= len(self.__messages):
            raise StopIteration
        item = self.__messages[self.index]
        self.index += 1
        return item
