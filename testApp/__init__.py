from flask import Flask, render_template, redirect, url_for
from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired
from flask.ext.pymongo import PyMongo


class CreateForm(Form):
    task = StringField('Task', validators=[DataRequired()])

application = Flask(__name__)
application.config.from_object('config')
mongo = PyMongo(application)


@application.route("/", methods=['GET', 'POST'])
def home():
    results = mongo.db.test.find()
    tList = []
    for i in range(results.count()):
        task = results.next()['Task']
        tList.append(task)
    form = CreateForm()
    if form.validate_on_submit():
        mongo.db.test.insert_one({'Task': form.task.data})
        return redirect(url_for('home'))
    return render_template('index.html', title='Home', form=form, tasks=tList)

if __name__ == "__main__":
    application.run(host='0.0.0.0')
