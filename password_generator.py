#password generator
import random
import string

password_length=int(input("Enter the length of the password you want to generate : "))

strings=string.ascii_letters + string.digits + string.punctuation  
password=""

for i in range(password_length):
        password+=random.choice(strings)
print(password)    

