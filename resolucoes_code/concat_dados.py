# Vamos receber dois dados diferentes do usuário e concatena-los em uma única string?!

# Captura dos dados inseridos pelo usuário
str1 = input("Digite o primeiro dado: ")
str2 = input("Digite o segundo dado: ")

# De acordo com a pesquisa feita para o ChatGPT existem algumas formas de relaizar a concatenação de dois dados em uma unica string, são eles: 

# Concatenação usando o operador +
resultado = str1 + " " + str2
print("Concatenação com o operador '+':", resultado)

# Concatenação usando f-strings
resultado = f"{str1} {str2}"
print("Concatenação com f-strings:", resultado)

# Concatenação usando o método format()
resultado = "{} {}".format(str1, str2)
print("Concatenação com o método format():", resultado)

# Concatenação usando o método join()
resultado = " ".join([str1, str2])
print("Concatenação com o método join():", resultado)