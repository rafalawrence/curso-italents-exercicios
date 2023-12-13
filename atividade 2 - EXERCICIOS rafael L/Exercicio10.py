import random

# A máquina escolhe um número aleatório entre 0 e 10.
numero_aleatorio = random.randint(0, 10)

# Solicita que digite um número.
numero_usuario = int(input("Tente adivinhar o número escolhido (entre 0 e 10): "))

# Compara os números e informa se acertou ou errou.
if numero_usuario == numero_aleatorio:
    print("Parabéns! Você acertou!")
else:
    print(f"Você errou. O número escolhido foi: {numero_aleatorio}")

    # Gustavo Graciotti Camporezi