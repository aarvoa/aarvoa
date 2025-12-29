from flask import Flask, render_template, request
from datetime import datetime
from users import users
from cards import cards
from balances import balances
from pins import pins
from transactions import transactions

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return '''<h3>We are the best toy bank.</h3>
    <p>I am made by a 11 yr old.</p>
    I am only made for Education purpose.'''

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'GET':
        card_number = request.args.get('card', type=str)
        if card_number in cards:
            user_name = cards[card_number]
            return render_template('checkout.html', user_name=user_name, card_number=card_number)
        else:
            return "Invalid Card Number"
    if request.method == 'POST':
        card_number = request.form.get('card')
        user_name = cards[card_number]
        amount = float(request.form.get('amount'))
        pin = request.form.get('pin')
        balance = balances[user_name]
        if balance >= amount:
            user_pin = pins[card_number]
            if user_pin == pin:
                balances[user_name] = balance - amount
                new_transaction = {
                    "amount": amount,
                    "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                transactions[user_name].append(new_transaction)
                return "Transaction Processed"
            else:
                return "Invalid Pin"
        


@app.route('/dashboard', methods=['POST'])
def dashboard():
    user_name = "Guest"
    if request.method == 'POST':
        user_name = request.form.get('username')
        if user_name in users:
            password = request.form.get('password')
            if password == users[user_name]:
                return render_template('dashboard.html',
                           user_name=user_name,
                           current_datetime=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                           balance = balances[user_name],
                           transactions = transactions[user_name])
            else:
                return "Invalid Password"
        else:
            return "Invalid Username"


app.run(host='0.0.0.0', debug=True, port=6767)
