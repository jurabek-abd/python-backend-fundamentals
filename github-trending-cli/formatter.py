from rich.console import Console
from rich.table import Table


def format_repos(repos):
    console = Console()

    table = Table(
        show_header=True,
        header_style="bold cyan",
        show_lines=False,
        box=None,
        padding=(0, 1),
    )

    table.add_column("Repository", style="bold white", no_wrap=True)
    table.add_column("Description", style="dim", overflow="fold")
    table.add_column("Stars", justify="right", style="yellow")
    table.add_column("Language", style="green")

    for repo in repos:
        name = repo.get("full_name") or repo.get("name", "—")
        description = repo.get("description") or "No description"
        stars = repo.get("stargazers_count", 0)
        language = repo.get("language") or "—"

        table.add_row(
            name,
            description,
            f"★ {stars:,}",
            language,
        )

    console.print(table)
