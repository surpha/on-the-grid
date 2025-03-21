from newspaper import Article
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

# Download required NLTK data
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

class ContentProcessor:
    """Process news articles to extract and summarize content"""
    
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        
    def extract_article_content(self, url):
        """Extract full article content using newspaper3k"""
        try:
            article = Article(url)
            article.download()
            article.parse()
            return article.text
        except Exception as e:
            print(f"Error extracting content from {url}: {e}")
            return None
            
    def summarize_text(self, text, max_sentences=3):
        """Create a simple extractive summary of text"""
        if not text:
            return "No content available."
            
        # Tokenize the text into sentences
        sentences = sent_tokenize(text)
        
        if len(sentences) <= max_sentences:
            return text
            
        # Calculate word frequency
        word_frequencies = {}
        for word in word_tokenize(text.lower()):
            if word not in self.stop_words and word.isalnum():
                if word not in word_frequencies:
                    word_frequencies[word] = 1
                else:
                    word_frequencies[word] += 1
        
        # Calculate sentence scores based on word frequency
        sentence_scores = {}
        for sentence in sentences:
            for word in word_tokenize(sentence.lower()):
                if word in word_frequencies:
                    if sentence not in sentence_scores:
                        sentence_scores[sentence] = word_frequencies[word]
                    else:
                        sentence_scores[sentence] += word_frequencies[word]
        
        # Get top sentences
        import heapq
        summary_sentences = heapq.nlargest(max_sentences, sentence_scores, key=sentence_scores.get)
        
        # Ensure sentences are in the original order
        ordered_summary = [s for s in sentences if s in summary_sentences]
        
        # Join sentences into summary
        summary = ' '.join(ordered_summary)
        
        return summary