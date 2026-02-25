import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/story')
def story():
    return render_template('story.html')

@app.route('/docs')
def docs():
    return render_template('docs.html')

if __name__ == '__main__':
    # These two lines must have the EXACT same number of spaces (4)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
