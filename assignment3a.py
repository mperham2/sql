# assignment3a.py

# need libraries to generate random integers and work with database
import random
import sqlite3

# generate a list of random numbers
numlist = []
for i in range(0,100):
    numlist.append([random.randint(1,100)])

print numlist
# open a connection to a new database
with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

# create a new table
    c.execute("""CREATE TABLE numbers (num INTEGER)""")

# add the list of random numbers to the table
    c.executemany("INSERT INTO numbers(num) values (?)", numlist)
