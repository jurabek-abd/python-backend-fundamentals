from textwrap import shorten

from rich.console import Console
from rich.table import Table


def display_movies_table(data, page=1):
    console = Console()

    table = Table(title="\n🎬 Movies", show_lines=True)
    table.add_column("#", style="dim", width=3)
    table.add_column("Title", style="bold")
    table.add_column("Release", width=10)
    table.add_column("Rating", justify="right", width=6)
    table.add_column("Popularity", justify="right", width=10)
    table.add_column("Overview")

    movies_per_page = 20
    start = (movies_per_page * (page - 1)) + 1

    for i, movie in enumerate(data.get("results", []), start=start):
        table.add_row(
            str(i),
            movie.get("title", "N/A"),
            movie.get("release_date", "N/A"),
            str(movie.get("vote_average", "N/A")),
            str(int(movie.get("popularity", 0))),
            shorten(movie.get("overview", ""), 80, placeholder="..."),
        )

    console.print(table)
