import unittest
from funciones import par_impar

class TestEsPar(unittest.TestCase):
    def test_numero_par(self):
        self.assertEqual(par_impar(4), "par")
    def test_numero_impar(self):
        self.assertEqual(par_impar(7), "impar")
    def test_numero_0(self):
        self.assertEqual(par_impar(0),"cero")
    def test_numero_negativo_par(self):
        self.assertEqual(par_impar(-4), "par")
    def test_numero_negativo_impar(self):
        self.assertEqual(par_impar(-3), "impar")

if __name__ == '__main__':
    unittest.main()