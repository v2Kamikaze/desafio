import unittest
import desafio


class VerificaRodizio(unittest.TestCase):
    def testar_rodizio(self):
        esperado = True
        resultado_recebido = desafio.rodizio_de_pedidos()
        self.assertEqual(esperado, resultado_recebido)
