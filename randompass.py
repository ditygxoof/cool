import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = ("1234567890")
symbols = ("!@#$%^&*(){][}~`")

upper, lower, nums, syms = True, True, True, True

all = uppercase_letters+lowercase_letters+digits+symbols
    
print('How many characters per password?')
length = input()

print('How many passwords?')
amount = input()

for x in range (int(amount)):
    password = "".join(random.sample(all, (int(length))))
    print(password)

