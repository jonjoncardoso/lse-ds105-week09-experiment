import requests

import pandas as pd

from bs4 import BeautifulSoup

def get_all_headlines_as_df(wiki_url): 
    # Code from @tz1211
    response = requests.get(wiki_url)
    soup = BeautifulSoup(response.text, 'html.parser') 
    headlines_soup = soup.find_all(attrs={'class': 'mw-headline'}) 
    df = get_headlines_as_df(headlines_soup) 

    return df 


def get_headlines_as_df(headlines_soup):
    
    return pd.DataFrame({'headline id': [headline.get('id') for headline in headlines_soup],
                        'parent tag': [headline.parent.name for headline in headlines_soup], 
                        'parent tag text': [headline.parent.text for headline in headlines_soup]})