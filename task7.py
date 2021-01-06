phone = input("phone No : ")
digit_char = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "Eight",
    "9": "Nine",
    "0": "zero"
}
output = ""
for ch in phone:
    output += digit_char.get(ch, "!") + " "
print(output)
