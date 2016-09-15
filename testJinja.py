from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime as dt

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)



@app.route("/")
def index():
    return render_template('template.html', my_list=[0,1,2,3,4,5,6,7,8,9,10], name="vamsi")


@app.route("/carousel")
def myCarousel():
    return render_template('carousel.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/dt')
def datetime():
    return render_template('index.html', current_time=dt.utcnow())

if __name__ == "__main__":
    app.run(debug=True)



