# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

# Captura dos dados inseridos pelo usuário
num1 = input("Digite o primeiro número (inteiro ou real): ")
num2 = input("Digite o segundo número (inteiro ou real): ")

# Verificação dos valores
try:
    num1 = float(num1)
    num2 = float(num2)
except ValueError:
    print("Por favor, digite números válidos.")
    exit()

# Realização de operações simples
sum = num1 + num2
sub= num1 - num2
multi = num1 * num2
div= num1 / num2 if num2 != 0 else "Um numero não pode ser dividido por 0"

# Exibe os resultados
print(f"Soma: {sum}")
print(f"Subtração: {sub}")
print(f"Multiplicação: {multi}")
print(f"Divisão: {div}")