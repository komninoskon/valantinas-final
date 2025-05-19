from dotenv import load_dotenv
import os
load_dotenv()
EMAIL_ADDRESS = os.getenv('EMAIL_USER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASS')
from flask import Flask, render_template, request, redirect
import datetime
import smtplib
from email.message import EmailMessage
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/menu')
def food_menu():
    return render_template("menu.html")

@app.route('/drinks')
def drinks_menu():
    return render_template("drinks_menu.html")

@app.route('/reservation', methods=["GET", "POST"])
def reservation():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        people = request.form['people']
        date = request.form['date']
        time = request.form['time']

        with open("C:/Users/User/Documents/restaurant_app/reservations.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.datetime.now()} - {name}, {phone}, {people} άτομα, {date} {time}\n")
        msg = EmailMessage()
        msg['Subject'] = 'Νέα Κράτηση Τραπεζιού'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_ADDRESS
        msg.set_content(f"Όνομα: {name}\nΤηλέφωνο: {phone}\nΆτομα: {people}\nΗμερομηνία: {date}\nΏρα: {time}")
        
        with smtplib.SMTP_SSL( 'smtp.gmail.com', 465) as smtp:
            smtp.login( EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        return redirect('/')
    return render_template('reservation.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
