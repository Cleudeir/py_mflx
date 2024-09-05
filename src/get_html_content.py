import requests
from urllib.parse import quote
from bs4 import BeautifulSoup

def get_html_content(url):
    # Properly encode the URL to handle special characters
    encoded_url = quote(url, safe='/:')
    
    try:
        response = requests.get(encoded_url)
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
        return response.text
    except requests.exceptions.RequestException as e:
        try:
            # Use a web crawler to access the page and get content if there is an error
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
            response = requests.get(encoded_url, headers=headers)
            response.raise_for_status()           
            return response.text
        except requests.exceptions.RequestException as crawler_error:
            return f"Error: Unable to fetch the page even with a crawler. Details: {crawler_error}"
