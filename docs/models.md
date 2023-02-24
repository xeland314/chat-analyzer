# Table of Contents

* [models](#models)
  * [Message](#models.Message)
    * [date\_time](#models.Message.date_time)
    * [emojis](#models.Message.emojis)
    * [is\_multimedia](#models.Message.is_multimedia)
    * [text](#models.Message.text)
    * [words](#models.Message.words)
    * [add\_more\_text](#models.Message.add_more_text)
    * [get\_word\_count](#models.Message.get_word_count)
    * [get\_character\_count](#models.Message.get_character_count)
    * [get\_sentiment](#models.Message.get_sentiment)
    * [\_\_len\_\_](#models.Message.__len__)
  * [Author](#models.Author)
    * [days](#models.Author.days)
    * [active\_days](#models.Author.active_days)
    * [messages](#models.Author.messages)
    * [name](#models.Author.name)
    * [get\_last\_message](#models.Author.get_last_message)
    * [get\_messages\_from\_day](#models.Author.get_messages_from_day)
    * [get\_message\_list](#models.Author.get_message_list)
    * [get\_word\_frequency](#models.Author.get_word_frequency)
    * [get\_emoji\_frequency](#models.Author.get_emoji_frequency)
    * [generate\_word\_cloud](#models.Author.generate_word_cloud)
    * [get\_average\_words\_per\_message](#models.Author.get_average_words_per_message)
    * [get\_most\_common\_words](#models.Author.get_most_common_words)
    * [get\_most\_common\_emojis](#models.Author.get_most_common_emojis)
    * [save\_message](#models.Author.save_message)
    * [update\_last](#models.Author.update_last)
  * [Chat](#models.Chat)
    * [authors](#models.Chat.authors)
    * [register\_message](#models.Chat.register_message)
    * [get\_last\_author\_name](#models.Chat.get_last_author_name)
    * [get\_last\_message](#models.Chat.get_last_message)
    * [update\_last\_message](#models.Chat.update_last_message)

<a id="models"></a>

# models

models

Author: Christopher Villamarín (xeland314)

Dependencies:
- collections
- datetime
- itertools
- os
- re
- typing
- emoji
- nltk
- wordcloud
- stopwords (own module)

<a id="models.Message"></a>

## Message Objects

```python
class Message(object)
```

Message format:
<date> - <author>: <content>

**Arguments**:

  - date: datetime
  - message: str
  

**Returns**:

  - emojis: Counter
  - words: Counter

<a id="models.Message.date_time"></a>

#### date\_time

```python
@property
def date_time() -> datetime
```

Returns the date when the message was writed.

<a id="models.Message.emojis"></a>

#### emojis

```python
@property
def emojis() -> Counter
```

Returns a list with the unique emojis present in the message.

<a id="models.Message.is_multimedia"></a>

#### is\_multimedia

```python
@property
def is_multimedia() -> bool
```

Determines if the message is multimedia and not text.

<a id="models.Message.text"></a>

#### text

```python
@property
def text() -> str
```

Returns the message content.

<a id="models.Message.words"></a>

#### words

```python
@property
def words() -> Counter
```

Returns a Counter object containing the words of the message,
filtered to remove unnecessary words like STOPWORDS, specific
regex patterns, and emojis.

<a id="models.Message.add_more_text"></a>

#### add\_more\_text

```python
def add_more_text(text: str) -> None
```

This function is responsible for
adding more text to an existing message.

<a id="models.Message.get_word_count"></a>

#### get\_word\_count

```python
def get_word_count() -> int
```

Returns the number of words in the message.

<a id="models.Message.get_character_count"></a>

#### get\_character\_count

```python
def get_character_count() -> int
```

Returns the number of characters in the message.

<a id="models.Message.get_sentiment"></a>

#### get\_sentiment

```python
def get_sentiment() -> float
```

Returns a float between -1 and 1 indicating
the overall sentiment of the message.

<a id="models.Message.__len__"></a>

#### \_\_len\_\_

```python
def __len__() -> int
```

Returns the number of characters in the message.

<a id="models.Author"></a>

## Author Objects

```python
class Author(object)
```

A class that represents an author of messages in a chat.

**Attributes**:

  - name : str
  - messages : dict

<a id="models.Author.days"></a>

#### days

```python
@property
def days() -> list[date]
```

Returns a day list which at least one message was sent.

<a id="models.Author.active_days"></a>

#### active\_days

```python
@property
def active_days() -> int
```

Returns the number of days in which the author sent at least one message.

<a id="models.Author.messages"></a>

#### messages

```python
@property
def messages() -> int
```

Returns the total number of messages sent by this author.

<a id="models.Author.name"></a>

#### name

```python
@property
def name() -> str
```

Returns the name of the author.

<a id="models.Author.get_last_message"></a>

#### get\_last\_message

```python
def get_last_message() -> Optional[Message]
```

Returns the last message of the message list if it exists, 
otherwise return None.

<a id="models.Author.get_messages_from_day"></a>

#### get\_messages\_from\_day

```python
def get_messages_from_day(day: date) -> list[Message]
```

Returns a list of Message objects sent on the specified day.

<a id="models.Author.get_message_list"></a>

#### get\_message\_list

```python
def get_message_list() -> list[Message]
```

Returns a list of all Message objects sent by this author.

<a id="models.Author.get_word_frequency"></a>

#### get\_word\_frequency

```python
def get_word_frequency() -> FreqDist
```

Returns a dictionary of all the words that
the author has used and their frequency.

<a id="models.Author.get_emoji_frequency"></a>

#### get\_emoji\_frequency

```python
def get_emoji_frequency() -> FreqDist
```

Returns a dictionary of all the words that
 the author has used and their frequency.

<a id="models.Author.generate_word_cloud"></a>

#### generate\_word\_cloud

```python
def generate_word_cloud() -> None
```

Generates a wordcloud image from the words that
the author wrote in the chat.

<a id="models.Author.get_average_words_per_message"></a>

#### get\_average\_words\_per\_message

```python
def get_average_words_per_message() -> float
```

Calculates the average of words per message.

<a id="models.Author.get_most_common_words"></a>

#### get\_most\_common\_words

```python
def get_most_common_words(n: int) -> FreqDist
```

Returns the n most common words used by the current author.

<a id="models.Author.get_most_common_emojis"></a>

#### get\_most\_common\_emojis

```python
def get_most_common_emojis(n: int) -> FreqDist
```

Returns the n most common emojis used by the current author.

<a id="models.Author.save_message"></a>

#### save\_message

```python
def save_message(new_message: Message) -> None
```

Registers a new message sent by this author.

<a id="models.Author.update_last"></a>

#### update\_last

```python
def update_last(message: Message) -> None
```

Updates the last message with more text founded in the file.

<a id="models.Chat"></a>

## Chat Objects

```python
class Chat(object)
```

A class that represents a chat conversation.

**Attributes**:

- `__authors` _dict_ - A dictionary of Author objects indexed by their name.
- `__last_author` _str_ - The name of the last author to register a message.

<a id="models.Chat.authors"></a>

#### authors

```python
@property
def authors() -> list[Author]
```

Returns a list with all the authors in the chat.

<a id="models.Chat.register_message"></a>

#### register\_message

```python
def register_message(author_name: str, new_message: Message) -> None
```

Registers a new message for a given author. If the author does not
exist, creates a new Author object and adds it to the chat's list of
authors.

<a id="models.Chat.get_last_author_name"></a>

#### get\_last\_author\_name

```python
def get_last_author_name() -> Optional[str]
```

Returns the last author name that saved a message.

<a id="models.Chat.get_last_message"></a>

#### get\_last\_message

```python
def get_last_message() -> Optional[Message]
```

Returns the last message of the message list.

<a id="models.Chat.update_last_message"></a>

#### update\_last\_message

```python
def update_last_message(author_name: str, message: Message) -> None
```

Updates the last message with more text founded in the file.

