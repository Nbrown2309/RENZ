from flask import Flask, render_template, request

app = Flask(__name__)

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

@app.route('/favortie')
def favorite():
    return render_template('favorite.html')

@app.route('/myhome')
def myhome():
    return render_template('myhome.html')

@app.route('/detail')
def deatail():
    return render_template('detail.html')

if __name__ == '__main__':
    app.run(debug=True)
