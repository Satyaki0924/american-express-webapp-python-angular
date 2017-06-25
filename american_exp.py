"""
This is a project by Satyaki Sanyal.
This project must be used for educational purposes only.
Follow me on:
LinkedIn - https://www.linkedin.com/in/satyaki-sanyal-708424b7/
Github - https://github.com/Satyaki0924/
Researchgate - https://www.researchgate.net/profile/Satyaki_Sanyal
"""
import bcrypt
from flask import Flask, render_template, request, flash, session, redirect, url_for
from flask.ext.pymongo import PyMongo
from matplotlib import style
from wtforms import Form, TextField, validators, PasswordField

style.use('ggplot')

from collect_info import Collect

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'american_express'
app.config['MONGO_URI'] = 'mongodb://admin:adminsatyaki@ds135532.mlab.com:35532/american_express'
app.config.from_object(__name__)
mongo = PyMongo(app)


class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    email = TextField('Email:', validators=[validators.required(), validators.Length(min=6, max=35)])
    password = PasswordField('Password:', validators=[validators.required(), validators.Length(min=3, max=35)])


class LoginForm(Form):
    email = TextField('Email:', validators=[validators.required(), validators.Length(min=6, max=35)])
    password = PasswordField('Password:', validators=[validators.required(), validators.Length(min=3, max=35)])


@app.route('/')
def index():
    if 'unique' in session:
        df = Collect.pass_dataframe()
        return render_template('index.html', df=df)
    else:
        return redirect(url_for('register'))


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'unique' in session:
        return redirect(url_for('index'))
    else:
        form = LoginForm(request.form)
        if request.method == 'POST' and form.validate():
            users = mongo.db.users
            password = form.password.data
            email = form.email.data
            login_user = users.find_one({'email': email})

            if login_user:
                if bcrypt.hashpw(password.encode('utf-8'), login_user['password']) == \
                        login_user['password']:
                    session['unique'] = email
                    return redirect(url_for('index'))
            flash("Error: Email doesn't exists or password incorrect")

    return render_template('login.html', form=form)


@app.route('/chart', methods=['GET', 'POST'])
def chart():
    id = request.args.get('id')
    gr = request.args.get('gr')
    if not id:
        id = 1
    if not gr:
        gr = 0

    labels = ["April", "May", "June", "July", "August", "September"]
    if int(gr) == 0:
        name, values = Collect.collect_payment(int(id))
        g = 'Bill'
    else:
        name, values = Collect.collect_payment2(int(id))
        g = 'Previous payment'

    print(gr, g)

    return render_template('chart.html', values=values, labels=labels, name=name, maximum=max(values), g=g)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'unique' in session:
        return redirect(url_for('index'))
    else:
        form = ReusableForm(request.form)
        users = mongo.db.users

        if request.method == 'POST' and form.validate():
            name = form.name.data
            password = form.password.data
            email = form.email.data
            existing_user = users.find_one({'email': email})
            if existing_user is None:
                hashpass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                users.insert({'name': name, 'password': hashpass, 'email': email})
                print(email)
                session['unique'] = email
                flash('Thanks for registration ' + name)
                return redirect(url_for('index'))

            else:
                flash('Error: ' + email + ' is already registered!')

        return render_template('register.html', form=form)


if __name__ == '__main__':
    app.secret_key = '7d441f27d441f27567d441f2b6176a'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)
