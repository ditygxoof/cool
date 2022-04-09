import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = ("1234567890")
symbols = "!@#$%^&*(){][}~`≈ç√∫˜µß∂ƒ©˙∆˙©ƒ∂ßœ∑´®†¥¨ˆø]"

upper, lower, nums, syms = True, True, True, True

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if syms:
    all += symbols

length = 40
amount = 10

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)

