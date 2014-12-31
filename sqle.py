# Create a SQLite3 database and table

# import the sqlite3 library
import sqlite3

conn = sqlite3.connect("new.db")
cursor = conn.cursor()
# with sqlite3.connect("new.db") as connection:
	# c = connection.cursor()
	# c.execute("INSERT INTO population VALUES('New Jack City', \
	# 	'NY', 8200000)")
	# c.execute("INSERT INTO population VALUES('San Franwierdo', \
	# 	'CA', 800000)")

# create a new databse if the database doesn't already exist
conn = sqlite3.connect("new.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

try:
	cursor.execute("INSERT INTO populations VALUES('New York City', \
		'NY', 8200000)")
	cursor.execute("INSERT INTO populations VALUES('San Francisco', \
		'CA', 800000)")

	conn.commit()
except sqlite3.OperationalError:
	print "Oops! Something went wrong. Try again..."


# cloase the database connection
conn.close()