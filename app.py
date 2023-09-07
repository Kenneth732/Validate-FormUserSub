

from flask import Flask, render_template, redirect, url_for
from forms import CourseForm
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
    if form.validate_on_submit():
        courses_list.append({
            'title' : form.title.data,
            'description': form.description.data,
            'available' : form.available.data,
            'level' : form.level.data
        })
        return redirect(url_for('courses'))
    return render_template('index.html', form=form)
