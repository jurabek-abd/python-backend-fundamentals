# Python Job Listings Scraper

A beginner-friendly web scraper that collects job listings from the [Fake Python Jobs](https://realpython.github.io/fake-jobs/) website and saves them to a CSV file.

This project is part of my Python learning journey, inspired by the [roadmap.sh Python projects](https://roadmap.sh/python/projects).

## Features

- Scrapes job postings including title, company, location, and job detail URL
- Exports data to CSV format for easy analysis
- Handles missing data gracefully
- Clean, readable code structure

## Requirements

- Python 3.x
- requests
- beautifulsoup4

## Installation

```bash
pip install requests beautifulsoup4
```

## Usage

Simply run the script:

```bash
python main.py
```

The scraped job listings will be saved to `data/postings.csv`.

## Project Structure

```
job-listings-scraper/
├── main.py           # Main scraper script
└── data/
    └── postings.csv  # Output file (generated after running)
```

## What I Learned

- HTML parsing with BeautifulSoup
- Making HTTP requests with the requests library
- Working with CSV files in Python
- Error handling and defensive programming
- Code organization and separation of concerns

## License

Feel free to use this code for learning purposes.
