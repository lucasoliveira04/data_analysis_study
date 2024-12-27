# É uma forma concisa de criar listas em Python.
# Permite a construção de novas listas aplicando uma expressão sobre um iterável (como uma lista ou range).


def main():
    numbers = [1, 2, 3, 4, 5]
    # quadrados = [x * x for x in numbers] # List Comprehension
    quadro_pares = [x * x
                    for x in numbers
                    if x % 2 == 0
                    ] # List Comprehension
    print(quadro_pares)

if __name__ == '__main__':
    main()