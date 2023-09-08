import os
from dotenv import load_dotenv
import requests
import json
import sqlite3

# loading Google Books API Key from .env file
load_dotenv()
API_KEY = os.getenv('API_KEY')

# sending a GET request to Google Books API to fetch books using the search term - Stephen King
response = requests.get(f'https://www.googleapis.com/books/v1/volumes?q=Stephen+King&key={API_KEY}')
# taking the content of the response
r_data = response.text
# parsing the data into json format
p_data = json.loads(r_data)

# declaring four empty lists to store the ids, titles, authors and published dates from the response
ids = []
titles = []
authors = []
published_date = []

# traversing through the parsed response data to get the information we need
for item in p_data['items']:
    ids.append(item['id'])
    titles.append(item['volumeInfo']['title'])
    authors.append(item['volumeInfo']['authors'])
    published_date.append(item['volumeInfo']['publishedDate'])

# verifying whether all four lists have equal amount of elements
# print(len(ids))
# print(len(titles))
# print(len(authors))
# print(len(published_date))

# processing authors list to have text as elements and not another list
p_authors = []
for author in authors:
    p_authors.append(", ".join(author))

# print(p_authors)

# storing all the data into one list
combined_data = []

for i in range(len(ids)):
    t = (ids[i], titles[i], p_authors[i], published_date[i])
    combined_data.append(t)

# creating a connection to sqlite db
conn = sqlite3.connect('books.db')
cur = conn.cursor()

# creating BOOKS table using sqlite
# cur.execute('CREATE TABLE BOOKS(ID TEXT, TITLE TEXT, AUTHORS TEXT, PUBLISHED_DATE TEXT)')

# inserting retrieved data into the BOOKS table
# cur.executemany("INSERT INTO BOOKS(ID, TITLE, AUTHORS, PUBLISHED_DATE) VALUES(?, ?, ?, ?)", combined_data)

# conn.commit()

cur.execute('SELECT * FROM BOOKS')

books = cur.fetchall()

for book in books:
    print(book)

conn.close()