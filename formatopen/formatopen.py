# TEXT #############################################
# Read entire file into a single string
text = open('examples/example.txt', 'r', encoding='utf-8').read()
print(text)
# Read example.txt line by line
lines = open('examples/example.txt', 'r', encoding='utf-8').readlines()
for num,line in enumerate(lines):
    print(num, line)


# JSON #############################################
import json
## File Loading
json_data = json.load(open('./examples/example.json'))
# Access to attribute
print(json_data['Name'])
# Access to nested attribute
print(json_data['Address'][0]['City'])
# Access to sub-dict
print(json_data['Occupation']['Job'])

## String Loading
json_data = json.loads('{"Name": "John", "Occupation": "Programmer"}')
print(json_data['Name'])


# CSV #############################################
import csv

csv_rows = []
with open('./examples/example.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        csv_rows.append(row)
# Print First Row
print(csv_rows[0])
# Print Second Row and First Column
print(csv_rows[1][0])


# HTML #############################################
from requests_html import HTML # pip install requests_html
html_str = open('./examples/example.html').read()
html = HTML(html=html_str)
# Find the Header
html.find('h1', first=True).text
# Find the paragraph
html.find('p', first=True).text


# SQLITE #############################################
import sqlite3

conn = sqlite3.connect("./examples/example.db")
# Drop table if exists
conn.execute("DROP TABLE IF EXISTS exampleData")
conn.commit()
# Create the exampleData table with columns ID, Name, Age and Job
conn.execute('''CREATE TABLE IF NOT EXISTS exampleData (
    ID INTEGER PRIMARY KEY,
    Name TEXT,
    Age INTEGER,
    Job TEXT
    )''')
conn.commit()
# Insert Data into table exampleData
conn.execute("INSERT INTO exampleData (Name, Age, Job) VALUES ('Fred', '25', 'UX Designer')")
conn.execute("INSERT INTO exampleData (Name, Age, Job) VALUES ('John', '20', 'Programmer')")
conn.commit()
# Read table exampleData
conn.execute('SELECT * FROM exampleData').fetchall()
# Delete the first row
conn.execute("DELETE FROM exampleData WHERE ID = 1")
conn.commit()