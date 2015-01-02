# assignment3b.py

# import libraries for interacting with a database
import sqlite3

choice = 1
while choice != 5:
    # prompt the user with five options: AVG, MAX, MIN, SUM, or exit
    choice = raw_input("Please choose an option by number: \n\
    1) AVG \n\
    2) MAX \n\
    3) MIN \n\
    4) SUM \n\
    5) EXIT: ")

    # Exit option
    if choice == '1' or choice == '2' or choice == '3' or choice == '4':
        # open a connection to the database
        with sqlite3.connect("new.db") as connection:
            c = connection.cursor()

        # create a dictionary of sql queries
            sql = {'1': "SELECT avg(num) FROM numbers",
                    '2': "SELECT max(num) FROM numbers",
                    '3': "SELECT min(num) FROM numbers",
                    '4': "SELECT sum(num) FROM numbers"}

        # request a result from the table with one of the four options
            c.execute(sql[choice])

        # report out the result
            result = c.fetchone()

            print choice + ": %s" % result[0]
    else:
        break
