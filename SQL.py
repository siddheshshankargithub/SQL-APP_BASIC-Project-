""" NOTE: Please uncomment the code commented one by one for perfectly running code without overwriting the table. 
"""
""" To import sqlite3
"""
import sqlite3

""" We need a connection to the database after we import 
sqlite3.
"""
conn = sqlite3.connect('customer.db')

"""If we want to store a small data on which operate, we can do:
NOTE: This will allow to create a database that is live on till we 
are in the program. It will make create a database in the memory.
"""
#conn = sqlite3.connect(':memory:')

""" To create a table in the database just created.
Whenever we query a database we are actually querying 
a table inside the database.
"""
""" So we have to use a cursor to query a database.
"""
c = conn.cursor()

# DOCSTRING APPROACH

'''c.execute("CREATE TABLE customers (first_name DATATYPE,last_name DATATYPE,email DATATYPE)")
'''
'''many_customers = [
   ('Wes','Brown','We@brown.com'),
    ('Steph','Keas','Step@keas.com'),
    ('Adwait','Joshi','Ad@xyz.com')]

c.executemany("INSERT INTO customers VALUES (?,?,?)",many_customers)
'''

""" QUERY THE DATABASE. 
"""
'''
c.execute("SELECT * FROM customers") 
#c.fetchone()
#c.fetchmany(3)
print(c.fetchall())
'''

""" To loop through the table to display items in a good format.
"""
'''
c.execute("SELECT * FROM customers")
items = c.fetchall()
print("NAME: " + "\t\tEMAIL: ")
print("------" + "\t\t-------")
for item in items:
	print(item[0] + " " + item[1] + "\t " + item[2])  # to get the first names.
'''

"""PRIMARY KEY ID(BACKGROUND ROW ID).
"""
'''
c.execute("SELECT rowid, * FROM customers")
items = c.fetchall()
for item in items:
	print(item)
'''

""" WHERE CLAUSE. 
"""
'''
c.execute("SELECT * FROM customers WHERE last_name LIKE  'sh%'")
items = c.fetchall()
for item in items:
	print(item)
'''

""" UPDATING OUR DATABASE.
"""
'''
c.execute("""UPDATE customers SET first_name = 'John'
			WHERE rowid = 1
	""")

c.execute("SELECT rowid, * FROM customers")
items = c.fetchall()
for item in items:
	print(item)
'''

""" DELETE A RECORD IN THE DATABASE.
"""
'''
c.execute("""DELETE from customers WHERE first_name = 'Siddhesh'
	""")

c.execute("SELECT * FROM customers")
items = c.fetchall()
for item in items:
	print(item)
'''

""" ORDERING
"""
'''
c.execute("SELECT * FROM customers ORDER BY last_name") # By default it is in ascending.
items = c.fetchall()
for item in items:
	print(item)
'''

""" AND / OR
"""
'''
c.execute("SELECT * FROM customers WHERE last_name LIKE 'Br%' OR rowid = 4") # We can use AND instead of OR but make sure that rowid is correct when we use AND
items = c.fetchall()
for item in items:
	print(item)
'''

""" LIMITING RESULTS
"""
'''
c.execute("SELECT rowid, * FROM customers LIMIT 2") 
items = c.fetchall()
for item in items:
	print(item)
'''

""" DELETE A TABLE 
"""
'''
c.execute("DROP TABLE customers")
c.execute("SELECT rowid, * FROM customers") 
items = c.fetchall()
for item in items:
	print(item)
'''

""" AN APP 
"""
# QUERYING THE DATABASE AND RETURNING ALL THE ITEMS FUNCTION
def show_all():
	conn = sqlite3.connect('customer.db')
	c = conn.cursor()
	c.execute("SELECT * FROM customers") 
	items = c.fetchall()
	for item in items:
		print(item)
	conn.commit()	
	conn.close()

# ADD A RECORD TO THE DATABASE

def add_one(first,last,email):
	conn = sqlite3.connect('customer.db')
	c = conn.cursor()
	c.execute("INSERT INTO customers VALUES (?,?,?)",(first , last, email))
	conn.commit()	
	conn.close()
# DELETE A RECORD FROM THE TABLE
def delete_one(id):
	conn = sqlite3.connect('customer.db')
	c = conn.cursor()	
	c.execute("DELETE from customers WHERE rowid = (?)", id)
	conn.commit()	
	conn.close()

# ADD MANY RECORDS FROM THE TABLE
def add_many(list):
	conn = sqlite3.connect('customer.db')
	c = conn.cursor()	
	c.executemany("INSERT INTO customers VALUES (?,?,?)", (list))
	conn.commit()	
	conn.close()

# WHERE CLAUSE FUNCTION
def email_lookup(email):
	conn = sqlite3.connect('customer.db')
	c = conn.cursor()	
	c.execute("SELECT * from customers WHERE email = (?)", (email,))
	items = c.fetchall()
	for item in items:
		print(item)
	conn.commit()	
	conn.close()

#conn.commit()	
#conn.close()


