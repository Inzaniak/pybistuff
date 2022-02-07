import sqlite3
import pandas as pd
import json

# CREATE AND CONNECT TO DB
conn = sqlite3.connect('./data/test.db')
inmem_conn = sqlite3.connect(':memory:')

# READ DATA FROM CSV
rows = []
df = pd.read_csv('./data/Highest Holywood Grossing Movies.csv')
df.rename(columns={'Unnamed: 0': 'movieID'},inplace=True)

# CREATE GENRES DATAFRAME
genres = df[['movieID','Genre']]
genres['Genre'] = genres['Genre'].astype(str)
genres['Genre'] = genres['Genre'].apply(lambda x: json.loads(x.replace("'", '"')))
genres = genres.explode('Genre')

#CREATE MAIN DATAFRAME
main = df.drop(['Genre'], axis=1)
    
# CREATE movies TABLE
try:
    conn.execute('''DROP TABLE movies''')
    conn.commit()
except:
    pass
conn.execute('''
    CREATE TABLE movies (
        idMovie INTEGER PRIMARY KEY,
        Title TEXT,
        MovieInfo TEXT,
        Distributor TEXT,
        ReleaseDate TEXT,
        DomesticSales INTEGER,
        InternationalSales INTEGER,
        WorldSales INTEGER,
        MovieRuntime TEXT,
        License TEXT
    )'''
)
conn.commit()


# INSERT ROWS INTO TABLE
rows = main.values.tolist()
conn.executemany('INSERT INTO movies VALUES (?,?,?,?,?,?,?,?,?,?)', rows)
conn.commit()

# CHECK IF ROWS INSERTED CORRECTLY
check = conn.execute('SELECT * FROM movies LIMIT 10').fetchall()
print(check[0])

# CREATE genres TABLE
try:
    conn.execute('''DROP TABLE genres''')
    conn.commit()
except:
    pass
conn.execute('''CREATE TABLE genres (
    idMovie INTEGER,
    Genre TEXT
)''')
conn.commit()

# POPULATE GENRES TABLE
rows = genres.values.tolist()
conn.executemany('INSERT INTO genres VALUES (?,?)', rows)
conn.commit()

# COMPLEX QUERY
cquery = conn.execute("""
    SELECT 
        movies.idMovie
        ,movies.Title
        ,movies.DomesticSales
    FROM movies
    INNER JOIN genres
    ON movies.idMovie = genres.idMovie
    WHERE genres.Genre = 'Action'
    ORDER BY DomesticSales DESC
    LIMIT 10"""
    ).fetchall()

conn.close()