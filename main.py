from analyzer import WhatsappAnalyzer
from typer import run, Option

def main(
    filename: str = Option(
        ..., "--file", "-f", help="File name o path.", 
    )
):
    analyzer = WhatsappAnalyzer(filename)
    analyzer.print_summary()
    del(analyzer)

if __name__ == "__main__":
    run(main)