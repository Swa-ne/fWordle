# # import json

# # # def main():
# # #     dictWord = {}
# # #     words = {}
# # #     # Try easy words
# # #     with open("easy.txt", "r") as db:
# # #         words = json.load(db)
# # #     # Saved all english words in an array
# # #     with open("5letters.txt", "r") as db:
# # #         dictWord = list(json.load(db).keys())
# # #     word = list(words)[0]
# # #     print(word)
# # #     greyLetter = set()
# # #     greenLetter = set()
# # #     yellowLetter = set()
# # #     # Six guesses per word
# # #     for chances in range(6):
# # #         wordLetterCount = {}
# # #         for ltr in word:
# # #             if ltr not in wordLetterCount:
# # #                 wordLetterCount[ltr] = 0
# # #             wordLetterCount[ltr] += 1
# # #         # 0 - Grey - Not in Word
# # #         # 1 - Yellow - in Word but in Wrong index
# # #         # 2 - Green - Correct index of the Letter
# # #         guessedLetter = [0, 0, 0, 0, 0]
# # #         guess = checkIfWord(dictWord)

# # #         for idx, letter in enumerate(guess):
# # #             indexes = list(find(word, letter))
# # #             if letter in wordLetterCount and wordLetterCount[letter] > 0:
# # #                 if idx in indexes:
# # #                     guessedLetter[idx] = 2
# # #                     greenLetter.add(letter)
# # #                 elif idx not in indexes:
# # #                     guessedLetter[idx] = 1
# # #                     yellowLetter.add(letter)
# # #                 wordLetterCount[letter] -= 1
# # #             else:
# # #                 greyLetter.add(letter)
# # #         print(guessedLetter)
# # #         if guessedLetter == [2, 2, 2, 2, 2]:
# # #             break
# # #     print(f"You Lose! the word is {word}")


# # # # To find the indexes of the letter
# # # def find(string, letter):
# # #     for idx, ltr in enumerate(string):
# # #         if ltr == letter:
# # #             yield idx

# # # # Check the word if it is in my dictionary
# # # def checkIfWord(validWords):
# # #     while True:
# # #         guess = input("a: ")
# # #         if len(guess) == 5:
# # #             if guess in validWords:
# # #                 return guess
# # #             else:
# # #                 print("Not a word")
# # #         else:
# # #             print("You need to input 5 letter word")
# # def main():
# #     dictWord = {}
# #     with open("5letters.txt", "r") as db:
# #         dictWord = list(json.load(db).keys())
        
# #     with open("try.txt", "r") as dbs:
# #         with open("special.txt", "w") as db1:
# #             for i in dbs:
# #                 i = i[:-1]
# #                 if i in dictWord:
# #                     db1.write(f"{i}\n")


# # main()

# # with open("try.txt", "r") as db:
# #     with open("special.txt", "w") as db1:
# #         count = 1
# #         db1.write("{\n")
# #         for i in db:
# #             db1.write(f"\"{count}\":\"{i}\",")
# #             count += 1
# #         db1.write("}")

# # import json
# # with open("easy.txt", "r") as db:
# #     easyWords = json.load(db)
# # with open("special.txt", "r") as db:
# #     specialWords = json.load(db)

# # c.execute("""CREATE TABLE special (
# #     id integer,
# #     word text
# # )
# # """)
# # with open("special.txt", "r") as db:
# #     specialWords = json.load(db)
# # for i in specialWords:
# #     c.execute("INSERT INTO special(id, word) VALUES (?, ?)", (i, specialWords[i]))
# # c.execute("DROP table special")
# # words.commit()
# # words.close()
# # print(specialWords)

# # words = sqlite3.connect("words.db")
# # c = words.cursor()
# # Fetch all words
# # dictWord = []
# # c.execute("SELECT * FROM words")
# # 
# # for i in c.fetchall():
#     # dictWord.append(i[0])
# # print(dictWord)

# # Fetch easy words
# # c.execute("SELECT * FROM easy")
# # easyWords = {str(i) : s for i, s in c.fetchall()}

# # Fetch Hard words
# # c.execute("SELECT * FROM hard")
# # hardWords = {str(i) : s for i, s in c.fetchall()}

# # Fetch special words
# # c.execute("SELECT * FROM special")
# # specialWords = {str(i) : s for i, s in c.fetchall()}
# inGameStatsHard = {
#     "played": 0,
#     "wins": 0,
#     "winRate": 0,
#     "cStreak": 0,
#     "mStreak": 0,
#     "gDistribution": {
#         1: 0,
#         2: 0,
#         3: 0,
#         4: 0,
#         5: 0,
#         6: 0
#     },
#     "history": {
#         0: {"text": 0, "color": [0, 0, 0, 0, 0]},
#         1: {"text": 0, "color": [0, 0, 0, 0, 0]},
#         2: {"text": 0, "color": [0, 0, 0, 0, 0]},
#         3: {"text": 0, "color": [0, 0, 0, 0, 0]},
#         4: {"text": 0, "color": [0, 0, 0, 0, 0]},
#         5: {"text": 0, "color": [0, 0, 0, 0, 0]}
#     },
#     "grey": [],
#     "yellow": [],
#     "green": [],
#     "word": ""
# }
# import sqlite3
# words = sqlite3.connect("history.db")
# c = words.cursor()
# c.execute("""CREATE TABLE easy (
#     played text,
#     wins integer,
#     winRate integer,
#     cStreak integer,
#     mStreak integer,
#     word text
# )
# """)
# c.execute("""CREATE TABLE easyDistribution (
#     one integer,
#     two integer,
#     three integer,
#     four integer,
#     five integer,
#     six integer
# )
# """)
# c.execute("""CREATE TABLE easyHistoryText (
#     one integer,
#     two integer,
#     three integer,
#     four integer,
#     five integer,
#     six integer
# )
# """)
# words.commit()
# words.close()

# from datetime import date

# today = date.today()

# # dd/mm/YY
# now = today.strftime("%Y/%m/%d")
# d0 = date(int(now[:3]), int(now[5:7]), int(now[8:]))
# d1 = date(2022, 11, 16)
# delta = d1 - d0
# print('The number of days between the given range of dates is :')
# print(delta.days)

from datetime import datetime, date, timedelta
today = datetime.now()
tom = date.today() + timedelta(1)
date_format = "%Y-%m-%d %H:%M:%S"
nowTime = datetime.strptime(today.strftime("%Y-%m-%d %H:%M:%S"), date_format)
next = datetime.strptime(tom.strftime("%Y-%m-%d %H:%M:%S"), date_format)
timeRemaining = next - nowTime
print(timeRemaining)
# import sqlite3
# import json

# words = sqlite3.connect("words.db")
# c = words.cursor()

# c.execute("""CREATE TABLE daily (
#     id integer,
#     word text
# )""")

# with open("try.txt", "r") as db:
#     dailyWords = json.load(db)
# for i in dailyWords:
#     c.execute("INSERT INTO daily(id, word) VALUES (?, ?)", (i, dailyWords[i]))
# words.commit()
# words.close()