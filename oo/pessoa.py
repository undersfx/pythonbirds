class Pessoa:
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

    print(Pessoa.cumprimentar(thiago))
    print(thiago.cumprimentar())
    print(id(thiago))

    print(thiago.nome)
    print(thiago.idade)
    for filho in thiago.filhos:
        print(filho.nome)