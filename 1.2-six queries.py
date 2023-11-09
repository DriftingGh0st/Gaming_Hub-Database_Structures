import mysql.connector

# connecting to local database
connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Pb26460329",
    database = "report2"
)

# creating cursor
cursor = connection.cursor()

# First SQL query
cursor.execute('Select * FROM product WHERE price < 150')
print('All rows from table Product where the Price is less than 150:')
for data in cursor:
    print(data)

# Second SQL query
cursor.execute('SELECT c.username, o.orderID FROM Customer c JOIN Orders o ON c.accountID = o.accountID')
print('\nDisplaying which order belongs to which account.customer:')
for data in cursor:
    print(data)

# Third SQL query
cursor.execute('Update Inventory SET statusID = \'Out of Stock\', quantity = 0 WHERE inventoryID = 101')
cursor.execute('SELECT inventoryID, statusID, quantity FROM inventory WHERE statusID = \'Out of Stock\'')
print('\nChanging the status of a product to "Out of Stock" and setting its Quantity 0:')
for data in cursor:
    print(data)

# Fourth SQL query
cursor.execute('SELECT c.username, SUM(o.totalAmount) AS total_order_value FROM Customer c JOIN Orders o ON c.accountID '
               '= o.accountID GROUP BY c.username;')
print('\nFinding the total order value for each customer:')
for data in cursor:
    print(data)

# Fifth SQL query
cursor.execute('SELECT categoryName FROM Category WHERE categoryName IN (SELECT categoryName FROM Product WHERE price > 150);')
print('\nDisplaying categories that have products priced over $150:')
for data in cursor:
    print(data)

# Sixth SQL query
cursor.execute('SELECT username FROM Customer c WHERE EXISTS (SELECT 1 FROM Orders o WHERE o.accountID = c.accountID);')
print('\nDisplaying customers who have place at least one order based on the Orders table:')
for data in cursor:
    print(data)

# Closing the cursor and the database connection
cursor.close()
connection.close()