# DATA102 Final Project: Anime Recommendation System

## Problem Statement
The anime industry has grown rapidly in recent years, with a projected annual growth rate of 9.8% from 2025 to 2030 [1], earning billions of dollars in annual revenue. This boom in popularity resulted in significant growth in anime production, with new anime being released every year. This resulted in a vast and diverse catalog, making it difficult to discern quality and keep up with the constant influx of new releases and numerous genres. As a result, users have the problem of navigating this saturated market to find anime that matches their unique preferences, hence the importance of an anime recommendation system.

Numerous shows are released, yet many are often overlooked due to current recommender systems and social groups interacting with only the most recent or most popular suggestions. Numerous hours and investments would have been wasted if viewers were not provided a chance to find these niche shows; hence, this recommender system aims to include niche content.

The goal of this project is to develop an effective recommendation system for anime using both collaborative filtering and content-based filtering approaches. The system aims to provide personalized recommendations based on user interactions and item characteristics.

## Data Collection
The dataset is gathered from MyAnimeList (MAL), a popular anime database. Data is sourced from different pages, including seasonal anime lists and user watchlists. A web scraper was implemented to extract data from MyAnimeList. The seasonal anime lists and user watchlists were compiled using custom scripts, with the extracted information stored in CSV files. Regular expressions and automated scripts were used to parse and clean URLs, ensuring accurate extraction of anime IDs and related metadata. The collected data includes attributes such as anime titles, genres, themes, ratings, and user preferences.

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
- Anime Stats Page containing aggregated and individual viewership

## Exploratory Data Analysis (EDA)
Exploratory analysis was conducted to understand the dataset. Summary statistics were generated for numerical features such as ratings, number of members, and episode counts. Missing values in certain columns like 'Score' and 'Episodes' were identified, along with duplicate records from anime appearing across multiple seasons.

## Data Preprocessing
Preprocessing involved merging datasets from different sources, such as seasonal anime lists and user ratings. The data was formatted into structured tables with relevant fields. Columns such as 'MAL_id' were extracted from URLs, and categorical features like 'Genres' and 'Themes' were transformed for further processing.

### Data Cleaning
The dataset also undergoes data cleaning by removing duplicate records, handling missing values, and standardizing numerical features. Null values in 'Score' and 'Episodes' were imputed with zeros. Addtionally, the dataset was filtered to remove inconsistencies, ensuring a more accurate representation.

### Feature Engineering
Feature engineering involves transforming categorical and numerical features for model training. One-hot encoding was applied to categorical variables such as 'Genres', 'Themes', and 'Airing Status'. Numerical features like 'Score', 'Favorites', and 'Members' were scaled using MinMaxScaler to prevent dominance over categorical variables in similarity calculations.

## Modeling
The recommendation system was implemented using two main approaches:
- Collaborative Filtering: User-item interaction data was used to compute similarity scores between users and items using cosine similarity.
- Content-Based Filtering: A similarity matrix was generated based on anime attributes, using both categorical and numerical features. Cosine similarity was applied to compare anime entries.

## Evaluation
The models were evaluated based on their ability to recommend relevant anime. Common evaluation metrics such as precision, recall, and mean average precision (MAP) were considered. Visualizations of similarity matrices and ranked recommendation lists were used to assess the effectiveness of the models.

## Conclusion
