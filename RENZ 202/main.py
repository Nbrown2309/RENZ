from flask import Flask, render_template

app = Flask(__name__)

#Including The Following pages

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/property/<int:property_id>')
def property(property_id):
    property_details = {
        'id': property_id,
        'title': 'Sample Property',
        'description': 'This is a sample property description.',
        'price': '500,000',
        'address': '123 Main St, Auckland',
        'images': ['property1.jpg', 'property2.jpg'],
        'features': ['3 Bedrooms', '2 Bathrooms', '1 Garage'],
        'agent': 'John Doe'
    }

    return render_template('property.html', property=property_details)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)


