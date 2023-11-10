from flask import Flask, render_template

app = Flask(__name__)

# Define a dictionary to map category names to their respective URLs
categories_mapping = {
    'keyboards': 'Keyboards',
    'mice': 'Mice',
    'laptops': 'Laptops',
    'headphones': 'Headphones',
    'accessories': 'Accessories',
    'monitors': 'Monitors',
    'chairs': 'Chairs',
    'storage':'Storage',
    'graphics-cards':'Graphics-Cards',
    'power-supplies': 'Power-Supplies'
}

@app.route('/')
def homepage():
    # Get a list of category names from the mapping dictionary
    categories = list(categories_mapping.values())
    return render_template('index.html', categories=categories)

@app.route('/<category>')
def category_page(category):
    # Check if the requested category exists in the mapping
    if category in categories_mapping:
        category_name = categories_mapping[category]
        return render_template(f'{category}.html', categories=[category_name])
    else:
        return "Category not found", 404

if __name__ == '__main__':
    app.run(debug=True)
