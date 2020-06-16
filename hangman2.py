import random
key = random.randint(0,3)
wordlist = ["cat","dog","pig","cow"]
word = wordlist[key]
def hangman(word):
        wrong = 0
        stages = ["",
                  "__________            ",
                  "|        |            ",
                  "|        |            ",
                  "|        O            ",
                  "|      ／|＼          ",
                  "|        |            ",
                  "|      ／ ＼          ",
                  "|                     ",
                  "|_____________________",
                  ]
        rletters = list(word)
        board = ["_"] * len(word)
        win = False
        print("ハングマンへようこそ！　絞首刑にされる前に３つのアルファベット（小文字）からなる動物を当てろ")
        while wrong < len(stages) - 1:
            print("\n")
            msg = "一文字を予想してね:"
            jjj = input(msg)
            if jjj in rletters:
               cind = rletters.index(jjj)
               board[cind] = jjj
               rletters[cind] = '$'
            else:
                   wrong += 1
            print(" ".join(board))
            e = wrong + 1
            print("\n".join(stages[0:e]))
            if "_" not in board:
                print("貴方の勝ち")
                print(" ".join(board))
                win = True
                break
        if not win:
            print("\n".join(stages[0:wrong+1]))
            print("貴方の負け！正解は{}。".format(word))

hangman(word)
