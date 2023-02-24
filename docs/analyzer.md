# Table of Contents

* [analyzer](#analyzer)
  * [LexicalAnalyzer](#analyzer.LexicalAnalyzer)
    * [extract\_author](#analyzer.LexicalAnalyzer.extract_author)
    * [extract\_datetime](#analyzer.LexicalAnalyzer.extract_datetime)
    * [extract\_message](#analyzer.LexicalAnalyzer.extract_message)
    * [process\_file](#analyzer.LexicalAnalyzer.process_file)
    * [get\_chat](#analyzer.LexicalAnalyzer.get_chat)
  * [WhatsappAnalyzer](#analyzer.WhatsappAnalyzer)
    * [print\_summary](#analyzer.WhatsappAnalyzer.print_summary)

<a id="analyzer"></a>

# analyzer

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

<a id="analyzer.LexicalAnalyzer"></a>

## LexicalAnalyzer Objects

```python
class LexicalAnalyzer(object)
```

LexicalAnalyzer recognizes message patterns in one chat.

**Arguments**:

  - filename: str
  

**Returns**:

  - chat: Chat

<a id="analyzer.LexicalAnalyzer.extract_author"></a>

#### extract\_author

```python
def extract_author(text) -> str
```

Extracts the author name from a given text. 
It uses a regular expression pattern to search for a match in the text.

<a id="analyzer.LexicalAnalyzer.extract_datetime"></a>

#### extract\_datetime

```python
def extract_datetime(text: str) -> Optional[datetime]
```

Extracts a datetime object from the given
text string using a regular expression pattern.

<a id="analyzer.LexicalAnalyzer.extract_message"></a>

#### extract\_message

```python
def extract_message(text) -> str
```

Extracts the message content from a given text. 
It uses a regular expression pattern to search for a match in the text.

<a id="analyzer.LexicalAnalyzer.process_file"></a>

#### process\_file

```python
def process_file(filename) -> None
```

Reads a text file and extracts the relevant data to create a Chat object.

**Arguments**:

- `filename` _str_ - The name of the file to process.
  

**Raises**:

- `FileNotFoundError` - If the file does not exist.
  

**Notes**:

  - The file must be in UTF-8 encoding.
  - The function iterates through each line of the file.
  - For each line, it extracts the date/time, author, and message.
  - If the date/time and author are not present, it is
  considered a continuation of the previous message.
  - The extracted data is used to create Message objects
  that are appended to the Chat object.

<a id="analyzer.LexicalAnalyzer.get_chat"></a>

#### get\_chat

```python
def get_chat() -> Chat
```

This function returns the current state of the chat,
which is an instance of the Chat class. It also resets
the current state of the chat to an empty Chat object.
This function can be used to obtain the chat after
processing it with the LexicalAnalyzer.

**Returns**:

  - A Chat object that contains the messages that were processed by the LexicalAnalyzer.
  

**Example**:

  ```python
  analyzer = LexicalAnalyzer()
  analyzer.process_file("chat.txt")
  chat = analyzer.get_chat()
  print(chat)
  ```

<a id="analyzer.WhatsappAnalyzer"></a>

## WhatsappAnalyzer Objects

```python
class WhatsappAnalyzer(object)
```

The WhatsappAnalyzer class processes a 
WhatsApp chat log file and generates a summary report.

<a id="analyzer.WhatsappAnalyzer.print_summary"></a>

#### print\_summary

```python
def print_summary() -> None
```

Generates a summary report of the chat log file
and prints it to the console.

