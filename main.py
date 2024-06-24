from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def ind():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return (f"<h1>Время при открытии страницы: {current_time}</h1>"
            f"<a href='/time_online'>Время онлайн</a>")

@app.route('/time_online')
@app.route('/time_online/')
def time_online():
    return render_template('time_online.html')

@app.route('/current_time')
def current_time():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return current_time

@app.route('/new/')
@app.route('/новаястраница/')
def new():
    return 'New Page'

if __name__ == '__main__':
    app.run()
