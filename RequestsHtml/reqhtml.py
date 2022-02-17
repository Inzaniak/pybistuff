import requests_html
import pandas as pd

"""
QUICK EXAMPLE ON HOW TO USE REQUESTS_HTML
"""

# CREATE HTML SESSION
sess = requests_html.HTMLSession()
url = 'https://en.wikipedia.org/wiki/Winter_Olympic_Games'

# GET HTTP RESPONSE
res = sess.get(url)
html_page = res.html

# FIND ALL THE TABLES IN THE PAGE
tables = html_page.find('.wikitable')
for num,table in enumerate(tables):
    print(f"Table{num}:",table.find('tr', first=True).text.replace('\n',' '))

# SELECT THE TABLE WE NEED
table_medals = tables[1]

# To use pandas read_html you need to install html5lib
# pip install html5lib
table_medals_df = pd.read_html(table_medals.html)[0]
print(table_medals_df)
