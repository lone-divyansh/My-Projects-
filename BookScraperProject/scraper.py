import requests
from bs4 import BeautifulSoup
from utils import timer

@timer
def scrape_pages_generator(url):
    """
    A Recursive Generator that scrapes book data from the website.
    
    Instead of returning a list, this function YIELDS one book at a time.
    It automatically detects the 'Next' button and calls itself recursively
    to scrape subsequent pages.

    Args:
        url (str): The URL of the page to scrape (e.g., index.html).

    Yields:
        tuple: A tuple containing (Book Title, Price String).
        Example: ('A Light in the Attic', '£51.77')
    """
    print(f"Scraping URL: {url}")
    
    # 1. Network Request
    response = requests.get(url)
    
    # Fix encoding issues (prevents 'Â' characters in currency)
    response.encoding = 'utf-8' 
    
    # 2. Create the Soup (Parse HTML)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # 3. Extract Books on CURRENT page
    books = soup.find_all("article", class_="product_pod")
    
    for book in books:
        # Extract raw text from specific HTML tags
        title = book.h3.a['title']
        price_text = book.find("p", class_="price_color").text
        
        # YIELD sends data back to main.py immediately, pausing this function
        yield (title, price_text)
        
    # 4. Recursion Logic (Find the Next Page)
    next_button = soup.find("li", class_="next")
    
    if next_button:
        # Extract the relative link (e.g., "page-2.html")
        next_page_partial = next_button.a['href']
        
        # Construct the Full URL
        # The website logic varies slightly depending on if we are in 'catalogue' or root
        if "catalogue" not in next_page_partial:
            full_next_url = "http://books.toscrape.com/catalogue/" + next_page_partial
        else:
            full_next_url = "http://books.toscrape.com/" + next_page_partial
            
        # SAFETY BRAKE: Stop recursion at page 4 to save time during testing
        if "page-4" in full_next_url:
            print("Safety limit reached (3 pages). Stopping generator.")
            return 
        
        # RECURSIVE CALL:
        # 'yield from' tells Python to take all items from the next page's generator
        # and pass them up the chain.
        yield from scrape_pages_generator(full_next_url)