"""
Author:         Cody Burhans
Date:           11/30/2021
Course:         SDEV 300
Description     Flask app designed to meet the basic requirements of Lab6
"""

from datetime import datetime
from flask import Flask, render_template, request

# Set globals
HOST = 'localhost'
PORT = 8080

app = Flask(__name__)


def get_datetime():
    """
    Helper function to get a formatted datetime
    :return: string formatted datetime
    """
    date_time = datetime.now()
    dt_formatted = date_time.strftime("%d/%m/%Y %H:%M:%S")
    return dt_formatted


@app.route('/')
def index():
    """
    Display available site routes
    :return: supported routes
    """
    return render_template('index.html')


@app.route('/resources', methods=['GET'])
def resources():
    """
    Display site resources and datetime
    :return: site info
    """
    return render_template('resources.html', dt=get_datetime())


@app.route('/about', methods=['GET'])
def about():
    """
    Display site information and contact info
    :return: help/contact info
    """
    return render_template("about.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Display register form for account creation
    :return: confirmation
    """
    # Display form if get request, read form data if post
    content = ""
    if request.method == "GET":
        content = render_template("register.html")
    elif request.method == "POST":
        # It will be more fun later on if I don't escape/validate input :)
        email = request.form.get("email", default=None)
        phone_number = request.form.get("phone_number", default=None)

        if email is not None and phone_number is not None:
            content = "A confirmation email has been sent to complete your sign up! (not really)"
        else:
            content = "Invalid email or phone"
    return content


if __name__ == "__main__":
    # Start the flask app using globals
    app.run(host=HOST, port=PORT)
