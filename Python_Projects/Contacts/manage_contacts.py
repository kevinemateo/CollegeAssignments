#added function
#display menu and preform input validation
def displayMenu():
	print("    Main Menu")
	print("*******************")
	print("1.Add New Contact\n2.View your address book\n3.Search for a contact\
		\n4.Edit a contact\n5.Delete a contact\n6.Exit the Program")
	#input validation
	again=True
	while again:
		try:
			response=int(input('Please choose an option(1-6): '))
			again=False
			return response
		except ValueError:
			print("! Value is not a number")
			print("---------------")
			print("    Main Menu")
		print("*******************")
		print("1.Add New Contact\n2.View your address book\n3.Search for a contact\
				\n4.Edit a contact\n5.Delete a contact\n6.Exit the Program")

#choice1
def addNewContact(contacts):
	print("Add new contact")
	print("---------------")
	#get contact valuesprint("-------------")
	name=input("Contacts name: ")
	address=input("Address(no commas): ")
	phones=input("Phone number(just numbers): ")
	email=input("E-mail: ")
	j=0
	#put contact into new list
	newC=[]
	for i in (name,address,phones,email):
		newC.append(i)
	#append list into list of lists(main list of contacts)
	contacts.append(newC)
#choice2
def displayAddressBook(contacts):
	print("Address book")
	print("-------------")
	#prints all contacts with commas in between
	i=0
	for i in range(len(contacts)):
		contactL=contacts[i]
		print((', '.join(contactL)))
		i+=1
	print("-------------")
#choice3
def searchContact(contacts):
	print("Search Contact")
	print("-------------")
	contactSearch = str(input("What contact name are you looking for? ")).lower()
	search=False
	j=0
	#searches through contacts
	while search==False and j!=len(contacts):
	#j is to make the loop end if there is no match in contacts
		for contact in contacts:
			#makes name lower case allows for user to search in case insensitive
			contactS=contact[0].lower()
			if contactS==contactSearch:
				search=True
				printContacts=(', '.join(contact))
				print(printContacts)
		j+=1
	print("*****************************************************")
	if search==False:
		print("!! There is no contact with that name in your address book !!")
#choice4
def modifyContact(contacts):
	print("Modify Contact")
	print("-------------")
	#use searchContact code
	choice=input("Enter contact name to change: ").lower()
	search=False
	j=0
	#searches through contacts
	while search==False and j!=len(contacts):
	#j is to make the loop end if there is no match in contacts
		for contact in contacts:
			#makes name lower case allows for user to search in case insensitive
			contactS=contact[0].lower()
			if contactS==choice:
				search=True
				printContacts=(', '.join(contact))
				print(printContacts)
		j+=1
	print("*****************************************************")
	if search==False:
		print("!! There is no contact with that name in your address book !!")
	#get what the user wants to change of the contact
	print("1.Name\n2.Address\n3.Phone Number\n4.E-mail")
	change=int(input("What would you like to change?(1-4)"))
	if change==1:
		name=input("Enter new name: ")
		contact[0]=name
	elif change==2:
		address=input("Enter new address: ")
		contact[1]=address
	elif change==3:
		phone=input("Enter new phone #: ")
		contact[2]=phone
	elif change==4:
		email=input("Enter new e-mail: ")
		contact[3]=email
#choice5
def deleteContact(contacts):
	print("Remove Contact")
	print("-------------")
	#use searchContact code
	choice=input("Enter contact name to remove: ").lower()
	search=False
	j=0
	#searches through contacts
	while search==False and j!=len(contacts):
	#j is to make the loop end if there is no match in contacts
		for contact in contacts:
			#makes name lower case allows for user to search in case insensitive
			contactS=contact[0].lower()
			if contactS==choice:
				search=True
				contacts.remove(contact)
		j+=1
	print("*****************************************************")
	if search==False:
		print("!! There is no contact with that name in your address book !!")
	print(contact[0],"has been removed from your address book.")
#choice6
def exitAddressBook(contacts):
	print("Goodbye!")
	file=open('contacts.txt','w')
	for contact in contacts:
		contact=(', '.join(contact))+'\n'
		file.write(contact)
#main
def main():
#Create Contacts List
	contacts=[]
	contactsFile=open("contacts.txt",'r')
	line=contactsFile.readline()
	i=0
#strip \n
	while line!='':
		line=line.rstrip('\n')
		line=line.split(', ')
		contacts.append(line)
		line=contactsFile.readline()
		i+=1
#Get user main menu choice	
	choice = displayMenu()
	choice = int(choice)
	#loop to allow user to stay in the menu until they want to get out
	while choice>=1 and choice<6:
		if choice==1:
			addNewContact(contacts)
		elif choice==2:
			displayAddressBook(contacts)
		elif choice==3:
			searchContact(contacts)
		elif choice==4:
			modifyContact(contacts)
		elif choice==5:
			deleteContact(contacts)
		cont=input("Return to main menu? (y/n)").lower()
		if cont =='y':
			choice = int(displayMenu())
		elif cont=='n':
			choice=6
	if choice == 6:
		contactsFile.close()
		exitAddressBook(contacts)
main()