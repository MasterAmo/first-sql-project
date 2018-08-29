# import the SQLite3 library
import sqlite3

# # create a new database if the database doesn't already exist
# conn = sqlite3.connect("new.db")

# # get a cursor object used to execute SQL commands
# cursor = conn.cursor()

# # create a table
# cursor.execute("INSERT INTO population VALUES('New York City', 'NY',840000) ")
# cursor.execute("INSERT INTO population VALUES('San Francisco', 'CA',800000) ")


# # commit the changes
# conn.commit()

# Here a more compact code than the code above so we dont need to use the commit() method


with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    c.execute("INSERT INTO population VALUES('New York City', 'NY', 840000) ")
    c.execute("INSERT INTO population VALUES('San Francisco', 'CA', 800000) ")
    c.execute("INSERT INTO population VALUES('Boston', 'MA', 600000) ")

# close the db connection
connection.close()
