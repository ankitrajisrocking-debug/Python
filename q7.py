class LibraryItem:
	def __init__(self, title, item_id):
		self.title = title
		self.item_id = item_id
		self.issued = False
	
	def issue(self):
		if not self.issued:
			self.issued = True
			print(f"{self.title} has been issued")
			
		else:
			print(f"{self.title} is already issued.")
			
			
	def return_item(self):
		if self.issued:
			self.issued = False
			print(f"{self.title} has been returned.")
		else:
			print(f"{self.title} was not issued.")
			
	
	def display(self):
		print(f"ID: {self.item_id}, Title: {self.title}")
		
		
	
class Book(LibraryItem):
		def display(self):
			print(f"Book -> ID: {self.item_id}, Title: {self.title}")
			
class Magazine(LibraryItem):
		def display(self):
			print(f"Magazine -> ID: {self.item_id}, Title: {self.title}")
			
class Journal(LibraryItem):
		def display(self):
			print(f"Journal -> ID: {self.item_id}, Title: {self.title}")
			
		
book = Book(101, "Python Programming")
magazine = Magazine(102, "Tech Today")
journal = Journal(103, "AI research jornal")
	
	
items = [book, magazine, journal]
	
for item in items:
	item.display()
		
print("\n--- Issue Operations---")
for item in items:
		item.issue()
		
print(f"\n---Trying to issue again---")
book.issue()
	
print(f"\n---Return operations---")
magazine.return_item()
	
print(f"\ntrying to return book again")
book.return_item()
