import pandas as pd
import sqlite3

# reading data from csv file
df = pd.read_csv('dataset.csv')
# print(df)

# checking for null values
# print(df.isnull().sum())

# removing columns having null values
df.dropna(axis=1, inplace=True)

# only keeping the below columns in the dataset
cols = ['id', 'first_name', 'last_name', 'date_of_birth', 'ethnicity', 'gender', 'email']

df = df[cols]
print(df)

# creating a connection to sqlite db
conn = sqlite3.connect('students.db')
cur = conn.cursor()

# creating STUDENTS table using sqlite
# cur.execute('CREATE TABLE STUDENTS(ID INTEGER, FIRST_NAME TEXT, LAST_NAME TEXT, DATE_OF_BIRTH TEXT, ETHNICITY TEXT, GENDER TEXT, EMAIL TEXT)')

# insert all values in the dataframe into the table
for row in df.itertuples():
    cur.execute('INSERT INTO STUDENTS(ID, FIRST_NAME, LAST_NAME, DATE_OF_BIRTH, ETHNICITY, GENDER, EMAIL) VALUES(?, ?, ?, ?, ?, ?, ?)', (row.id, row.first_name, row.last_name, row.date_of_birth, row.ethnicity, row.gender, row.email))

# commiting the changes to the db
conn.commit()

# viewing the data stored in STUDENTS table
cur.execute('SELECT * FROM STUDENTS')

students = cur.fetchall()

for student in students:
    print(student)

conn.close()

