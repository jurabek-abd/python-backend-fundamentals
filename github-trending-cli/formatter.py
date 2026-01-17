from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text


def output_repos(data):
    """
    Pretty-prints GitHub JSON response with an aesthetic CLI format.
    """
    console = Console()

    # Header panel
    total = data.get("total_count", 0)
    header = Panel(
        f"[bold cyan]GitHub Repository Search Results[/bold cyan]\n"
        f"[dim]Total repositories found: {total:,}[/dim]",
        box=box.DOUBLE,
        border_style="cyan",
    )
    console.print(header)
    console.print()

    # Create table
    table = Table(
        show_header=True,
        header_style="bold magenta",
        border_style="blue",
        box=box.ROUNDED,
        title="[bold]📚 Repositories[/bold]",
        title_style="bold green",
    )

    table.add_column("Repository", style="cyan", no_wrap=False, width=35)
    table.add_column("Description", style="white", no_wrap=False, width=50)
    table.add_column("⭐ Stars", justify="right", style="yellow")
    table.add_column("Language", style="green", justify="center")

    # Add rows
    for item in data.get("items", []):
        name = item.get("full_name", "N/A")
        description = item.get("description") or "[dim]No description[/dim]"
        stars = f"{item.get('stargazers_count', 0):,}"
        language = item.get("language") or "[dim]None[/dim]"

        # Truncate description if too long
        if len(description) > 100:
            description = description[:97] + "..."

        table.add_row(name, description, stars, language)

    console.print(table)
    console.print()

    # Footer
    footer = Text.from_markup(
        f"[dim]Showing {len(data.get('items', []))} repositories[/dim]",
        justify="center",
    )
    console.print(footer)
