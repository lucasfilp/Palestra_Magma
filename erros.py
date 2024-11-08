
# Função para calcular o quadrado dos números em uma lista
def calcula_quadrado(lista_numeros):
    quadrados = []
    for numero in lista_numeros:
        quadrado = numero ** 2 
        quadrados.append(quadrado)  

    return quadrados  # ERRO: deve retornar 'quadrados' em vez de 'quadrado'

# Função para verificar se um número é positivo, negativo ou zero
def verifica_positivo_negativo_zero(num):
    if num > 0:
        return "Positivo"  
    elif num < 0:
        return "Negativo" 
    else:
        return "Zero"  

def calcula_media(lista_numeros):
    soma = 0
    for numero in lista_numeros:
        soma += numero
    if len(lista_numeros) == 0:
        return "A lista está vazia, não é possível calcular a média"
    media = soma / len(lista_numeros)
    return media  

# Testando o código
numeros = [2, -3, 0, 5, 7]

print("Quadrados dos números:", calcula_quadrado(numeros))
print("Verificação do segundo número:", verifica_positivo_negativo_zero(numeros[1]))
print("Média dos números:", calcula_media(numeros))
