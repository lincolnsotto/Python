print("Digite qualquer valor: ")
num = input()
print()
print("Digite um valor de 1 a 5 para multiplicarmos ele: ")
div = input()
print()
num = int(num) * int(div) / int(num)
print()
print("Divida o resultado desse número pelo mesmo número que pensou")
print("Atribua o resultado da divisão de acordo com a relação abaixo")
print("e pense em um pais com essa letra")
print("a = 1, b = 2, c = 3, d = 4, e = 5")
print("Quando estiver pronta, digite ok")
ok = input()
if int(num) == 1:
    print("Seu pais é Argentina")
elif int(num) == 2:
    print("Seu pais é Brasil")
elif int(num) == 3:
    print("Seu pais é Canada")
elif int(num) == 4:
    print("Seu pais é Dinamarca")
elif int(num) == 5:
    print("Seu pais é Espanha")
else:
    print("continue programando Lincoln")
