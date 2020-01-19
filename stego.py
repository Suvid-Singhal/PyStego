import os
from zipfile import ZipFile

print("*****************")
print("Welcome to PySteg")
print("*****************")
print("\n Enter your choice: ")
print("1. Encrypt")
print("2. Decrypt")
choice = input()

if choice == '1':

	secret = input("Enter the text you want to hide: ")
	image = input ("Enter the path to image: ")

	file = open('secret.txt','w')

	file.write(secret)
	file.close()
	file = "secret.txt"

	with ZipFile('meow.zip', 'w') as zipObj:
		zipObj.write(file)

	os.system("cat "+image+" meow.zip > "+image+"_secret")

	os.system("rm -rf "+file+" meow.zip "+image)

if choice == '2':
	imagepath = input("Enter the path to image: ")
	os.system("unzip "+imagepath+" >/dev/null")
	if os.path.exists("secret.txt") == True:
		print("Success!")
		print("Secret Message:\n")
		os.system("cat secret.txt")
		print("\n")
		os.system("rm -rf secret.txt")
	else:
		print("No secret message found...")
