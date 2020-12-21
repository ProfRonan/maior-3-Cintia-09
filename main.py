"""Arquivo principal que será interpretado pelo interpretador."""



def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    

    primeiro = float(input('Digite o primeiro numero: '))
    segundo  = float(input('Digite o segundo numero : '))
    terceiro = float(input('Digite o terceiro numero: '))

    # Achando o maior número
    
    if primeiro > segundo and primeiro > terceiro:
        maior = primeiro
    elif segundo > primeiro and segundo > terceiro:
        maior = segundo
    else:
        maior = terceiro    

    print(f"{maior}")

    

    

    

if __name__ == '__main__':
    main()
