catNames = []
while True:
    print("Enter the name of cats: " + str(len(catNames) + 1) +
        " (Or enter nothing to stop.)")
    name = input()
    if name == "":
        break
    catNames = catNames + [name]
print("The cat nam e are: ")
for name in catNames:
    print("" + name)
