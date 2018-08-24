import markovify
import requests_html
import sqlite3
import sys
import getopt

conn = sqlite3.connect('data/db.db')

def create_sql_table():
    try:
        conn.execute('CREATE TABLE `Articles` ( `ArticleName` TEXT, `ArticleText` TEXT, PRIMARY KEY(`ArticleName`) )')
    except sqlite3.OperationalError:
        print('Table already in DB')

def get_pages(num_pages=10):
    sess = requests_html.HTMLSession()
    for i in range(0,num_pages):
        print('Page:',i)
        res = sess.get("https://en.wikipedia.org/wiki/Special:Random")
        title = res.html.find('.firstHeading')[0].text
        text = ' '.join([p.text for p in res.html.find('p') if len(p.text) > 30])
        try:
            conn.execute('INSERT INTO Articles VALUES (?,?)'
                            ,(
                                title
                                ,text
                            )
                        )
            conn.commit()
        except sqlite3.IntegrityError:
            print('Riga già presente')

def generate_markov(num_sentences=1):
    rows = conn.execute('SELECT ArticleText FROM Articles').fetchall()
    rows = '. '.join([r[0] for r in rows])
    text_model = markovify.Text(rows)
    for i in range(0,num_sentences):
        print('-'*24)
        print(text_model.make_sentence())
        print('-'*24)

def generate_markov_long(num_sentences=1,length=140):
    rows = conn.execute('SELECT ArticleText FROM Articles').fetchall()
    rows = '. '.join([r[0] for r in rows])
    text_model = markovify.Text(rows)
    for i in range(0,num_sentences):
        sentence = text_model.make_sentence()
        if sentence == None:
            sentence = ''
        while len(sentence)<length:
            sentence = text_model.make_sentence()
            if sentence == None:
                sentence = ''
        print(sentence)

def main():
    create_sql_table()
    get_pages(10)
    generate_markov(10)
    # generate_markov_long(1,length=400)

if __name__ == '__main__':
    if sys.argv[-1] == '-nodown':
        generate_markov(1)
        generate_markov_long(1,length=400)
    else:
        main()
