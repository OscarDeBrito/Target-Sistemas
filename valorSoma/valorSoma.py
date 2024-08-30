def soma(indice):
    soma = 0
    k = 0

    while k < indice:
        k += 1
        soma += k

    return soma

# Exemplo de uso
indice = 13
resultado = soma(indice)
print(f"O valor final de SOMA é: {resultado}")
