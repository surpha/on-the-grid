import requests
from config.config import NEWSAPI_KEY, CATEGORIES

class NewsAPIClient:
    """Client for fetching news from NewsAPI.org"""
    
    def __init__(self, api_key=NEWSAPI_KEY):
        self.api_key = api_key
        self.base_url = "https://newsapi.org/v2"
        
    def get_top_headlines(self, category='general', country='us', page_size=10):
        """Fetch top headlines from a specific category"""
        url = f"{self.base_url}/top-headlines"
        params = {
            'apiKey': self.api_key,
            'category': category,
            'country': country,
            'pageSize': page_size
        }
        
        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                return response.json()['articles']
            else:
                print(f"Error fetching news: {response.status_code}")
                return []
        except Exception as e:
            print(f"Exception during news fetch: {e}")
            return []
            
    def get_everything(self, query, from_date=None, to_date=None, page_size=10):
        """Search for articles matching query"""
        url = f"{self.base_url}/everything"
        params = {
            'apiKey': self.api_key,
            'q': query,
            'pageSize': page_size
        }
        
        if from_date:
            params['from'] = from_date
        if to_date:
            params['to'] = to_date
            
        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                return response.json()['articles']
            else:
                print(f"Error fetching news: {response.status_code}")
                return []
        except Exception as e:
            print(f"Exception during news fetch: {e}")
            return []