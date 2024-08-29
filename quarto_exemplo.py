"""
SOMANDO NÚMEROS
"""

soma = 0 # lista (armazena uma fila de numeros)

while True:
    numero = int(input("Digite um número (0 para parar): "))
    soma += numero
    if numero == 0:
        break

print(f"A soma total é: {soma}")