import requests_html
import sqlite3

url = 'https://www.cnet.com/tech/computing/{page}/'
sess = requests_html.HTMLSession()

class Article:
    
    def __init__(self, title, url):
        self.title = title
        self.url = url
        self.author = None
        self.short_description = None
        self.date = None
        self.text = None
        
    def get_full_article(self):
        """Get the full article from the url
        """        
        art_sess = requests_html.HTMLSession()
        art_res = art_sess.get(self.url)
        try:
            self.date = art_res.html.find('time',first=True).attrs['datetime']
            full_text = []
            for el in art_res.html.find('.article-main-body',first=True).find('p'):
                full_text.append(el.text)
            self.text = '\n'.join(full_text)
        except KeyError as e:
            print(f'KeyError: {e}')
            
    def __str__(self):
        return "{}, {}".format(self.title, self.url)

# DATA SCRAPING
articles = []
for page in range(1,2):
    res = sess.get(url.format(page=page))
    html = res.html
    for html_article in html.find('.item'):
        title = html_article.find('h3', first=True).text
        print('Scraping article:', title)
        url = [el for el in list(html_article.absolute_links) if 'profiles' not in el][0]
        article = Article(title, url)
        article.short_description = html_article.find('p', first=True).text
        article.author = html_article.find('span', first=True).text.replace('by ','')
        article.get_full_article()
        articles.append(article)
        print('Scraped article:', article.title)
        print('-' * 20)

# DATA STORAGE
conn = sqlite3.connect('cnet_articles.db')
conn.execute('''CREATE TABLE IF NOT EXISTS articles ( 
             artTitle TEXT PRIMARY KEY,
             artUrl TEXT,
             artAuthor TEXT,
             artShortDesc TEXT,
             artDate TEXT,
             artText TEXT
             )''')
conn.commit()
for article in articles:
    conn.execute('''INSERT OR IGNORE INTO articles VALUES (?,?,?,?,?,?)''',
                 (article.title, article.url, article.author, article.short_description, article.date, article.text))
conn.commit()

conn.execute('''SELECT * FROM articles''').fetchall()