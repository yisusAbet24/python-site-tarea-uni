from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('site/index.html')

@app.route('/menu')
def menu():
    return render_template('site/menu.html')

@app.route('/about')    
def about():
    return render_template('site/about.html')

@app.route('/contact')
def contact():
    return render_template('site/contact.html')

@app.route('/location')
def location():
    return render_template('site/location.html')



if __name__ == '__main__':
    app.run(debug=True, port=8000)