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
    inventory_info = cursor.fetchone()  # Fetches the first record or None

    if inventory_info:
        quantity, statusID = inventory_info
        if quantity > 0:
            print(f"Product ID {product_id} is in stock with quantity {quantity}.")
            return inventory_info  # Return the inventory information including the quantity
        else:
            print(f"Product ID {product_id} is out of stock.")
            return None  # Return None to indicate no stock
    else:
        print(f"No inventory record found for Product ID {product_id}.")
        return None  # Return None to indicate no record found

def product_added(product_id, amount):
    inventory_info = product_stock_status(product_id)
    if inventory_info and inventory_info[0] >= amount:
        current_quantity = inventory_info[0]
        new_quantity = current_quantity - amount
        update_query = "UPDATE Inventory SET quantity = %s WHERE productID = %s"
        cursor.execute(update_query, (new_quantity, product_id))
        connection.commit()
        print(f"Quantity updated. Product ID {product_id} now has {new_quantity} items in stock.")
    elif inventory_info and inventory_info[0] < amount:
        print(f"Not enough stock for Product ID {product_id}. Current stock is {inventory_info[0]}.")
    else:
        print(f"No inventory record found for Product ID {product_id}.")


if __name__ == "__main__":
    continue_shopping = True

    while continue_shopping:
        products = fetch_all_products()
        display_unique_categories(products)

        selected_category = input("Enter the name of the category you would like to purchase from: ")
        display_products_in_category(selected_category, products)

        product_id_to_purchase = input(
            f"\nEnter the product ID of the {selected_category} you would like to purchase: ")

        try:
            product_id_to_purchase = int(product_id_to_purchase)
            while True:  # This will allow us to re-prompt for the quantity if necessary
                quantity_to_purchase = int(input("Enter the quantity you would like to purchase: "))

                if quantity_to_purchase <= 0:
                    print("Please enter a positive number for the quantity.")
                    continue

                # Check if enough stock is available
                inventory_info = product_stock_status(product_id_to_purchase)
                if inventory_info is not None:
                    current_stock = inventory_info[0]
                    if current_stock >= quantity_to_purchase:
                        product_added(product_id_to_purchase, quantity_to_purchase)
                        break
                    else:
                        print(f"Not enough stock. Only {current_stock} left in stock.")
                        retry = input("Would you like to try a lower quantity? (yes/no): ").lower()
                        if retry != 'yes':
                            break  # Exit the quantity prompt loop if user does not want to retry

            # Ask the user if they want to continue shopping
            user_choice = input("Would you like to add more items to your purchase? (yes/no): ").lower()
            if user_choice != 'yes':
                continue_shopping = False

        except ValueError:
            print("Invalid input. Please enter a numerical value for both Product ID and quantity.")

    cursor.close()
    connection.close()