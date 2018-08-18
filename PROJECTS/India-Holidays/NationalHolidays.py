from requests import get
from bs4 import BeautifulSoup as bs

# National Holidays data found under below url
url = 'https://www.goodreturns.in/bank-holidays-in-andhra-pradesh.html'

# reading the html data from the url using requests.get() method
html_data = get(url).text

# Parsing the html data to bs4 readable format
soup = bs(html_data, 'html.parser')

count=0

# This is where the real scrapping starts
for i in soup.findAll('tr'): # tr is the tag in html; I am here getting all the text with tr tag
        if count is 0:
            count+=1
            continue

        # <tr>.text returns only the text between tags <tr>...TEXT...</tr>
        x = str(i.text).strip().split('\n')  # Converted to list
        if x[0] == 'Month Wise Bank Holiday in Andhra Pradesh':
            break
        print("{0:<25} {1} ".format(x[0], x[2]))