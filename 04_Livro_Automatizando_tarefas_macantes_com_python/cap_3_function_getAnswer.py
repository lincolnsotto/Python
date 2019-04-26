import random


def getAnswer(answerNumer):
    if answerNumer == 1:
        return "It is cartain"
    elif answerNumer == 2:
        return "It is decidely so"
    elif answerNumer == 3:
        return "Yes"
    elif answerNumer == 4:
        return "Reply hazy try again"
    elif answerNumer == 5:
        return "Ask again later"
    elif answerNumer == 6:
        return "Concentrate and ask again"
    elif answerNumer == 7:
        return "My reply is no"
    elif answerNumer == 8:
        return "Outlook not so good"
    elif answerNumer == 9:
        return "Very dubful"
        r = random.randint(1, 9)
        fortune = getAnswer(r)
        print(fortune)
