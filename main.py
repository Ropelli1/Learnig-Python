# Exercício: Tabuada Simples

# Objetivo:
# Escreva um programa que peça ao usuário um número inteiro.
# O programa deve exibir a tabuada desse número de 1 a 10.
# Use uma estrutura de repetição para multiplicar o número pelo contador e exibir o resultado.


numero = int(input("Digite um número: "))

for i in range(1, 11):
    resultado = numero * i
    print(numero, "*", i, "=", resultado)