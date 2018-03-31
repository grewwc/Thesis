from flask import Flask, render_template

main: Flask = Flask(__name__)

main.debug = True

@main.route("/")
def index():
    return render_template('inner/main.html')

@main.route("/article_1.html")
def article_1():
    return render_template('another_inner/article_1.html')


@main.route("/article_2.html")
def article_2():
    return render_template('article_2.html')


if __name__ == '__main__':
    main.run()
