from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(80), nullable=False)


    def __repr__(self):
        return f"<User {self.email}>"

def init_db():
    with app.app_context():
        db.create_all()

@app.route('/')
def home():
    return render_template('login_and_signup.html')

@app.route('/api/login', methods=['POST'])
def log_in():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):
        return jsonify(success=True)
    return jsonify(success=False, message='Invalid credentials')

@app.route('/api/signup', methods=['POST'])
def sign_up():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    name = data.get('name')

    if User.query.filter_by(email=email).first():
        return jsonify(success=False, message='Email already registered')

    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
    new_user = User(email=email, password=hashed_password, name=name)
    db.session.add(new_user)
    db.session.commit()
    return jsonify(success=True, message='Signup successful!')

if __name__ == '__main__':
    init_db() 
    app.run(debug=True, port=5001)