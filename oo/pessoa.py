"""
    Sandbox para brincar com conceitos de classes em Python
"""


class Pessoa:
    # Atributo de Dado (Classe)
    olhos = 2

    # Método Inicializador
    def __init__(self, *filhos, nome=None, idade=None):
        # Atributos de Dado (Instância)
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    # Método
    def cumprimentar(self):
        return f'Olá meu nome é {self.nome}'

    # Método Estático
    @staticmethod
    def metodo_estatico(): # Independe de Instância (self)
        return 42
    
    # Método de Classe
    @classmethod
    def metodo_de_classe(cls): # Tem acesso a classe da Instância (cls)
        return f'Classe: {cls}, olhos: {cls.olhos}'


class Mutante(Pessoa): # Herança
    # Sobrescrita de Atributo de dado
    olhos = 3

class Homem(Pessoa):
    # Sobrescrita de método
    def cumprimentar(self):
        cumprimento_de_classe = super().cumprimentar() # Executar método da classe Pai
        return f'{cumprimento_de_classe}. Aperto de mão.'

if __name__ == "__main__":
    #Testes
    fulano = Pessoa(nome='Fulano')
    ciclano = Pessoa(nome='Ciclano')
    thiago = Pessoa(fulano, ciclano, nome='Thiago', idade=27)

    # Métodos
    print(Pessoa.cumprimentar(thiago))
    print(thiago.cumprimentar())
    print(id(thiago), '\n')

    # Atributos de Instância
    print(thiago.nome)
    print(thiago.idade, '\n')

    # Atributo Complexo
    for filho in thiago.filhos:
        print(filho.nome)

    # Atributo Dinâmico (Adicionado em Tempo de Execução)
    thiago.sobrenome = 'Rodrigues'
    print('\n', thiago.sobrenome)
    print(thiago.__dict__)
    print(fulano.__dict__)
    del thiago.sobrenome
    print(thiago.__dict__, '\n')

    #Atributo de Classe
    print(Pessoa.olhos)
    print(thiago.olhos)
    print(thiago.__dict__)
    thiago.olhos = 1
    print(thiago.__dict__)
    del thiago.olhos
    print(thiago.__dict__)
    print(thiago.olhos, '\n')

    # Métodos Estáticos
    print(Pessoa.metodo_estatico())
    print(thiago.metodo_estatico(), '\n')

    # Métodos de Classe
    print(Pessoa.metodo_de_classe())
    print(thiago.metodo_de_classe(), '\n')

    # Classe Herdeira de Pessoa
    renzo = Homem(nome='Renzo')
    luciano = Pessoa(nome='Luciano')
    print(isinstance(renzo, Pessoa))
    print(isinstance(renzo, Homem))
    print(isinstance(luciano, Pessoa))
    print(isinstance(luciano, Homem), '\n')

    # Sobrescrita de Atributo
    print(renzo.olhos)
    mutante = Mutante(nome='Mutante')
    print(mutante.olhos, '\n')

    # Sobrescrita de Método
    print(renzo.cumprimentar())
    print(mutante.cumprimentar())