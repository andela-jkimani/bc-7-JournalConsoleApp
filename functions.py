
from datetime import datetime
from my_database import Database

class JournalEntry:

	def create_entry(self, args):
		"""
			Add entry to the Journal Entry
		
		Args:
			entry - string containing the journal entry
			title - string containing the title of your journal
		"""

		
		body = (" ".join(args['<entry>']))
		title = raw_input('Title: ')
		title = title.upper()

		obj = Database()
		obj.data_entry(title, body)
		print 'Journal entry added successfully'

	def search_text(self, args):
		"""
		Search for a specific journal entry
		Args:
			variable - String you want to search for
		"""
		
		obj = Database()
		obj.search_text(args)

	def search_date(self, search_criteria):
		"""
		Search for a specific journal entry
		Args:
			variable - String you want to search for
		"""
		
		obj = Database()
		obj.search_date(search_criteria)

	def search_both(self, search_criteria):
		"""
		Search for a journal using both date and text
		"""
		obj = Database()
		obj.search_both(search_criteria)

	def open(self, args):

		obj = Database()
		obj.open(args)

	def open_all(self, args):
		obj = Database()
		obj.open_all(args)


	def delete(self, args):
		"""
		Deletes a journal entry that contains certain text
		"""

		obj = Database()
		obj.delete(args)

