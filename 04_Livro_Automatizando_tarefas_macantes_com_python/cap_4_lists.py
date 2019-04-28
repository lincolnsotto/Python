#########################################################
# it = ["cat", "bat", "rat", "elephant"]
# print("the " + it[0] + " ate the " + it[2])

#########################################################
# it_2 = [["cat", "bat", "rat", "elephant"], ["00", "10", "20", "30"]]
# print(it_2[0][1])
# print(it_2[1][-1])

#########################################################
# it_3 = ["cat", "bat", "rat", "elephant"]
# print(it_3[1:3])
# print(it_3[:])
# print(it_3[1:])
# print(it_3[:2])
# print(len(it_3))
# print(type(it_3))

#########################################################
# it_4 = ["cat", "bat", "rat", "elephant"]
# it_4[0] = "dog"
# print(it_4)

#########################################################
# it_5 = ["cat", "bat", "rat", "elephant"]
# it_5 = it_5 + [1, 2, 3, 4]
# it_5 = it_5 * 2
# print(it_5[:])

#########################################################
# it_6 = ["cat", "bat", "rat", "elephant"]
# del it_6[:-2]
# print(it_6)

#########################################################
# for i in range(1, 100, 10):
#     print(i)

# it_7 = [1, 2, 30, 4, 5]
# for i in it_7:
#     it_7.sort()
#     print("***" + str(i) + "***")

#########################################################
# supplies = ["pens", "staplers", "flame-throwers", "binders"]
# for i in range(len(supplies)):
#     print("index: " + str(i) + " in supplies is: " + supplies[i])

#########################################################
# it_8 = ["lincoln", "lincoln1", "lincoln2", "lincoln3"]
# if "lincoln" in it_8:
#     print("ok")
# else:
#     print("NOK")

#########################################################
# it_9 = ["lincoln", "lincoln1", "lincoln2", "lincoln3"]
# print("Digite um nome da familia")
# name = input()
# if name in it_9:
#     print("Nome OK")
# else:
#     print("Nome NOK")

#########################################################
# cat = ["fat", "black", "loud"]
# size = cat[0]
# color = cat[1]
# disposition = cat[2]
# print(cat)
# print(size)
# print(color)
# print(disposition)

# OR BETTRER..

# cat = ["fat", "black", "loud"]
# size, color, disposition = cat
# print(cat)
# print(size)
# print(color)
# print(disposition)

#########################################################
# spam = 42
# spam += 1
# print(spam)

#########################################################
# spam = " Hello"
# c = " world"
# spam *= 3
# spam += c * 3
# print(spam)

#########################################################
# spam = [1, 4, 3, 2]

# spam.insert(1, 5)  # insert number 5 in first position
# spam.sort()  # ordened AASC
# print(spam.index(5))  # print number 5 position
# print(spam)  # print new list

#########################################################
# spam = ["D0", "a1", "A2", "b1", "B2", "D0"]

# spam.sort(key=str.lower)
# spam.remove("D0")
# print(spam)

#########################################################
# import random
# messages = ["it is cetain",
#             "it is decidely to",
#             "yes definitely",
#             "reply hazy try again",
#             "ask again later",
#             "concentrate and ask again",
#             "my reply is no",
#             "outlook not so good",
#             "very doubful"]
# print(messages[random.randint(0, len(messages)-1)])

#########################################################
# name = "lincoln"
# name = name + " Sotto"
# for i in name:
#     print("@@@ " + i + " @@@")

#########################################################
# name = "Lincoln Sotto"
# print(len(name))
# print(name[8:])
# newName = name[:8] + "teste " + name[8:]
# print(newName)

#########################################################
# eggs = [1, 2, 3, 5]
# print(eggs)
# del eggs[3]
# eggs.append(4)
# print(eggs)

#########################################################
# print(tuple([1, 2, 3, "teste"]))
# print(list((1, 2, 3, "teste")))

#########################################################
# the list is a reference, then:
# lst = [1, 2, 3, 4, 5]
# lst1 = lst
# lst2 = lst
# print(lst, lst1, lst2)

#########################################################
#
#
# def eggs(someParameter):
#     someParameter.append("hello")
#
#
# spam = [1, 2, 3]
# eggs(spam)
# print(spam)

#########################################################
# import copy
#
# spam = ["A", "B", "c"]
# cheese = copy.copy(spam)
# cheese[0] = "aa"
#
# print(spam)
# print(cheese)

#########################################################
