from abc import ABC, abstractmethod

from bs4 import BeautifulSoup

import re
import pandas as pd



class ScrapedPage(ABC):
    @abstractmethod
    def parse() -> dict:
        return {}

    def cleanString(item : str) -> str :
        return re.sub(r'\s+', ' ', item).strip()



class SeasonPage(ScrapedPage):
    def parse(soup : BeautifulSoup) -> dict:
        link_titles = soup.find_all(class_ ='link-title')

        return {
            'Title':[a.text for a in link_titles], 
            'Link':[a.get('href') for a in link_titles]
        }




class DetailsPage(ScrapedPage):
    def parse(soup : BeautifulSoup) -> dict:
        output = {}

        try:
            DetailsPage.parseLeftPanel(soup, output)
        except Exception as e:
            print('Left Panel Failed')
            
        try:
            DetailsPage.parseScore(soup, output)
        except Exception as e:
            print('Score Failed')
                  
        try:
            DetailsPage.parseSynopsis(soup, output)
        except Exception as e:
            print('Synopsis Failed')

        try:
            DetailsPage.parseRelatedEntries(soup, output)
        except Exception as e:
            print('Related Entries Failed')
        
        return output

    def parseLeftPanel(soup : BeautifulSoup, output : dict) :
        for d in soup.find_all(class_='dark_text'):
            label = d.text.replace(':','').strip()
            content = d.find_next_sibling(string=True).strip()
            
            if content == '':
                content = [a.text.strip() for a in d.find_next_siblings('a')]
        
            output[label] = content

    def parseScore(soup : BeautifulSoup, output : dict) :
        e = soup.find('span', attrs={'itemprop':'ratingValue'})

        if e is None:
            print('No score')
            raise ValueError
        
        output['Score'] = e.text.strip()
        output['Scorers'] = soup.find('span', attrs={'itemprop':'ratingCount'}).text.strip()

    def parseSynopsis(soup : BeautifulSoup, output : dict) :
        output['Synopsis'] = DetailsPage.cleanString(soup.find('p', attrs={'itemprop':'description'}).text)

    def parseRelatedEntries(soup : BeautifulSoup, output : dict) :
        output['Related_Entries'] = [DetailsPage.cleanString(entry.text) for entry in soup.find_all('div', attrs={'class':'entry borderClass'})]




class StatisticsSummaryPage(ScrapedPage):
    def parse(soup : BeautifulSoup) -> dict :
        output = {}

        try:
            StatisticsSummaryPage.parseSummary(soup, output)
            StatisticsSummaryPage.parseScores(soup, output)

        except Exception as e:
            print(e)
        
        finally:
            return output

        
    @staticmethod
    def parseSummary(soup : BeautifulSoup, output : dict):
        H2_SUMMARY = soup.find('h2', attrs={'id':'summary_stats'})

        for s in H2_SUMMARY.find_all_next('span', attrs={'class':'dark_text'}):
            output[s.text.strip(':')] = s.find_next_sibling(string=True).strip()

    @staticmethod
    def parseScores(soup : BeautifulSoup, output : dict):
        TABLE_SCORE = soup.find('table', attrs={'class':'score-stats'})
        
        for tr in TABLE_SCORE.find_all('tr'):
            output[tr.select('.score-label')[0].text] = re.search(r'(\d+)', tr.find('small').text).group(1)




class StatisticsSubmissionPage(ScrapedPage):
    def parse(soup : BeautifulSoup) -> dict :
        table = soup.find('table', attrs={'class':'table-recently-updated'})

        rows = [[header.text for header in table.find('tr').find_all('td')]]
        
        
        for tr in table.find_all('tr')[1:]:
            row = [tr.find('a', attrs={'class':'word-break'}).text.strip()]
            [row.append(td.text.strip()) for td in tr.find_all('td', attrs={'class':'borderClass ac'})]
    
            rows.append(row)
        return rows

    def parseAsDf(soup : BeautifulSoup) -> pd.DataFrame :
        rows = StatisticsSubmissionPage.parse(soup)
        return pd.DataFrame(rows[1:], columns=rows[0])