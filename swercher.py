import sqlite3
import os


conn = sqlite3.connect('swercherdb.db')
c = conn.cursor()

q = ''

def create_table():
	#creating the table if it does not exist
	c.execute('CREATE TABLE IF NOT EXISTS paths(name varchar, filepath varchar)')

def data_entry(username, userfilepath):
	#this is for the user input to insert into the database
	c.execute("INSERT INTO paths(name, filepath) VALUES (?, ?)", 
		(username, userfilepath))
	os.system('cls' if os.name == 'nt' else 'clear') #clearing the previous inputs
	print(username + " " + userfilepath + " has been successfully added to the database")
	conn.commit()

def deleting_entry(username):
	#note there needs to be a check statment to see if the words exists or not 

	#this is to delete records 
	c.execute("DELETE FROM paths WHERE name = ? ", (username,))
	os.system('cls' if os.name == 'nt' else 'clear') #clearing the previous inputs 
	print(username + ' has been delete successfully for the database ')
	conn.commit()


def showing_all():
	#displaying all the data in the database 
	selectstatment = c.execute("SELECT * FROM paths")
	for row in c.fetchall():
		#print(row)
		explorer = ' '.join(row)
		print(explorer)

	



def the_search(username):

	c.execute("SELECT filepath FROM paths where name = ?", (username,))
	for row in c.fetchall():
		#print(row)

		if row == "":
			print(username + 'does not exist in the database')

		explorer = ' '.join(row) #converting a tuple to a string	
		os.startfile(explorer) #doing the search on explorer this goes both ways for files, folders and websites
		os.system('cls' if os.name == 'nt' else 'clear') #clearing the previous inputs 



def user_input():
	while q != 'quit':
		command = input('what would you like:\n')

		#this is for searching in either the broswer or explorer
		if command != 'insert' and command != 'delete' and command != 'quit' and command != 'showall':
			the_search(command)


		#typing insert activates data_entry
		if command == 'insert':
			name = input('NAME: ')
			path = input('FILE PATH: ')
			create_table()
			data_entry(name, path)

		#typing delete activates deleting_entry
		if command == 'delete':
			name = input('NAME: ')
			deleting_entry(name)


		if command == 'showall':
			showing_all()

		#typing quit ends the program
		if command == 'quit':
			c.close() #closing connection with the database 
			conn.close()
			os.system('cls' if os.name == 'nt' else 'clear') #clearing the previous inputs 
			break






user_input()