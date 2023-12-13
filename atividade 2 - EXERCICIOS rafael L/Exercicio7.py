# Solicita o salário atual do colaborador.
salario_atual = float(input("Digite o salário atual do colaborador: "))

# Calcula o reajuste salarial com base nas faixas salariais.
if salario_atual <= 280.0:
    percentual_aumento = 20
elif salario_atual <= 700.0:
    percentual_aumento = 15
elif salario_atual <= 1500.0:
    percentual_aumento = 10
else:
    percentual_aumento = 5

# Calcula os valores relacionados ao reajuste.
valor_aumento = (percentual_aumento / 100) * salario_atual
novo_salario = salario_atual + valor_aumento

# Exibe as informações.
print(f"Salário antes do reajuste: R${salario_atual:.2f}")
print(f"Percentual de aumento aplicado: {percentual_aumento}%")
print(f"Valor do aumento: R${valor_aumento:.2f}")
print(f"Novo salário após o reajuste: R${novo_salario:.2f}")

# Gustavo Graciotti Camporezi