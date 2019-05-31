class Pessoa:
    #Atributo de Classe
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == "__main__":
    fulano = Pessoa(nome='Fulano')
    ciclano = Pessoa(nome='Ciclano')
    thiago = Pessoa(fulano, ciclano, nome='Thiago', idade=27)

    # Chamada de Métodos
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