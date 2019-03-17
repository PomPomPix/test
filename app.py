from flask import Flask, render_template, request, url_for, session, redirect
from message import Message

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
	if request.method == 'POST':
		message = Message()
		message.save('username', request.form['text-message'])

	# messages = message.all()
	return render_template('new_index.html', messages=message.all())