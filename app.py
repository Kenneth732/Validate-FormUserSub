from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = '86987815d884ef414253fac91dd187339165a9500f25d1d5'


courses_list = [{
    'title': 'Python 101',
    'description': 'Learn Python basics',
    'price': 34,
    'available': True,
    'level': 'Beginner'
    }]

@app.route('/', methods=('GET', 'POST'))
def index():
    form = CourseForm()
    return render_template('index.html', form=form)