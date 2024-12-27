
# Definição da classe Pessoa
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome # Atributo
        self.idade = idade # Atributo

    # Método
    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome} e tenho {self.idade} anos.'

    def andar(self):
        return f'{self.nome} está andando.'

def main():
    people1 = Pessoa('João', 30) # Instância
    print(people1.cumprimentar())
    print(people1.andar())

if __name__ == '__main__':
    main()
