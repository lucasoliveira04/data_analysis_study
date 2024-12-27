# A função map aplica uma função a cada item de um iterável (como uma lista) e retorna um iterador.

# Função que será aplicada a cada item
def quadrado(x):
    return x * x

def main():
    # Usando map
    numbers = [1, 2, 3, 4, 5]
    quadrados = map(quadrado, numbers)

    # Convertendo o resultado para uma lista
    print(list(quadrados))

if __name__ == "__main__":
    main()