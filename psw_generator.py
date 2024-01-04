import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]


print("Welcome to the PyPassword Generator!")
ltrs = int(input("How many letters would you like in your password?\n"))
smbls = int(input("How many symbols would you like?\n"))
nmbrs = int(input("How many numbers would you like?\n"))

psw = ""
# Easy mode
for n in range(ltrs):
    psw += letters[random.randint(0, len(letters) - 1)]
for n in range(smbls):
    psw += symbols[random.randint(0, len(symbols) - 1)]
for n in range(nmbrs):
    psw += numbers[random.randint(0, len(numbers) - 1)]

print(f"yor psw is: '{psw}'")

# hard mode
psw_l = []

for char in range(1, ltrs + 1):
    psw_l.append(random.choice(letters))
for char in range(1, smbls + 1):
    psw_l += random.choice(symbols)
for char in range(1, nmbrs + 1):
    psw_l += random.choice(numbers)
random.shuffle(psw_l)
psw_h = "".join(psw_l)
print(f"yor hard psw is: '{psw_h}'")
