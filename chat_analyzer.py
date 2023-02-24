"""
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

Example:
```bash
# Analyze a chat log file and show summary
python chat_analyzer.py chat.txt

# Install NLTK dependencies
python chat_analyzer.py --install

# Show help
python chat_analyzer.py --help
```
"""

from os.path import exists
from typing import Optional

from nltk import download
from typer import run, Option, Argument, BadParameter

from analyzer import WhatsappAnalyzer

def file_callback(file: Optional[str]) -> str:
    """
    file_callback
        Checks if a file exists and throws an exception if not.

    Raises:
        BadParameter: If the file does not exist.
    """
    if file is None:
        return
    if not exists(file):
        raise BadParameter(f"El archivo {file} no existe.")
    return file

def main(
    file: Optional[str] = Argument(
        None, help="File name o path.", callback=file_callback
    ),
    install: bool = Option(
        False, "--install", "-i", help="Install nltk dependencies."
    ),
    words: int = Option(
        30, "--words", "-w", help="Number of words to show in the summary."
    ),
    emojis: int = Option(
        15, "--emojis", "-e", help="Number of emojis to show in the summary"
    )
):
    if install and file is None:
        download("punkt")
        download("stopwords")
        download("wordnet")
        download("vader_lexicon")
        return

    analyzer = WhatsappAnalyzer(file, words, emojis)
    analyzer.print_summary()

if __name__ == "__main__":
    run(main)
