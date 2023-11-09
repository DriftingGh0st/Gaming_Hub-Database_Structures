import mysql.connector

# connecting to local database
connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Pb26460329",
    database = "report2"
)

cursor = connection.cursor()

def display_product_category(selected_category):
    # Simulate displaying a list of products in a specific category
    query = "SELECT productID, productName, categoryName, price, specs FROM Product WHERE categoryNAME = %s"
    cursor.execute(query, (selected_category,))
    products = cursor.fetchall()

    print(f'Products in the {selected_category} category:')
    for product in products:
        print(f"Product ID: {product[0]}, Name: {product[1]}, Category: {product [2]}, Price: ${product[3]}")

    return products

def change_keybaord_color(product_id):
    # Simulate changing the color of a keyboard
    print("Do you want to change the keyboard color? (yes/no)")
    user_choice = input().lower()

    if user_choice == "yes":
        print("Available colors:")
        print("1. White")
        print("2. Black")
        print("3. Red")
        print("4. Blue")
        color_choice = input("Enter the number of your preferred color: ")

        available_colors = ["White", "Black", "Red", "Blue"]
        try:
            color_number = input("Enter the number of your preferred color: ")
            if 1 <= color_number <= len(available_colors):
                new_color = available_colors[color_number - 1]
                query = "UPDATE Product SET specs = CONCAT('Type: Full Keyboard, Color: ', %s) WHERE productID = %s"
                cursor.execute(query, (new_color, product_id))
                connection.commit()
                print("Color changed successfully.")
                return new_color # Return the new color
            else:
                print("Invalid color choice.")
        except ValueError:
            print("Invalid input.")
    elif user_choice == "no":
        print("No changes made.")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    selected_category = "Keyboards" # Replace with the desired category
    products = display_product_category(selected_category)

    user_choice = input("Enter the product ID you want to view or change specifications for: ")
    try:
        product_id = int(user_choice)
        selected_product = [product for product in products if product [0] == product_id]
        if selected_product:
            selected_product = selected_product[0]
            print(f"Product Specifications:\n{selected_product[4]}")

            if selected_product[2] == "Keyboards":
                new_color = change_keybaord_color(product_id)
                if new_color:
                    selected_product = list(selected_product) # convert the tuple to a list ot modify it
                    selected_product[4] = f'Type: Full Keyboard, Color: {new_color}' # Update the color in the list
                    print("Updated Product Entry:")
                    print(f"Product ID: {selected_product[0]}, Name: {selected_product[1]}, Category {selected_category[2]}, Price: ${selected_product[3]}")
                    print(f"Product Specifications:\n{selected_product[4]}")
            else:
                print("Product not found.")
    except ValueError:
        print("Invalid product ID. Please enter a valid product ID.")

cursor.close()
connection.close()