from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///properties.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
app.config['UPLOAD_FOLDER'] = 'uploads'  
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}  
db = SQLAlchemy(app)

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(200), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    salesdate = db.Column(db.String(50), nullable=True)
    subtitle = db.Column(db.String(200), nullable=True)
    salestype = db.Column(db.String(50), nullable=True)
    property_detail = db.Column(db.Text, nullable=True)
    description = db.Column(db.Text, nullable=True) 
    price_range_low = db.Column(db.Integer, nullable=True)
    price_range_medium = db.Column(db.Integer, nullable=True)
    price_range_high = db.Column(db.Integer, nullable=True)
    capital_value = db.Column(db.Integer, nullable=True)
    agent_name = db.Column(db.String(100), nullable=True)
    agent_email = db.Column(db.String(100), nullable=True)
    agent_phone = db.Column(db.String(50), nullable=True)
    photo_path = db.Column(db.String(255))

with app.app_context():
    db.create_all()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/findagent')
def findagent():
    return render_template('findagent.html')

@app.route('/agentsearch')
def agentsearch():
    return render_template('agentsearch.html')

@app.route('/homeinspiration')
def homeinspiration():
    return render_template('homeinspiration.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/favorite')
def favorite():
    return render_template('favorite.html')

@app.route('/myhome')
def myhome():
    return render_template('myhome.html')

@app.route('/propertyupload')
def upload_form():
    return render_template('propertyupload.html')

# Route for the form page
@app.route('/')
def form():
    return render_template('propertyupload.html')

# Route to handle form submission
@app.route('/submit', methods=['GET', 'POST'])
def submit_property():
    if request.method == 'POST':
        location = request.form['location']
        title = request.form['title']
        salesdate = datetime.strptime(request.form['salesdate'], '%Y-%m-%d').date() if request.form['salesdate'] else None
        subtitle = request.form['subtitle']
        salestype = request.form['salestype']
        property_detail = request.form['propertydetail']
        description = request.form['description']
        pricerange_low = request.form['pricerange-low']
        pricerange_medium = request.form['pricerange-medium']
        pricerange_high = request.form['pricerange-high']
        capital_value = request.form['capitalvalue']
        agent_name = request.form['agent-name']
        agent_email = request.form['agent-email']
        agent_phone = request.form['agent-phone']

       
        if 'photo' in request.files:
            photo = request.files['photo']
            if photo.filename == '':
                photo_path = None
            elif photo and allowed_file(photo.filename):
                filename = secure_filename(photo.filename)
                photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                photo_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            else:
                photo_path = None
        else:
            photo_path = None

        
        new_property = Property(location=location, title=title, sales_date=salesdate,
                                subtitle=subtitle, sales_type=salestype, property_detail=property_detail,
                                description=description, price_low=pricerange_low, price_medium=pricerange_medium,
                                price_high=pricerange_high, capital_value=capital_value, agent_name=agent_name,
                                agent_email=agent_email, agent_phone=agent_phone, photo_path=photo_path)
        
        db.session.add(new_property)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('submit.html')

if __name__ == '__main__':
    app.run(debug=True)