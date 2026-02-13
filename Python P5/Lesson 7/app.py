from flask import Flask, render_template, request, flash, redirect, session, url_for, make_response 
from hashlib import sha256
import re, json

app = Flask(__name__)
app.secret_key = 'Public_Key'

@app.route("/home")
def toHome():
    title = 'Home'
    with open("data.json", "r") as f:
        data = json.load(f)
        print(session)
    return render_template('home.html', name="abc", title=title)

@app.route("/createBlog")
def createBlog():
    title = 'Create New Blog'
    return render_template('createBlog.html', name="abc", title=title)

@app.route("/register")
def toSignUp():
    title = 'Register'
    return render_template('register.html', name="abc", title=title)

@app.route("/login")
def login():
    title = 'Login'
    username = request.cookies.get('username')
    password = request.cookies.get('password')
    return render_template('login.html', name="abc", username=username, password=password, title=title)

@app.route("/logout")
def logout():
    session.pop("username")
    return redirect(url_for("toHome"))


@app.route("/loginValidate", methods=['POST'])
def loginValidate():
    f = open('data.json')
    data = json.load(f)
    f.close
    username = request.form['username']
    password = request.form['password']
    password = sha256(password.encode('utf-8')).hexdigest()
    if username not in data["data"]:
        flash('Invalid Username')
        return redirect(url_for("login"))
    if data["data"][username]["password"] == password:
        session["username"] = username
        return redirect(url_for("toHome"))
    else:
        flash('Invalid Password')
        return redirect(url_for("login"))


@app.route("/validate", methods=['POST'])
def validate():
    resp = make_response(redirect(url_for("toHome")))
    username = request.form['username']
    password = request.form['password']
    rememberMe = 'remember' in request.form
    flag = 0
    f = open('data.json')    
    data = json.load(f)
    while True:
        if username in data["data"]:
            flag = -2
            break
        if (len(password)<=4):
            flag = -1
            break
        elif not re.search("[a-z]", password):
            flag = -1
            break
        elif not re.search("[A-Z]", password):
            flag = -1
            break
        elif not re.search("[0-9]", password):
            flag = -1
            break
        else:
            flag = 0
            if rememberMe == True:
                resp.set_cookie('username', username)
                resp.set_cookie('password', password)
                with open("data.json", "r") as f:
                    data1 = json.load(f)
                password = sha256(password.encode('utf-8')).hexdigest()
                data1["data"][username] = {"password":password}
                with open('data.json', 'w') as f:
                    json.dump(data1, f, indent=4)
                session["username"] = username
                return resp
    if flag == -1:
        flash('Invalid Password')
        return redirect(url_for("toSignUp"))
    if flag == -2:
        flash('Username already exist')
        return redirect(url_for("toSignUp"))

if __name__ == "__main__":
    app.run(debug=True)