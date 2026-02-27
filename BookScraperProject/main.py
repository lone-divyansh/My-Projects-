import csv
from scraper import scrape_pages_generator

def clean_and_sort(raw_books):
    """
    Cleans raw book data and sorts it by price.
    
    Args:
        raw_books (list): A list of tuples ('Title', '£Price').
        
    Returns:
        list: A sorted list of tuples ('Title', float_Price).
    """
    print("Processing data...")
    
    # Step 1: List Comprehension for Cleaning
    # - Removes '£' symbol
    # - Strips whitespace
    # - Converts string to float
    cleaned = [
        (b[0], float(b[1].replace('£', '').strip())) 
        for b in raw_books
    ]
    
    # Step 2: Lambda Sort
    # Sorts the list based on the 2nd item (Index 1: The Price)
    cleaned.sort(key=lambda x: x[1])
    
    return cleaned

def save_to_csv(filename, books):
    """
    Saves a list of book tuples to a CSV file.
    
    Args:
        filename (str): The name of the file (e.g., 'data.csv').
        books (list): The list of book tuples to write.
    """
    # newline='' is REQUIRED on Windows to prevent blank lines between rows
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        
        # Write Column Headers
        writer.writerow(["Book Title", "Price (£)"])
        
        # Write all data rows at once
        writer.writerows(books)
        
    print(f"Success! Saved {len(books)} books to {filename}")

# --- Entry Point ---
# This block only runs if you execute 'python main.py' directly.
if __name__ == "__main__":
    print("--- Starting Book Scraper Project ---")
    
    start_url = "http://books.toscrape.com/index.html"
    
    # 1. Collection Phase
    # We iterate over the Generator to pull data into memory
    raw_data = []
    for book in scrape_pages_generator(start_url):
        raw_data.append(book)
        
    print(f"Collection Complete. Found {len(raw_data)} raw items.")
    
    # 2. Processing Phase
    final_data = clean_and_sort(raw_data)
    
    # 3. Storage Phase
    save_to_csv("organized_books.csv", final_data)