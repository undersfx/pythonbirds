class Pessoa:
    # Atributo de Classe
    olhos = 2

    # Método Inicializador
    def __init__(self, *filhos, nome=None, idade=None):
        # Atributos de Instância
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    # Método
    def cumprimentar(self):
        return f'Olá {id(self)}'

    # Método Estático
    @staticmethod
    def metodo_estatico():
        return 42
    
    # Método de Classe
    @classmethod
    def metodo_de_classe(cls):
        return f'Classe: {cls}, olhos: {cls.olhos}'

if __name__ == "__main__":
    fulano = Pessoa(nome='Fulano')
    ciclano = Pessoa(nome='Ciclano')
    thiago = Pessoa(fulano, ciclano, nome='Thiago', idade=27)

    # Métodos
    print(Pessoa.cumprimentar(thiago))
    print(thiago.cumprimentar())
    print(id(thiago))

    # Atributos de Instância
    print(thiago.nome)
    print(thiago.idade)

    # Atributo Complexo
    for filho in thiago.filhos:
        print(filho.nome)
    
    # Atributo Dinâmico (Adicionado em Tempo de Execução)
    thiago.sobrenome = 'Rodrigues'
    print(thiago.sobrenome)
    print(thiago.__dict__)
    print(fulano.__dict__)
    del thiago.sobrenome
    print(thiago.__dict__)

    #Atributo de Classe
    print(Pessoa.olhos)
    print(thiago.olhos)
    print(thiago.__dict__)
    thiago.olhos = 1
    print(thiago.__dict__)
    del thiago.olhos
    print(thiago.olhos)

    # Métodos Estáticos
    print(Pessoa.metodo_estatico())
    print(thiago.metodo_estatico())

    # Métodos de Classe 
    print(Pessoa.metodo_de_classe())
    print(thiago.metodo_de_classe())