from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    page_title = 'Главная страница'
    return render_template('index.html', title=page_title)


if __name__ == '__main__':
    app.run(debug=True)
    app.add_url_rule('/img/<path:filename>')