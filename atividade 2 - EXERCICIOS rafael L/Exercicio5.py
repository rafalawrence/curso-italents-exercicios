# Solicita que informe dois números.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Verifica se os números são iguais ou identifica o maior.
if num1 == num2:
    print("Números iguais.")
else:
    maior_numero = max(num1, num2)
    print(f"O maior número é: {maior_numero}")

    # Gustavo Graciotti Camporezi