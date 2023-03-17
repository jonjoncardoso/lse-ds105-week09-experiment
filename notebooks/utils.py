import pandas as pd

def get_headlines_as_df(headlines_soup):
    
    return pd.DataFrame({'headline id': [headline.get('id') for headline in headlines_soup],
                        'parent tag': [headline.parent.name for headline in headlines_soup], 
                        'parent tag text': [headline.parent.text for headline in headlines_soup]})