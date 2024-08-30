import json

def calcular_faturamento(faturamento_diario):
    # Filtra os dias com faturamento maior que zero (ignora finais de semana e feriados)
    faturamento_filtrado = [dia['faturamento'] for dia in faturamento_diario if dia['faturamento'] > 0]
    
    if not faturamento_filtrado:
        return None, None, 0
    
    # Calcula o menor e maior valor de faturamento
    menor_faturamento = min(faturamento_filtrado)
    maior_faturamento = max(faturamento_filtrado)
    
    # Calcula a média de faturamento mensal
    media_mensal = sum(faturamento_filtrado) / len(faturamento_filtrado)
    
    # Conta os dias com faturamento superior à média mensal
    dias_acima_da_media = sum(1 for f in faturamento_filtrado if f > media_mensal)
    
    return menor_faturamento, maior_faturamento, dias_acima_da_media

def main():
    # Carrega os dados do JSON
    with open('faturamento.json', 'r') as file:
        dados = json.load(file)
    
    # Extrai o faturamento diário dos dados
    faturamento_diario = dados["faturamento_diario"]
    
    # Calcula os resultados
    menor, maior, dias_acima_media = calcular_faturamento(faturamento_diario)
    
    # Exibe os resultados
    if menor is not None and maior is not None:
        print(f"Menor faturamento: {menor}")
        print(f"Maior faturamento: {maior}")
        print(f"Número de dias com faturamento acima da média: {dias_acima_media}")
    else:
        print("Não há dados de faturamento para calcular.")

if __name__ == "__main__":
    main()
