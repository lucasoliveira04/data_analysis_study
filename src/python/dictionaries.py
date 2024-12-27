def pedir_dados():
    nome = input("Digite o nome: ").lower().capitalize()
    idade = int(input("Digite a idade: "))
    cidade = input("Digite a cidade: ").lower().capitalize()

    return {"nome": nome, "idade": idade, "cidade": cidade}

def main():
    # Criando dicionário inicial
    pessoa = {
        "nome": "João",
        "idade": 39,
        "cidade": "São Paulo"
    }

    # Acessando valor
    print("Acessando valor: ", pessoa["nome"])

    print("===========================")

    # Iterando sobre dicionário
    for chave, valor in pessoa.items():
        print(chave, valor)

    # Removendo valores
    del pessoa["idade"]

    print("===========================")

    # Iterando sobre dicionário após remoção
    print("Iterando sobre dicionário após remoção:")
    for chave, valor in pessoa.items():
        print(chave, valor)

    print("===========================")

    # Adicionando novos valores
    pessoa = pedir_dados()

    print("===========================")

    # Iterando sobre dicionário após adição
    print("Iterando sobre dicionário após adição:")
    for chave, valor in pessoa.items():
        print(chave, valor)

    print("===========================")
    # Alterando valor
    column = input("Digite a chave que deseja alterar: ")
    if column in pessoa:

        value = input("Digite o novo valor: ")

        if isinstance(column, str):
            value = value.lower().capitalize()

        pessoa[column] = value
        print(f"Chave '{column}' alterada para '{value}'")
    else:
        print(f"A chave '{column}' não foi encontrada.")

    print("===========================")

    # Iterando sobre dicionário após alteração
    print("Iterando sobre dicionário após alteração:")
    for chave, valor in pessoa.items():
        print(chave, valor)

if __name__ == "__main__":
    main()
