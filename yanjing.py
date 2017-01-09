from flask import Flask, render_template
import db

app = Flask(__name__)


@app.route('/')
def hello_world():

    songs=db.getData()

    return render_template('index.html', songs=songs)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5008")
