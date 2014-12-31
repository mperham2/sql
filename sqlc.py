# the executemany() method

import sqlite3

# create a new databse if the database doesn't already exist
with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	# insert multiple records using a tuple
	cities = [
			('Boston', 'MA', 600000),
			('Chicago', 'IL', 27000000),
			('Houston', 'TX', 2100000),
			('Phoenix', 'AZ', 1500000)
			]

	# insert data into table
	c.executemany('INSERT INTO population VALUES (?,?,?)', cities)

