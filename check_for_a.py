# 2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

# # IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
import unittest

def check_for_a(string):
    string = string.lower()
    return string.count('a') if 'a' in string else False

class TestCheckForA(unittest.TestCase):
    def test_ola_mundo(self):
        self.assertEqual(check_for_a('ola mundo'), 1)

    def test_hello_world(self):
        self.assertEqual(check_for_a('hello world'), 0)

    def test_target_sistemas(self):
        self.assertEqual(check_for_a('tArget sistemas'), 2)

    def test_algo_a_parte_do_mundo(self):
        self.assertEqual(check_for_a('algo a parte do mundo'), 3)

    def test_testando_funcionalidade(self):
        self.assertEqual(check_for_a('Testando funcionAlidAde'), 3)

if __name__ == '__main__':
    unittest.main()