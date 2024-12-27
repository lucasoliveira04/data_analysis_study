def main():
    numbers = [1, 2, 3, 4, 5]

    # Acessando valor
    print("Acessando valor: ", numbers[2])

    # Adicionando valores
    numbers.append(1) # Adiciona valor no final da lista
    numbers.insert(0, 10) # Adiciona valor na posição 0

    print("===========================")

    # Iterando sobre lista

    for i in numbers:
        print(i)

    # Removendo valores
    numbers.remove(1) # Remove a primeira ocorrência do valor 1

    # Removendo valores com loop
    for i in numbers:
        if i == 1:
            numbers.remove(i)

    print("===========================")

    # Iterando sobre lista após remoção
    print("Iterando sobre lista após remoção crescente:")
    for i in numbers:
        print(i)

    print("===========================")

    # Ordenando lista
    numbers.sort(reverse=False)  # Ordena a lista em ordem crescente

    # Iterando sobre lista após ordenação
    print("Iterando sobre lista após ordenação decrescente:")
    for i in numbers:
        print(i)

    print("===========================")

    numbers.sort(reverse=True)  # Ordena a lista em ordem decrescente

    # Iterando sobre lista após ordenação
    print("Iterando sobre lista após ordenação:")
    for i in numbers:
        print(i)

if __name__ == "__main__":
    main()