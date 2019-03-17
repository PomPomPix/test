import sqlite3 

DB_PATH = 'message.db'

def commit_message_to_db(username, message):
	connection = sqlite3.connect(DB_PATH)
	cursor = connection.cursor()
	query = '''
		INSERT INTO message
		(username, message)
		values 
		(?, ?)'''

	cursor.execute(query, (username, message))
	connection.commit()
	connection.close()


def fetch_message_from_db():
	connection = sqlite3.connect(DB_PATH)
	cursor = connection.cursor()
	query = "SELECT * FROM message"
	cursor.execute(query)
	data = cursor.fetchall()
	connection.close()
	return data


# class Message:
# 	def __init__(self):
# 		self.connection = sqlite3.connect(DB_PATH)
# 		self.cursor = self.connection.cursor()

# 	def commit_message_to_db(self, username, message):
# 		# data = (username, message)
# 		query = "INSERT INTO message (usernmae, message) VALUES('{}','{}')".format(name, email)

# 		query = '''
# 			insert into message
# 			(name, message)
# 			values 
# 			(?, ?)'''

# 		self.cursor.execute(query, (username, message))
# 		self.connection.commit()
# 		self.connection.close()

# 		print('insert into xxx values {}, {}'.format(username, message))


# 	def retrieve_all_users(self):
# 		query = "SELECT * FROM customers"
# 		self.cursor.execute(query)
# 		customers = self.cursor.fetchall()
# 		self.connection.close()
# 		return customers

# Initially, build your app with a default User
# Messages (of the class Message) are made of a username and a text
# Messages are displayed on the front end
# When a user types in a message, this message appears on the screen and it registered into the database