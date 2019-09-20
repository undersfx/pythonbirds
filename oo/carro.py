"""
Criar uma casse carro que possua dois atributos compostos por outras duas classes:

1 Motor
2 Direção

Motor: Controla a velocidade do carro.
Atributos de dado: Velocidade
Métodos: Acelerar (+1 velocidade), Frear (-2 velocidade)

Direção: Controlar a direção do carro.
Atributos de dado: Direção 4 pontos:  N
                                    O   L
                                      S
Métodos: Virar a Direita, Virar a Esquerda

Exemplos:

# Doctest Motor
>>> motor = Motor()
>>> motor.velocidade
0
>>> motor.acelerar()
>>> motor.velocidade
1
>>> motor.acelerar()
>>> motor.velocidade
2
>>> motor.acelerar()
>>> motor.velocidade
3
>>> motor.frear()
>>> motor.velocidade
1
>>> motor.frear()
>>> motor.velocidade
0

# Doctest Direção
>>> direcao = Direcao()
>>> direcao.valor
'Norte'
>>> direcao.virar_a_direita()
>>> direcao.valor
'Leste'
>>> direcao.virar_a_direita()
>>> direcao.valor
'Sul'
>>> direcao.virar_a_direita()
>>> direcao.valor
'Oeste'
>>> direcao.virar_a_direita()
>>> direcao.valor
'Norte'
>>> direcao.virar_a_esquerda()
>>> direcao.valor
'Oeste'
>>> direcao.virar_a_esquerda()
>>> direcao.valor
'Sul'
>>> direcao.virar_a_esquerda()
>>> direcao.valor
'Leste'
>>> direcao.virar_a_esquerda()
>>> direcao.valor
'Norte'

# Dcotest Carro
>>> carro = Carro(direcao, motor)
>>> carro.calcular_velocidade()
0
>>> carro.acelerar()
>>> carro.calcular_velocidade()
1
>>> carro.acelerar()
>>> carro.calcular_velocidade()
2
>>> carro.frear()
>>> carro.calcular_velocidade()
0
>>> carro.calcular_direção()
'Norte'
>>> carro.virar_a_direita()
>>> carro.calcular_direção()
'Leste'
>>> carro.virar_a_esquerda()
>>> carro.calcular_direção()
'Norte'
>>> carro.virar_a_esquerda()
>>> carro.calcular_direção()
'Oeste'

"""

class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self, incremento=1):
        self.velocidade += incremento

    def frear(self, decremento=2):
        self.velocidade = max(0, self.velocidade - decremento)

class Direcao:
    DIRECOES = ("Norte", "Leste", "Sul", "Oeste")

    def __init__(self):
        self.valor = self.DIRECOES[0]

    def virar_a_direita(self):
        i = (self.DIRECOES.index(self.valor) + 1) % len(self.DIRECOES)
        self.valor = self.DIRECOES[i]
    
    def virar_a_esquerda(self):
        i = (self.DIRECOES.index(self.valor) - 1) % len(self.DIRECOES)
        self.valor = self.DIRECOES[i]

class Carro:
    def __init__(self, direcao, motor):
        self.direcao = direcao
        self.motor = motor

    def calcular_velocidade(self):
        return self.motor.velocidade
    
    def acelerar(self, incremento=None):
        if incremento:
            self.motor.acelerar(incremento)
        else:
            self.motor.acelerar()

    def frear(self, decremento=None):
        if decremento:
            self.motor.frear(decremento)
        else:
            self.motor.frear()
        
    def calcular_direção(self):
        return self.direcao.valor

    def virar_a_direita(self):
        self.direcao.virar_a_direita()
    
    def virar_a_esquerda(self):
        self.direcao.virar_a_esquerda()