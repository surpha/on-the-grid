import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Keys
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")
NYT_API_KEY = os.getenv("NYT_API_KEY")
GUARDIAN_API_KEY = os.getenv("GUARDIAN_API_KEY")

# News Categories
CATEGORIES = ['general', 'business', 'technology', 'sports', 'science', 'health']

# Grid Configuration
GRID_SIZE = 9
MAX_SUMMARY_LENGTH = 100