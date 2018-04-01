from flask import Flask, render_template

app = Flask(__name__)
app.debug = True


@app.route('/')
def main():
    return render_template('another_inner/main.html')


@app.route('/about/')
def about():
    return render_template('inner/article_2.html')


# app.run()
from scipy import constants
print(100 * 1e9 * 1.6e-19 , constants.m_e * constants.c**2)
