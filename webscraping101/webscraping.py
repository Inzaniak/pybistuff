## URLLIB #########################
# pip install pandas
import urllib.request
import pandas as pd

URL = 'https://www.w3schools.com/html/html_tables.asp'

with urllib.request.urlopen(URL) as response:
   html = response.read()
   
df = pd.read_html(html)[0]


## URLLIB + beautifulsoup #########################
# pip install pandas
# pip install beautifulsoup4
import urllib.request
from bs4 import BeautifulSoup

URL = 'https://www.w3schools.com/html/html_tables.asp'

with urllib.request.urlopen(URL) as response:
   html = response.read()
   
parser = BeautifulSoup(html, 'html.parser')
html_table = parser.find_all('table')[0].prettify()

df = pd.read_html(html_table)[0]


## REQUESTS_HTML #########################
# pip install requests-html
# pip install pandas
import requests_html
import pandas as pd

URL = 'https://www.w3schools.com/html/html_tables.asp'

ses = requests_html.HTMLSession()
res = ses.get(URL)
html_table = res.html.find("table", first=True).html

df = pd.read_html(html_table)[0]


## REQUESTS #########################
# pip install requests
# pip install pandas
import requests
import pandas as pd

URL = 'https://www.w3schools.com/html/html_tables.asp'

res = requests.get(URL)
html = res.content

df = pd.read_html(html)[0]


## SELENIUM #########################
# pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://www.w3schools.com/html/html_tables.asp'
driver = webdriver.Firefox(executable_path=r'PATH_TO_YOUR_WEBDRIVER')
driver.get(URL)

# Waiting for the page to load
table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "table"))
    )

table_html = table.get_attribute('outerHTML')

df = pd.read_html(table_html)[0]

driver.close()


## PANDAS #########################
#pip install pandas
import pandas as pd
df = pd.read_html('https://www.w3schools.com/html/html_tables.asp')[0]
