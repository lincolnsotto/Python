# function with parameters
# def hello(name):
#     print("Hello" + name)
#
#
# hello(" Lincoln")
# hello(" Stephany")
###########################


# function without parameters
# def hello():
#     print("Lincoln")
#     print("Stephany")
#     print("Wiliam")
###########################


# definição confusa das variáveis lacais e globais
# def spam():
#     eggs = "spam local"
#     print(eggs)     # local spam


# def bacon():
#     eggs = "bacon local"
#     print(eggs)     # exibe bacon local
#     spam()
#     print(eggs)     # exibe bacon local


# eggs = "global"
# bacon()
# print(eggs)         # exibe global
###########################

# tratando exceções
# código OK

# def spam(divideBy):
#     return 42 / divideBy


# print(spam(2))
# print(spam(4))

# tratando exceções
# código NOK

# def spam(divideBy):
#    try:
#        return 42 / divideBy
#    except ZeroDivisionError:
#        print("divisão por zero")


# print(spam(2))
# print(spam(0))
# print(spam(4))
