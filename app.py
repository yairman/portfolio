from cs50 import SQL
from flask import Flask, request, redirect, render_template, flash, session, jsonify
from flask_session import Session
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

db = SQL("sqlite:///posts.db")

upload_folder = "static/media"
app.config["UPLOAD_FOLDER"] = upload_folder

admin = db.execute("SELECT * FROM admins")[0]
admin_name = admin['name']
admin_hash_password = admin['hash_password']
admin_email = admin['email']


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "GET":
        return render_template("admin_login.html")
    else:
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        if name == admin_name and email == admin_email and check_password_hash(admin_hash_password, password):
            return render_template("admin.html")
        else:
            return render_template("error.html", message="Error logging in!")
