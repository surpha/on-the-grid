from datetime import datetime
from config.config import GRID_SIZE, MAX_SUMMARY_LENGTH, CATEGORIES

class GridFormatter:
    """Format processed news articles into a grid layout"""
    
    def __init__(self, grid_size=GRID_SIZE):
        self.grid_size = grid_size
        
    def create_balanced_grid(self, articles):
        """Select articles to create a balanced grid across categories"""
        selected_articles = []
        
        # Ensure at least one article from main categories
        main_categories = ['general', 'business', 'sports']
        for category in main_categories:
            category_articles = [a for a in articles if a.get('category') == category]
            if category_articles:
                selected_articles.append(category_articles[0])
                # Remove from articles list to avoid duplication
                articles = [a for a in articles if a != category_articles[0]]
        
        # Fill remaining slots with other articles
        remaining_slots = self.grid_size - len(selected_articles)
        if remaining_slots > 0 and articles:
            # In a real implementation, would sort by importance
            remaining_articles = articles[:remaining_slots]
            selected_articles.extend(remaining_articles)
        
        return selected_articles
        
    def format_for_display(self, articles):
        """Format articles for display in grid"""
        formatted_articles = []
        
        for article in articles:
            # Truncate summary if needed
            summary = article.get('summary', '')
            if len(summary) > MAX_SUMMARY_LENGTH:
                summary = summary[:MAX_SUMMARY_LENGTH-3] + '...'
                
            formatted = {
                'category': article.get('category', 'general').upper(),
                'title': article.get('title', 'No Title'),
                'summary': summary,
                'source': article.get('source', 'Unknown Source'),
                'url': article.get('url', '')
            }
            
            formatted_articles.append(formatted)
            
        return formatted_articles
        
    def generate_html_grid(self, formatted_articles):
        """Generate HTML for the news grid"""
        date_str = datetime.now().strftime('%B %d, %Y')
        
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>On the GRID - {date_str}</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                .grid-container {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; }}
                .grid-item {{ border: 1px solid #ddd; padding: 15px; }}
                .category {{ font-size: 12px; color: #666; text-transform: uppercase; }}
                .title {{ font-size: 16px; font-weight: bold; margin: 5px 0; }}
                .summary {{ font-size: 14px; line-height: 1.4; }}
                .source {{ font-size: 12px; color: #666; font-style: italic; margin-top: 10px; }}
                h1, h2 {{ text-align: center; }}
            </style>
        </head>
        <body>
            <h1>ON THE GRID</h1>
            <h2>{date_str}</h2>
            
            <div class="grid-container">
        """
        
        for article in formatted_articles:
            html += f"""
                <div class="grid-item">
                    <div class="category">{article['category']}</div>
                    <div class="title">{article['title']}</div>
                    <div class="summary">{article['summary']}</div>
                    <div class="source">Source: {article['source']}</div>
                </div>
            """
            
        html += """
            </div>
        </body>
        </html>
        """
        
        return html