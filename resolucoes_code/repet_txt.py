# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

# Captura dos dados inseridos pelo usuário
dado = input("digite o dado a ser repetido: ")
num = input("digite o numero de repetições: ")

# Verificação do numero de repetições e realização das repetições
try:
    num = int(num)
    if num < 0:
        raise ValueError
    else:
        for num_repeat in range(num):
            print(dado)

except ValueError:
    print("valor do numero invalida")
