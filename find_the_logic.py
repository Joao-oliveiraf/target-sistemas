# 4) Descubra a lógica e complete o próximo elemento:
# a) 1, 3, 5, 7, ___
# b) 2, 4, 8, 16, 32, 64, ____
# c) 0, 1, 4, 9, 16, 25, 36, ____ impares
# d) 4, 16, 36, 64, ____ Todos pares, 
# e) 1, 1, 2, 3, 5, 8, ____ a + b
# f) 2,10, 12, 16, 17, 18, 19, ____
import math

def a_answer(arr):
    """
    Cada elemento é gerado a partir da soma dele mesmo com 2
    """
    return arr.append(arr[-1] + 2)
def b_answer(arr):
    """
    Cada elemento é gerado a partir da multiplicação do ultimo com 2
    """
    return arr.append(arr[-1] * 2)
def c_answer(arr):
    """
    Cada elemento é gerado a partir da soma dele mesmo com o menor número impar dísponivel
    Um número impar disponível é aquele que ainda não foi utilizado em outra soma
    """
    prox_impar = (arr[-1] - arr[-2]) + 2 # O proximo impar é a diferença entre os ultimos dois indices, somado com 2
    arr.append(arr[-1] + prox_impar)
    return arr
def d_answer(arr):
    """
    Cada elemento é o quadrado de uma sequencia de numeros pares
    """
    ultimo_elemento = arr[-1]
    base_do_proximo = math.sqrt(ultimo_elemento) + 2 # Raiz quadrada do ultimo elemento, somando 2 para achar o proximo numero par
    arr.append(math.pow(base_do_proximo, 2)) # potencia para descobrir o proximo elemento
    return arr
    
def e_answer(arr):
    """
    Cada elemento é gerado a partir da soma dos dois ultimos indices
    """
    return arr.append(arr[-2] + arr[-1])
def f_answer():
    pass
