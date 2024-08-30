import os
import json


current_directory = os.path.dirname(__file__)
file_path = os.path.join(current_directory, 'faturamento.json')


with open(file_path, 'r') as file:
    faturamento_diario = json.load(file)

faturamento_valido = [dia['valor'] for dia in faturamento_diario if dia['valor'] > 0]

menor_faturamento = min(faturamento_valido)
maior_faturamento = max(faturamento_valido)


media_mensal = sum(faturamento_valido) / len(faturamento_valido)

dias_acima_da_media = sum(1 for valor in faturamento_valido if valor > media_mensal)

# Exibir os resultados
print(f"Menor valor de faturamento: {menor_faturamento:.2f}")
print(f"Maior valor de faturamento: {maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
