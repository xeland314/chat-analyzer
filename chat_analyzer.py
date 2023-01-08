from analyzer import WhatsappAnalyzer
from os.path import exists
from typer import run, Option, Argument

def main(
    file: str = Argument(..., help="File name o path."), 
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
    if install:
        import nltk
        nltk.download("punkt")
        nltk.download("stopwords")

    if not exists(file):
        raise FileNotFoundError(f"El archivo {file} no existe.")

    analyzer = WhatsappAnalyzer(file, words, emojis)
    analyzer.print_summary()
    del(analyzer)

if __name__ == "__main__":
    run(main)