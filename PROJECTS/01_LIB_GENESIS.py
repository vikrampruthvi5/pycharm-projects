"""
Goal is to use requests and bs4 to get the list of books and to be able to download them programatically.
"""

# imports
import requests
from bs4 import BeautifulSoup as bs

# Global variables
search = "tkinter"
import requests


def list_books():
    url = 'http://gen.lib.rus.ec/search.php?req=' + search + '&lg_topic=libgen&open=0&view=simple&res=25&phrase=0&column=def'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }
    source_code = requests.get(url, headers=headers)
    plain_text = source_code.text

    # Converting plain text into soup
    soup = bs(plain_text, "html.parser")

    for book in soup.findAll('a', {'title': 'Gen.lib.rus.ec'}):
        href = book.get('href')
        download_book(href)


def download_book(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    source_code = requests.get(url, headers=headers)
    plain_text = source_code.text

    # Converting plain text into soup
    soup = bs(plain_text, "html.parser")
    for book in soup.findAll('td', {'id':'info'}):
        plain_text = str(book)
        soup = bs(plain_text, "html.parser")

        # Title for the book
        for i in soup.findAll('h1'):
            print(i.get_text())

        count = 0
        # Author, publisher, isbn for the book
        for i in soup.findAll('p'):

            # Publisher
            if count is 1:
            #     # Condition to check for the "Series"
            #     x = str(i.get_text()).split(':')[1].strip()
            #     if x is 'Series':
            #         continue
                print(i.get_text())

            # Authors
            if count is 0:
                text = str(i.get_text())
                auth = text.split(':')
                print(auth[1].strip())
                count += 1

        # Title for the book
        for i in soup.findAll('a'):
            print("Download link : "+i.get('href'))
            break
        print()

        print("- "*100, "\n")

list_books()
