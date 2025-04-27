import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

url = "https://www.example.com"  # Replace with the URL you want to scrape
html_content = fetch_html(url)

if html_content is not None:
    soup = BeautifulSoup(html_content, 'html.parser')
    # Extract data from the HTML content (e.g., extract all text within a specific tag)
    # Example: Extract all text within an article element
    articles = soup.find_all('article')  # Replace with your specific elements to extract data

    for article in articles:
        # Extract and print the text of each article
        print(article.get_text())

else:
    print("Failed to retrieve HTML content.")
