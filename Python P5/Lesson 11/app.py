import os
from flask import Flask, render_template, request, flash, redirect, session, url_for, make_response 
from hashlib import sha256
import re, json

app = Flask(__name__)
app.secret_key = 'Public_Key'
UPLOAD_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower()

@app.route("/home")
def toHome():
    title = 'Home'
    with open("blog.json", "r") as f:
        data = json.load(f)["data"]
    return render_template('home.html', name="abc", title=title, data=data)

@app.route("/<route>")
def toBlog(route):
    title = 'Blog Page'
    with open("blog.json", "r") as f:
        data = json.load(f)["data"][route]
    print(data)
    return render_template('blog.html', name="abc", title=title, data=data)

@app.route('/')
def root():
    return redirect(url_for("toHome"))

@app.route("/createBlog")
def createBlog():
    title = 'Create New Blog'
    return render_template('createBlog.html', name="abc", title=title)

@app.route("/upload", methods=['POST'])
def upload():
    f = open('blog.json')
    username = request.cookies.get('username')
    title = request.form.get("Title1")
    shortDescription = request.form.get("Title2")
    catagory = request.form.get("Title3")
    picture = request.files["Title4"]
    actualContent = request.form.get("Title5")
    print(picture)
    if picture.filename == '':
            flash('No file was selected')
            return redirect(request.url)
    elif picture and allowed_file(picture.filename):
        picture.save(os.path.join(app.config["UPLOAD_FOLDER"], picture.filename))
    with open("blog.json", "r") as f:
        blog1 = json.loads(f.read())
    blog1["data"][username] = {"title": title, "description": shortDescription, "catagory": catagory, "photo": os.path.join(app.config["UPLOAD_FOLDER"], picture.filename), "content": actualContent}
    print(blog1)
    with open('blog.json', 'w') as f:
        json.dump(blog1, f, indent=4)
    
    return redirect(url_for("toHome"))

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