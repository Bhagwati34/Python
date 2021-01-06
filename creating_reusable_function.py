def emoji_converter(massage):
    word = massage.split(" ")
    emoji = {
        ":)": "😊",
        ":(": "😞"
    }

    output = ""
    for wrd in word:
        output += emoji.get(wrd, wrd) + " "
    return output


massage = input("> ")
rslt = emoji_converter(massage)
print(rslt)
