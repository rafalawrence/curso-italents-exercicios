# Solicita o número desejado.
numero = int(input("Digite um número inteiro: "))

# Imprime os divisores do número informado.
print(f"Divisores de {numero}:")
for i in range(1, numero + 1):
    if numero % i == 0:
        print(i)

        # Gustavo Graciotti Camporezi