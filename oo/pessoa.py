class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == "__main__":
    p = Pessoa('Thiago', 27)

    print(Pessoa.cumprimentar(p))
    print(p.cumprimentar())
    print(id(p))

    print(p.nome)
    print(p.idade)