# Email Scraper

This is a Python script that scrapes email addresses from web pages using Google search. The script allows the user to choose between a simple search or a domain search. For simple search, the user enters a search string and the number of Google results to retrieve. For domain search, the user enters a domain and the number of Google results to retrieve. The script then scrapes email addresses from the retrieved web pages and saves them to a file.

## Dependencies

This script requires the following Python packages:

- `googlesearch`
- `requests`
- `beautifulsoup4`

You can install these dependencies by running:

```
pip install google googlesearch beautifulsoup4
```

## How to use

1. Install the required dependencies as described above.

2. Clone this repository.

3. Navigate to the repository directory in a terminal.

4. Run the script using the command `python email_scraper.py`.

5. Choose a search type by entering 1 for a simple search or 2 for a domain search.

6. Enter the search string or domain and the number of Google results to retrieve.

7. The script will then scrape email addresses from the retrieved web pages and save them to a file called `emails.list` in the same directory as the script.

