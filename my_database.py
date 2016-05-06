import sqlite3
from datetime import datetime, timedelta


class Database:
	def __init__(self):
		self.conn = sqlite3.connect('journal.db')
		self.cursor = self.conn.cursor()
		self.cursor.execute("CREATE TABLE IF NOT EXISTS JournalEntries(id INTEGER PRIMARY KEY AUTOINCREMENT, created_at TIMESTAMP, title TEXT, body TEXT)")

	def data_entry(self, title, body):
		"""
		Enters data into database

		Attr:
			created_at
			entry
			tags
		"""
		with self.conn:
			self.cursor.execute("INSERT INTO JournalEntries (created_at, title, body) VALUES('%s', '%s', '%s')" % (datetime.now(), title, body))

	def search_text(self, args):
		"""
		Searches for entries based on journal body/entry
		"""
		# import pdb; pdb.set_trace()

		self.cursor.execute("SELECT * FROM JournalEntries WHERE body LIKE '%{}%' ORDER BY id LIMIT 10".format(args))
		for row in self.cursor.fetchall():
			print '\n  {} : {} \n    {} \n   {}\n\n'.format(row[0], row[1], row[2], row[3])

	def search_date(self, search_criteria):
		n = int(search_criteria[1])
		day_n_days_ago = datetime.now() - timedelta(days = n)

		if search_criteria[0] == '<':
			self.cursor.execute("SELECT * FROM JournalEntries WHERE created_at > '{}' ORDER BY id LIMIT 10".format(day_n_days_ago))
		else:
			self.cursor.execute("SELECT * FROM JournalEntries WHERE created_at < '{}' ORDER BY id LIMIT 10".format(day_n_days_ago))
			
		for row in self.cursor.fetchall():
			print '\n  {} : {} \n    {} \n   {}\n\n'.format(row[0], row[1], row[2], row[3])


	def search_both(self, search_criteria):
		n = int(search_criteria[1])
		day_n_days_ago = datetime.now() - timedelta(days = n)

		if search_criteria[0] == '<':
			self.cursor.execute("SELECT * FROM JournalEntries WHERE created_at > '{}' AND body LIKE '%{}%' ORDER BY id LIMIT 10".format(day_n_days_ago, search_criteria[4]))
		else:
			self.cursor.execute("SELECT * FROM JournalEntries WHERE created_at < '{}' AND body LIKE '%{}%' ORDER BY id LIMIT 10".format(day_n_days_ago, search_criteria[4]))

		for row in self.cursor.fetchall():
			print '\n  {} : {} \n    {} \n   {}\n\n'.format(row[0], row[1], row[2], row[3])

	
	def delete(self, args):
		"""Delete entry with a certain word"""
		self.cursor.execute("DELETE FROM JournalEntries WHERE body LIKE '%{}%'".format(args))
		self.conn.commit()

	def open(self, args):
		self.cursor.execute("SELECT * FROM JournalEntries WHERE id = {}".format(args))
		for row in self.cursor.fetchall():
			print '\n  {} : {} \n    {} \n   {}\n\n'.format(row[0], row[1], row[2], row[3])

	def open_all(self, args):
		self.cursor.execute("SELECT * FROM JournalEntries")
		for row in self.cursor.fetchall():
			print '\n  {} : {} \n    {} \n   {}\n\n'.format(row[0], row[1], row[2], row[3])