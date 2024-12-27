from src.python.oop.Pessoa import Pessoa

# Herança
# Definição da classe filha Estudante
class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade) # Herdando os atributos da classe pai
        self.curso = curso # Atributo

    # Método
    def estudar(self):
        return f'{self.nome} está estudando {self.curso}.'

    # Método
    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}, tenho {self.idade} anos e estudo {self.curso}.'

def main():
    studant1 = Estudante('João', 30, 'Engenharia') # Instância
    print(studant1.cumprimentar())
    print(studant1.estudar())

if __name__ == '__main__':
    main()