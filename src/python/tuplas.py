# Tuplas são coleções imutáveis, ou seja, uma vez criadas, seus elementos não podem ser alterados. Elas são úteis quando você precisa garantir que os dados não sejam modificados.

def main():
    pessoa = ('João', 30, 'Engenharia') # Tupla

    # Acessando elementos da tupla
    print(pessoa[0])

    print("====================================")

    # Iterando sobre a tupla
    print("Iterando sobre a tupla")
    for item in pessoa:
        print(item)

    print("====================================")

    # Desempacotamento de tupla
    nome, idade, curso = pessoa

    print("Desempacotamento de tupla")

    print(nome)
    print(idade)
    print(curso)

    print("====================================")

    # Concatenando tuplas
    pessoa2 = ('Maria', 25, 'Medicina')
    pessoas = pessoa + pessoa2

    print("Concatenando tuplas")
    print(pessoas)

    print("====================================")

    separador = ". ".join(
        map(
            str, pessoas
        )
    )

    print("Separador")
    print(separador)

if __name__ == '__main__':
    main()