
import os
import time
import string
import random


os.system('cls')

pass_length_verify = []
passw = ""

for y in range(6, 43):
    pass_length_verify.append(str(y))


print("###############################################################\n")
print("######                PASSWORD GENERATOR                 ######\n")
print("###############################################################\n")


print("How long would you like your password to be?")
print("*Password must be between 6 - 42 characters*")
time.sleep(1.5)

while True:
    user_input = input(">: ")
    if user_input in pass_length_verify:
        # name = True
        os.system('cls')

        break
    else:
        print("\nYOU MUST INPUT A NUMBER BETWEEN 6-42. PLEASE TRY AGAIN\n")

print("###############################################################\n")
print("######                PASSWORD GENERATOR                 ######\n")
print("###############################################################\n")
time.sleep(.75)
print("Generating your password...\n")
time.sleep(2)

user_input_int = int(user_input)

for x in range(1, user_input_int):
    y = random.choice([random.choice(string.ascii_lowercase),
                      random.choice(string.ascii_uppercase),
                      random.choice(string.punctuation),
                      random.choice(string.digits)])
    passw += str(y)
print(f"Your {user_input_int} char length password is...")
time.sleep(.75)
print(passw)
print("\n")
