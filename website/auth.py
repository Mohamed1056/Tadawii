from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route("/login")
def login():
    return render_template("login.html")

@auth.route("/logout")
def log_out():
    return "<p>Log-out</p>"

@auth.route("/sign-up")
def sign_up():
    return render_template("sign_up.html")

@auth.route('sign-up/doctor_signup')
def doctor_signUp():
    return render_template("doctor_signup.html")

@auth.route('sign-up/patient_signup')
def patient_signUp():
    return render_template("patient_signup.html")