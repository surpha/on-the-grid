import os
from datetime import datetime
from src.news_fetcher.api_client import NewsAPIClient
from src.processors.content_processor import ContentProcessor
from src.grid_generator.grid_formatter import GridFormatter
from config.config import CATEGORIES

def main():
    print("Starting On the GRID news generator...")
    
    # Initialize components
    news_client = NewsAPIClient()
    processor = ContentProcessor()
    grid_formatter = GridFormatter()
    
    # Collect news from different categories
    all_articles = []
    for category in CATEGORIES:
        print(f"Fetching {category} news...")
        articles = news_client.get_top_headlines(category=category, page_size=5)
        
        # Process each article
        for article in articles:
            # Extract full content when available
            content = processor.extract_article_content(article.get('url'))
            
            # Create summary
            if content:
                summary = processor.summarize_text(content)
            else:
                summary = article.get('description', 'No description available')
                
            # Add to processed articles
            processed_article = {
                'title': article.get('title'),
                'summary': summary,
                'source': article.get('source', {}).get('name', 'Unknown'),
                'url': article.get('url'),
                'published': article.get('publishedAt'),
                'category': category
            }
            
            all_articles.append(processed_article)
    
    # Create balanced grid
    grid_articles = grid_formatter.create_balanced_grid(all_articles)
    
    # Format for display
    formatted_grid = grid_formatter.format_for_display(grid_articles)
    
    # Generate HTML
    html_output = grid_formatter.generate_html_grid(formatted_grid)
    
    # Create output directory if it doesn't exist
    os.makedirs('output', exist_ok=True)
    
    # Save to file
    date_str = datetime.now().strftime('%Y-%m-%d')
    output_file = f"output/grid_{date_str}.html"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_output)
        
    print(f"News grid generated and saved to {output_file}")
    
    # Also print a text version to console
    print("\n===== ON THE GRID - NEWS MAT DEMO =====")
    print(f"Date: {datetime.now().strftime('%B %d, %Y')}\n")
    
    for i, article in enumerate(formatted_grid, 1):
        print(f"+---------- GRID CELL {i} ----------+")
        print(f"[{article['category']}]")
        print(f"{article['title']}")
        print(f"\n{article['summary']}")
        print(f"\nSource: {article['source']}")
        print("+"+"-"*30+"+\n")
    
    print("===== END OF NEWS MAT DEMO =====")

if __name__ == "__main__":
    main()