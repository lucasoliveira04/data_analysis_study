def applyRegex(value):
    letters = []

    for i in value:
        letters.append(i)

    for i in letters:
        if i.isnumeric():
            return True

def main():
   while True:
       name = input("Digite seu nome: ").capitalize()

       if not applyRegex(name):
           print("Nome Válido")
           break

       print("Nome invalido. Tente novamente.")

if __name__ == '__main__':
    main()