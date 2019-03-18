import sqlite3

class Message():
	def __init__(self):
		self.conn = sqlite3.connect('data/thewall.db')
		self.cursor = self.conn.cursor()


	def save(self, username, text):
		query = "INSERT INTO message (username, text) VALUES (?, ?) "
		self.cursor.execute(query, (username, text))
		self.conn.commit()
		

	def all(self):
		query = "SELECT * FROM message ORDER BY id DESC"
		self.cursor.execute(query)
		messages = []
		for item in self.cursor.fetchall():
			message = {
			"username" : item[1],
			"text" : item[2]
			}
			messages.append(message)
		
		return messages 


	def close(self):
		self.conn.close()


