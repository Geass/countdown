from flask import Flask, render_template
from datetime import datetime
import time

app = Flask(__name__)

@app.route('/')
def index():
    target_date = datetime(2023, 8, 5)
    now = datetime.now()
    countdown = target_date - now
    days = countdown.days
    hours, remainder = divmod(countdown.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return render_template('index.html', days=days, hours=hours, minutes=minutes, seconds=seconds)

if __name__ == '__main__':
    app.run()
