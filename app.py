from flask import Flask, render_template, request, redirect

FILENAME = 'list_of_users.txt'

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def greeting_page():
    return render_template('greetings.html')


@app.route("/registration", methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if check_user_in_file(email):
            return redirect("/login")
        else:
            new_user_to_file(email, password)
    return render_template('registration.html')


@app.route("/login", methods=['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if check_user_in_file(email):
            if check_password(email, password):
                return render_template('sign_in_ok.html')
            else:
                return render_template('sign_in_fail.html')
    return render_template('sign_in.html')


def check_user_in_file(email):
    with open(FILENAME, 'r') as file:
        for line in file:
            if email is not None:
                if email in line:
                    return True
        return False


def check_password(email, password):
    with open(FILENAME, 'r') as file:
        if password != "":
            for line in file:
                if email in line:
                    if password in line:
                        return True
        else:
            return False


def new_user_to_file(email, password):
    with open(FILENAME, 'a') as file:
        if email is not None:
            file.write(f"email: {email}, password: {password}\n")
