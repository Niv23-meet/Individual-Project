from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase


config = {
  "apiKey": "AIzaSyD-suLqhR2ikGog6OiAXgVqoYouTWa5tE8",
  "authDomain": "individual-project-7e24c.firebaseapp.com",
  "projectId": "individual-project-7e24c",
  "storageBucket": "individual-project-7e24c.appspot.com",
  "messagingSenderId": "640220452831",
  "appId": "1:640220452831:web:f9dcabe78cbd0f41a4966a",
  "measurementId": "G-HWRB93R0M8",
  "databaseURL": "https://individual-project-7e24c-default-rtdb.firebaseio.com"
}


firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['srtHRHTTRHTRJtyKutueyew432436%$7%CVu'] = 'gerGREREhetHTRJyt325#V34Tv3easace'
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/index')
def home1():
    return render_template("index.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/category')
def category():
    return render_template("category.html")

@app.route('/blog')
def blog():
    return render_template("blog.html")

@app.route('/artist')
def artist():
    return render_template("artist.html")

@app.route('/playlist')
def playlist():
    return render_template("playlist.html")

@app.route('/signin', methods = ['POST', 'GET'])
def signin():
    error = ""
    if request.method == 'POST':
        email = request.form['email-signin']
        password = request.form['password-signin']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('home'))
        except:
            error = "Authentication failed"
            return render_template("signin.html")

    return render_template("signin.html")


@app.route('/signup', methods = ['POST', 'GET'])
def signup():
    error = ""
    if request.method == 'POST':
        email = request.form['email-signup']
        password = request.form['password-signup']
        name = request.form['name-signup']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            user = {"name": request.form['name-signup'], "email":request.form['email-signup'], "password": request.form["password-signup"]}
            db.child("Users").child(login_session['user']['localId']).set(user)
            return redirect(url_for('index'))
        except: 
            return render_template("signin.html")
    return render_template("signin.html")



@app.route('/forum', methods = ['POST', 'GET'])
def forum():
    comm = db.child("Comments").get().val()
    if request.method == 'POST':
        name = request.form["name"]
        content = request.form["content"]

        date = request.form["date"]
        uid = db.child("Users").child(login_session['user']['localId']).get().val()
        
        
        comment = {"name": name, "date": date, "content": content, "uid":uid}
        db.child("Comments").push(comment)
        comm = db.child("Comments").get().val()
        return render_template("forum.html", c = comm)
    
    return render_template("forum.html", c = comm)


if __name__ == '__main__':
    app.run(debug=True)