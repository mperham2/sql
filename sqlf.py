# SELECT statement

import sqlite3

with sqlite3.connect("new2.db") as connection:
	c = connection.cursor()



	# use a for loop to iterate through the database results line by line
	c.execute("SELECT firstname, lastname from employees")

	rows = c.fetchall()

	for r in rows:
		print r[0], r[1]