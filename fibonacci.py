# 1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

# IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
import unittest

def fibo(numero):
    # Verificar inputs de negativos e zero.
    if numero <= 0:
        return False
    fibo_arr = [0, 1]
    while True:
        fibo_arr.append(fibo_arr[-1] + fibo_arr[-2])
        if max(fibo_arr) > numero: # Verifica o maior algarismo presente na array, se passou o valor de numero, o numero informado Não Pertence.
            return False
        elif numero in fibo_arr: # Procura o número dentro da array, se encontrar retorna que pertence
            return True
class TestFibo(unittest.TestCase):
    def test_fibo(self):
        self.assertEqual(fibo(0), False)
        self.assertEqual(fibo(5), True)
        self.assertEqual(fibo(8), True)
        self.assertEqual(fibo(145), False)
        self.assertEqual(fibo(144), True)
        self.assertEqual(fibo(-144), False)

if __name__ == '__main__':
    unittest.main()