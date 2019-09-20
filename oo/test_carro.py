from unittest import TestCase
from unittest import main as unittest_main

try:
    from oo.carro import Motor, Direcao, Carro
except ModuleNotFoundError:
    from carro import Motor, Direcao, Carro

class MotorTesteCase(TestCase):
    def test_velocidade_inicial(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade)
    
    def test_acelerar(self):
        motor = Motor()
        motor.acelerar()        
        self.assertEqual(1, motor.velocidade)

    def test_frear(self):
        motor = Motor()
        motor.acelerar()
        motor.frear()        
        self.assertEqual(0, motor.velocidade)

class DirecaoTesteCase(TestCase):
    def test_direcao_inicial(self):
        direcao = Direcao()
        self.assertEqual('Norte', direcao.valor)
    
    def test_virar_a_direita(self):
        direcao = Direcao()
        self.assertEqual('Norte', direcao.valor)
        direcao.virar_a_direita()
        self.assertEqual('Leste', direcao.valor)
        direcao.virar_a_direita()
        self.assertEqual('Sul', direcao.valor)
        direcao.virar_a_direita()
        self.assertEqual('Oeste', direcao.valor)
        direcao.virar_a_direita()
        self.assertEqual('Norte', direcao.valor)

    def test_virar_a_esquerda(self):
        direcao = Direcao()
        self.assertEqual('Norte', direcao.valor)
        direcao.virar_a_esquerda()
        self.assertEqual('Oeste', direcao.valor)
        direcao.virar_a_esquerda()
        self.assertEqual('Sul', direcao.valor)
        direcao.virar_a_esquerda()
        self.assertEqual('Leste', direcao.valor)
        direcao.virar_a_esquerda()
        self.assertEqual('Norte', direcao.valor)

if __name__ == "__main__":
    unittest_main()
