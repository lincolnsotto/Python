print("Send a number: ")

try:
    number = int(input())
except ValueError:
    print("please send a integer value")
    exit()


def collatz(number):
        try:
            if number % 2 == 0:
                print("par number")
            else:
                print("impar number")
                return number

        except TypeError:
                print("please send a integer value")


try:
    print(collatz(number))
except NameError:
    print("please send a integer value")
