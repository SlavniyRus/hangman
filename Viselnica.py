def viselnica():
    word = input("Enter word").lower()
    wrong = 0
    stages = ["",
              "__________         ",
              "|                  ",
              "|         |        ",
              "|         O        ",
              "|        /|\       ",
              "|        / \       ",
              "|     |=           ",
              ]
    remaining_letters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Добро пожаловать на Казнь")
    while wrong < len(stages) - 1:
        print("\n")
        guess = "enter char: "
        char = input(guess)
        if char in remaining_letters:
            cind = remaining_letters.index(char)
            board[cind] = char
            remaining_letters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "__" not in board:
            print("U win! Word was: ")
            print(" ".join(board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0: wrong + 1]))
        print(' Game over:(\nБыло загадано слово: {}'.format(word))
