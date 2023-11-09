import mysql.connector

# connecting to local database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pb26460329",
    database="report2"
)

cursor = connection.cursor()


def fetch_all_products():
    # Query to select all product information
    query = "SELECT productID, productName, categoryName, price, specs FROM Product "
    cursor.execute(query)
    products = cursor.fetchall()
    return products


def display_unique_categories(products):
    unique_categories = {product[2] for product in products}  # Use a set to store unique category names

    print("Available categories:")
    for category in unique_categories:
        print(f"Category: {category}")

    return products

def display_products_in_category(category_name, products):
    print(f"\nDisplaying products in the '{category_name}' category:")
    category_products = [product for product in products if product[2] == category_name]
    for product in category_products:
        print(f"Product ID: {product[0]}, Name: {product[1]}, Price: ${product[3]}, Specs: {product[4]}")

def product_stock_status(product_id):
    query = "SELECT quantity, statusID FROM Inventory WHERE productID = %s"
    cursor.execute(query, (product_id,))
    inventory_info = cursor.fetchall()

    # Check if the product is out of stock
    if inventory_info:
        quantity, statusID = inventory_info[0]  # Unpack the tuple
        if quantity > 0:
            print(f"Product ID {product_id} is in stock with quantity {quantity}.")
            return True
        else:
            print(f"Product ID {product_id} is out of stock.")
            return False
    else:
        print(f"No inventory record found for Product ID {product_id}.")
        return False


if __name__ == "__main__":
    products = fetch_all_products()
    display_unique_categories(products)

    selected_category = "Mice"
    display_products_in_category(selected_category, products)
    user_selects_mouse = input(f"\nEnter the product ID of the {selected_category} you would like to purchase: ")
    try:
        product_stock_status(int(user_selects_mouse))  # Convert to int before passing
    except ValueError:
        print("Invalid input. Please enter a numerical Product ID.")
    cursor.close()
    connection.close()

