
import random
import string

print("Hey! lets generate a password")

#List of characters
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()abcdefghijklmnopqrstuvwxyz"
#Prompt the user to specified the length of the password
passwordLength = int(input("How long will you like your password to be ?"))
#Generate a random password
newPassword = []

for x in range(passwordLength):
    #Append a random character to the newPassword
    newPassword.append(random.choice(characters))
#Join the list back to a string    
finalPassword = ''.join(map(str, newPassword))

#Let the user know their new password
print("\n This is your new password:", finalPassword)