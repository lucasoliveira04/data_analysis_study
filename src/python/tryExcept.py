# É sempre bom tratar erros de forma adequada, para que seu código não quebre inesperadamente.

def main():
    try:
        numero = int("abc")
    except ValueError as e: # Captura o erro
        print(f"Erro: {e}")
    else: # Se não houver erro
        print(f"Valor convertido: {numero}")
    finally: # Sempre será executado
        print("Bloco try-except finalizado")

if __name__ == '__main__':
    main()