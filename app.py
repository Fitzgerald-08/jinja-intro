import datetime 
import pytz
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    obj = datetime.datetime(2002, 10, 28, 14, 58, 33)
    standard_format = obj.strftime("%a %m %y")
    hour_extract = obj.hour

    # Format to print the time below 
    fmt = '%Y-%m-%d %H:%M:%S %Z%z'

    """
    eastern = pytz.timezone('US/Eastern')
    dtlocal = eastern.localize(datetime.datetime(2002, 7, 15, 11, 50, 48))
    ams = pytz.timezone('Europe/Amsterdam')
    ams_dt = dtlocal.astimezone(ams)

    dtlocal = dtlocal.strftime(fmt)
    """

    amsterdam = pytz.timezone('Europe/Amsterdam')

    time = datetime.datetime.now()
    utc_dt = time.astimezone(amsterdam).strftime("%d/%m/%Y - %H:%M:%S")

    return render_template('index.html', timenow=standard_format, extracted_hour=hour_extract, utc_time=utc_dt)

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/comments/')
def comments():
    comments = [
        "This is the first comment",
        "This is the second comment",
        "This is the third comment",
        "This is the fourth comment",
        "This is the fifth comment",
    ]

    return render_template('comments.html', comments=comments)