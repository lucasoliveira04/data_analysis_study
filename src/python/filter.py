# A função filter permite filtrar elementos de um iterável, aplicando uma função que retorna True ou False.

def par(x):
    return x % 2 == 0

def main():
    numbers = [1, 2, 3, 4, 5]
    numebrs_pares = filter(par, numbers)

    if numebrs_pares:
        print(list(numebrs_pares))
    else :
        print('Nenhum número par foi encontrado.')

if __name__ == '__main__':
    main()