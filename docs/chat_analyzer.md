# Table of Contents

* [chat\_analyzer](#chat_analyzer)
  * [file\_callback](#chat_analyzer.file_callback)

<a id="chat_analyzer"></a>

# chat\_analyzer

chat_analyzer - analyze WhatsApp chats

This module provides a command-line interface to analyze WhatsApp chat
logs. It uses the `analyzer` module to compute statistics and generate
a summary of the chat, which is printed to the console using the `rich`
library. The `typer` library is used to define the command-line options.

Author: Christopher Villamarín (xeland314)

Dependencies:
- os
- typing
- rich
- typer
- nltk (if `--install` option is used)
- analyzer (custom module)

Usage:
- To analyze a chat, run `python chat_analyzer.py <file>`.
- To install NLTK dependencies, run `python chat_analyzer.py --install`.

Options:
- `file`: Name or path of the chat log file. Required for analysis.
- `--install`, `-i`: Install NLTK dependencies and exit.
- `--words`, `-w`: Number of words to show in the summary (default: 30).
- `--emojis`, `-e`: Number of emojis to show in the summary (default: 15).

Functions:
- `file_callback(file: str) -> str`: A callback function for the `typer`
library, used to check if a file exists before running the analysis.

**Example**:

```bash
# Analyze a chat log file and show summary
python chat_analyzer.py chat.txt

# Install NLTK dependencies
python chat_analyzer.py --install

# Show help
python chat_analyzer.py --help
```

<a id="chat_analyzer.file_callback"></a>

#### file\_callback

```python
def file_callback(file: str) -> str
```

file_callback
Checks if a file exists and throws an exception if not.

**Raises**:

- `BadParameter` - If the file does not exist.

