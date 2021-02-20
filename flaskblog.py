from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY']='e79e27c3bb345bd8965a34eda10a853e'

#generate random key using secret module
# import secrets
# secrets.token_hex(16) => 16 = 16 bytes

posts = [
    {
        'author':'Dragon Warrior',
        'title':'How you doing',
        'content':'First blog',
        'date_posted':'Feb 19, 2021'
    },
    {
        'author':'Axel Blaze',
        'title':'How you doing',
        'content':'Second blog',
        'date_posted':'Feb 20, 2021'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=posts)

@app.route('/about')
def about():
    return render_template('about.html',title="About")

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!',category='success')
        return redirect(url_for('home'))
    return render_template('registration.html', title='Register',form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data =='ravi@gmail.com' and form.password.data=='ravi':
            flash('You have been logged in!','success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password','danger')
    return render_template('login.html', title='Login',form=form)

if __name__=='__main__':
    app.run(debug=True)