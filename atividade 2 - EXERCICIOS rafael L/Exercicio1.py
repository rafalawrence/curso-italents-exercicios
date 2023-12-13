#Cotações das moedas em relação ao Real(R$).
cotacoes = {
    'USD': 5.5,    # Dólar Americano
    'EUR': 6.5,    # Euro
    'GBP': 7.2,    # Libra Esterlina
    'CAD': 4.2,    # Dólar Canadense
    'ARS': 0.055,  # Peso Argentino
    'CLP': 0.007,  # Peso Chileno
}

# Solicita o valor em reais.
valor_em_reais = float(input("Digite o valor em reais (R$): "))

# Converte o valor para as outras moedas.
for moeda, cotacao in cotacoes.items():
    valor_convertido = valor_em_reais / cotacao
    print(f'{moeda}:{valor_convertido:.2f}')

    # Gustavo Graciotti Camporezi