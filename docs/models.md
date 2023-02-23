# Table of Contents

* [models](#models)
  * [Message](#models.Message)
    * [emojis](#models.Message.emojis)
    * [words](#models.Message.words)
    * [add\_more\_text](#models.Message.add_more_text)
  * [EmptyChat](#models.EmptyChat)
  * [Chat](#models.Chat)
    * [append](#models.Chat.append)
    * [get\_last\_message](#models.Chat.get_last_message)
    * [update\_last](#models.Chat.update_last)
    * [\_\_len\_\_](#models.Chat.__len__)

<a id="models"></a>

# models

models

Author: Christopher Villamarín (xeland314)

Dependencies: standard python modules (collections, datetime, re),
downloaded packages (emoji, nltk), own module (stopwords).

<a id="models.Message"></a>

## Message Objects

```python
class Message(object)
```

Message format:
<date> - <author>: <content>

**Arguments**:

  - date: datetime
  - author: str
  - message: str
  

**Returns**:

  - emojis: Counter
  - words: Counter

<a id="models.Message.emojis"></a>

#### emojis

```python
@property
def emojis() -> Counter
```

Returns a list with the unique emojis present in the message.

<a id="models.Message.words"></a>

#### words

```python
@property
def words() -> Counter
```

Returns a Counter object containing the words
of the message, filtered to remove unnecessary words
like STOPWORDS and specific regex patterns.

<a id="models.Message.add_more_text"></a>

#### add\_more\_text

```python
def add_more_text(text: str) -> None
```

This function is responsible for adding more text to an existing message.

<a id="models.EmptyChat"></a>

## EmptyChat Objects

```python
class EmptyChat(Exception)
```

EmptyChat:

Exception thrown when trying to access an empty chat.

<a id="models.Chat"></a>

## Chat Objects

```python
class Chat(object)
```

The Chat class allows to manage and manipulate messages.

<a id="models.Chat.append"></a>

#### append

```python
def append(new_message: Message) -> None
```

Append a new mwssage to the message list.

<a id="models.Chat.get_last_message"></a>

#### get\_last\_message

```python
def get_last_message() -> Message
```

Return the last message of the message list.

<a id="models.Chat.update_last"></a>

#### update\_last

```python
def update_last(message: Message) -> None
```

Update the last message with more text founded in the file.

<a id="models.Chat.__len__"></a>

#### \_\_len\_\_

```python
def __len__() -> int
```

Return the total number of messages in the chat

