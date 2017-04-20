import os
from flask import Flask, flash, render_template, request, redirect, url_for, session
application = Flask(__name__, static_url_path='')



@application.route('/')
def index():
    if 'logged_in' in session:
        return render_template('index.html')
    else:
        return redirect('/login')


@application.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        passw = request.form['password']
        if valid_login(passw):
            session['logged_in'] = True
            return redirect(url_for('index'))

        else:
            flash('invalid')
            return redirect(url_for('login'))
    else:
        return render_template('login.html')


@application.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in')
        return redirect(url_for('login'))

def valid_login(passw):
    if passw == 'starboy':
        return True
    return False


application.secret_key = 'qhgioew324oghewoqui256hg272owqegq'

if __name__ == '__main__':
    application.debug = True
    application.run()
