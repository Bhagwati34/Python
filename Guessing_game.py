secret_num = 8
i = 0
while i < 3:
    guess = int(input("Guess the number: "))
    i = i + 1
    if guess == secret_num:
        print("You win !")
        break
else:
    print("sorry, you failed")
