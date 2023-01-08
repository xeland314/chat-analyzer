from analyzer import WhatsappAnalyzer
from typer import run, Option, Argument

def main(
    file: str = Argument(..., help="File name o path."), 
    install: bool = Option(
        False, "--install", "-i", help="Install nltk dependencies."
    )
):
    if install:
        import nltk
        nltk.download("punkt")
        nltk.download("stopwords")

    analyzer = WhatsappAnalyzer(file)
    analyzer.print_summary()
    del(analyzer)

if __name__ == "__main__":
    run(main)