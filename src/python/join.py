# O método join é usado para unir os elementos de um iterável (como uma lista ou tupla) em uma única string.

def main():
    itens = ["maçã", "banana", "cereja"]
    fruta = ", ".join(itens)
    print(fruta)


if __name__ == "__main__":
    main()