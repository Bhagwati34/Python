message = input("> ")
words = message.split()
emoji = {
    ":)": "😊",
    ":(": "😥",

}
# windows key + .(dot) or windows key + ; (for emoji)
output = ""
for word in words:
    output += emoji.get(word, word) + " "
print(output)
