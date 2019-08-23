# coding=utf-8
#
# myCat = {"size": "fat", "color": "gray", "disposition": "loud"}
# print(myCat)
# print(myCat["size"])
# print("My cat has " + myCat["color"] + " fun")

##################################################################
#
# myDog = {1: "Little", 2: "Black"}
# print(myDog)
# print(myDog[1])
# print(myDog[2])

##################################################################
#
# spam = ["a", "b"]
# spam2 = ["b", "a"]
# print(spam == spam2)
#
# spam = {1: "a", 2: "b"}
# spam2 = {2: "b", 1: "a"}
# print(spam == spam2)

##################################################################
#
# It put friend's birthdays in dictionary
#
# birthdays = {"lincoln": "dec 20", "fabiana": "fev 02"}
#
# while True:
#     print("Enter a name: (blank to quit)")
#     name = input()
#     if name == "":
#         break
#
#     if name in birthdays:
#         print(birthdays[name] + " is the birthday of " + name)
#     else:
#         print("I don't have birthday information for " + name)
#         print("What is their birthday? ")
#         bday = input()
#         birthdays[name] = bday
#         print("birthday data base update")
# print(birthdays)

##################################################################
#
# spam = {"color": "red", "age": "42"}
# for i in spam.values():
#      print(i)

# for i in spam.keys():
#     print(i)

# for i in spam.items():
#     print(i)

##################################################################
#
# spam = {"color": "red", "age": "42"}
# print(list(spam.values()))
# or use keys
# or use items

##################################################################
#
# spam = {"color": "red", "age": "42"}
# print(spam.keys())
# print(list(spam.keys()))

##################################################################
#
# spam = {"color": "red", "age": 42}
# for k, v in spam.items():
#     print("key:" + k + "Value:" + str(v))

##################################################################
# KEYS(), VALUES(), ITEMS() #
# spam = {"color": "red", "age": 42}
# print("color" in spam.keys())
# print("red" in spam.values())
# print("age" in spam)
# print("color" in spam)

##################################################################
# GET() #
# picnicItems = {"apples": 5, "cups": 2}
# print("I'm bringing " + str(picnicItems.get("cups", 0)) + " cups")
# print("I'm bringing " + str(picnicItems.get("eggs", 2)) + " eggs")
# print(picnicItems)

##################################################################
# SETDEFAULT() #
# spam = {"name": "lincoln", "age": 28}
# if "color" not in spam:
#             spam.setdefault("color", "red")
# print(spam)
# print(spam["color"])
# print("red" in spam.values())

##################################################################
# import pprint
#
# message = "Texto de exemplo para contagem de caracteres."
# emptydict = {}
#
# for character in message:
#     emptydict.setdefault(character, 0)
#     emptydict[character] = emptydict[character] + 1
# pprint.pprint(emptydict)

##################################################################
# LET`S PLAY GAME
# Criando um dicionário com as posições.
# theBoard = {"top-l": " ", "top-m": " ", "top-r": " ",
#             "mid-l": " ", "mid-m": " ", "mid-r": " ",
#             "low-l": " ", "low-m": " ", "low-r": " "}
# print(theBoard)


# Criando uma função que representará uma lista no formato do tabuleiro
# de chadrez


# def printBoard(board):
#     print(board["top-l"] + "|" + board["top-m"] + "|" + board["top-r"])
#     print("-+-+-")
#     print(board["mid-l"] + "|" + board["mid-m"] + "|" + board["mid-r"])
#     print("-+-+-")
#     print(board["low-l"] + "|" + board["low-m"] + "|" + board["low-r"])
#
#
# turn = "X"
# for i in range(9):
#     printBoard(theBoard)
#     print("Turn for " + turn + ". Move on which space?")
#     move = input()
#     theBoard[move] = turn
#     if turn == "X":
#         turn = "0"
#     else:
#         turn = "X"
#
# printBoard(theBoard)

##################################################################
#
# allGuests = {"Aline": {"apples": 5, "pretzels": 12},
#              "Bob": {"ham": 3, "apples": 2},
#              "Carol": {"cups": 3, "apple pie": 1}}
#
#
# def totalBrought(guests, item):
#     numbrought = 0
#     for k, v in guests.items():
#         numbrought = numbrought + v.get(item, 0)
#     return numbrought
#
# print("Number of things being brought:")
# print("Apples: "+str(totalBrought(allGuests, "apples")))
# print("pretzels: "+str(totalBrought(allGuests, "pretzels")))
# print("ham: "+str(totalBrought(allGuests, "ham")))
# print("cups: "+str(totalBrought(allGuests, "cups")))
# print("apple pie: "+str(totalBrought(allGuests, "apple pie")))

##################################################################
