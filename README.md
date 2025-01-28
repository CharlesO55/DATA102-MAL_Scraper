# DATA102 MyAnimeList.net Scraper

Common Variables to Alter:
- Scraper.MINIMUM_DELAY # Delay per scrape to avoid being blocked
- YEAR : int
- SEASON : Scraper.SEASONS # enum

Files
- Notebooks:
  - Dev # Step by step Discussion
  - Automation # Full automated implementation
- Modules
  - Scraper.py
  - ScrapedPage.py


Packages used:
- BeautifulSoup4
- requests
- re
- pandas
- typing (Python 10+)
  

Outputs [.csv files]:
- Season/
- Detail/
- Statistics/Submissions/
- Statistics/Summary/

Targets:
- Season Page containing Anime Titles and Page Links
- Anime Details Page containing general info
- Anime Stats Page containing aggregated and individual viewerships
