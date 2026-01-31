from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

messages = []

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        message = request.form.get('message')
        if username and message:
            messages.append({
                'username': username,
                'message': message,
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })
        return redirect('/')
    return render_template('messages.html', messages = messages)

app.run(debug=True, port=7700, host='0.0.0.0')