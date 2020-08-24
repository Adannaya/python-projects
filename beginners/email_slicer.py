print("Email slicer!\nEnter an email address and the username and domain name will be returned to you\n")
email = input("Enter an email address here: ")

at_index = email.find("@")
if at_index == -1:
	print('Are you sure this is a valid email address? There is no "@" symbol.')
else:
	username = email[:at_index]
	domain = email[at_index + 1:]
	print(f"Username: {username}\nDomain name: {domain}")
