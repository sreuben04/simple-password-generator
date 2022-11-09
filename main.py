#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


r_pass = []
if nr_letters >0:
  for i in range(1,nr_letters + 1):
    r_pass.append(random.choice(letters))
    # print(r_pass)
if nr_symbols > 0:
  for i in range(1,nr_symbols+1):
    r_pass.append(random.choice(symbols))
if nr_numbers > 0:
  for i in range(1,nr_numbers+1):
    r_pass.append(random.choice(numbers))

random.shuffle(r_pass)
password = ""
for x in r_pass:
  password += x
print(password)  
  



