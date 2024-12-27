# A função reduce aplica uma função de dois argumentos cumulativamente a todos os elementos de um iterável, de forma que o resultado final é um único valor.
from functools import reduce


def soma(x, y):
    return x + y

def main():
    numbers = [1, 2, 3, 4, 5]
    soma_total = reduce(soma, numbers)
    print(soma_total)

if __name__ == '__main__':
    main()