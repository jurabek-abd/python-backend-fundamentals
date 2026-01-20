import csv
from pathlib import Path

import requests
from bs4 import BeautifulSoup

DATA_DIR = Path("data")
DATA_FILE = DATA_DIR / "postings.csv"

POSTING_CONTAINER_CLASS = "column is-half"
POSTING_TITLE_CLASS = "title is-5"
POSTING_COMPANY_CLASS = "subtitle is-6 company"
POSTING_LOCATION_CLASS = "location"
POSTING_HREF_START = "https://realpython.github.io/fake-jobs/jobs"


def save_to_csv(postings):
    """Saves list of dicts to a CSV file."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    try:
        with open(DATA_FILE, mode="w", newline="") as f:
            writer = csv.DictWriter(
                f, fieldnames=["title", "company", "location", "url"]
            )

            writer.writeheader()

            for posting in postings:
                writer.writerow(
                    {
                        "title": posting.get("title", ""),
                        "company": posting.get("company", ""),
                        "location": posting.get("location", ""),
                        "url": posting.get("url", ""),
                    }
                )
            return True
    except Exception as e:
        print(f"# Error: {e}")
        return False


def fetch_page():
    """Fetches and returns the webpage as a string."""
    url = "https://realpython.github.io/fake-jobs/"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            return response.text
        else:
            response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"# Error: {e}")
        return None


def extract_job_postings(response):
    """Scrapes data from webpage and returns list of dicts."""
    soup = BeautifulSoup(response, "html.parser")
    postings = []
    posting_boxes = soup.find_all("div", class_=POSTING_CONTAINER_CLASS)
    for box in posting_boxes:
        box_title = box.find("h2", class_=POSTING_TITLE_CLASS)
        box_company = box.find("h3", class_=POSTING_COMPANY_CLASS)
        box_location = box.find("p", class_=POSTING_LOCATION_CLASS)
        box_link = box.find(
            "a",
            href=(lambda h: h and h.startswith(POSTING_HREF_START),),
        )

        posting = {
            "title": box_title.get_text(strip=True) if box_title else "N/A",
            "company": box_company.get_text(strip=True) if box_company else "N/A",
            "location": box_location.get_text(strip=True) if box_location else "N/A",
            "url": box_link.get("href") if box_link else "N/A",
        }
        postings.append(posting)
    return postings


def main():
    """Orchestrates everything."""
    response = fetch_page()

    if not response:
        print("# Failed to fetch the page. Try Again")
        return

    postings = extract_job_postings(response)

    if len(postings) == 0:
        print("# No data scraped")
        return

    result = save_to_csv(postings)

    if result:
        print(f"# Successfully saved to: {DATA_FILE}")
    else:
        print("# Something went wrong. Try again")


if __name__ == "__main__":
    main()
