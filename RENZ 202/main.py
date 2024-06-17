from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'renz'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/findagent')
def findagent():
    return render_template('findagent.html')

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

@app.route('/detail')
def detail():
    return render_template('detail.html')

@app.route('/login_and_signup')
def login_and_signup():
    return render_template('login_and_signup.html')

@app.route('/mappopup')
def mappopup():
    return render_template('mappopup.html')

@app.route('/video')
def video():
    return render_template('video.html')

@app.route('/floorplan')
def floorplan():
    return render_template('floorplan.html')

@app.route('/solarpopup')
def solarpopup():
    return render_template('solarpopup.html')

if __name__ == '__main__':
    app.run(debug=True)
