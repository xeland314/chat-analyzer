from analyzer import WhatsappAnalyzer
from os.path import exists
from typer import run, Option, Argument, BadParameter
from typing import Optional

def file_callback(file: str) -> None:
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
        import nltk
        nltk.download("punkt")
        nltk.download("stopwords")
        return

    analyzer = WhatsappAnalyzer(file, words, emojis)
    analyzer.print_summary()
    del(analyzer)

if __name__ == "__main__":
    run(main)