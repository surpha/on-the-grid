from src.news_fetcher.api_client import NewsAPIClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_news_api():
    # Print the API key (partially masked for security)
    api_key = os.getenv("NEWSAPI_KEY")
    if api_key:
        masked_key = api_key[:4] + "..." + api_key[-4:]
        print(f"Using API key: {masked_key}")
    else:
        print("ERROR: No API key found. Make sure you have NEWSAPI_KEY in your .env file")
        return

    # Initialize the news client
    news_client = NewsAPIClient()
    
    # Try to fetch some headlines
    category = "general"
    print(f"\nFetching top headlines in the '{category}' category...")
    
    articles = news_client.get_top_headlines(category=category, page_size=3)
    
    if not articles:
        print("No articles retrieved. Check your API key and internet connection.")
        return
        
    # Print the results
    print(f"Successfully retrieved {len(articles)} articles!\n")
    print("Sample headlines:")
    
    for i, article in enumerate(articles[:3], 1):
        print(f"{i}. {article.get('title')} - {article.get('source', {}).get('name', 'Unknown')}")
        print(f"   URL: {article.get('url')}")
        print()

if __name__ == "__main__":
    test_news_api()