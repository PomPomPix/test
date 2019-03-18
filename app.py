from flask import Flask
from flask import render_template, request, url_for, session, redirect
from message import Message

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
	message = Message()
	
	if request.method == 'POST':
		message.save('current_username', request.form['message-content'])

	return render_template('index.html', messages=message.all())