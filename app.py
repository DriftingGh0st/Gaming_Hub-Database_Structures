from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    categories = [
        'Keyboards', 'Mice', 'Laptops', 'Headphones'
    ]
    return render_template('index.html', categories=categories)

@app.route('/<category>')
def category_page(category):
    # Replace spaces with underscores and convert to lowercase for template filenames
    template_name = category.replace(" ", "_").lower() + '.html'
    return render_template(template_name)




if __name__ == '__main__':
    app.run(debug=True)


