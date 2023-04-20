while True:
    try:
        numero = int(input("Entre com um número inteiro: "))
        print(5/numero)
        break 
    except (ValueError, ZeroDivisionError):
        print("Valor errado ou não é possível dividir por zero.")
    except:
        print("Desculpa, algo errado aconteceu....")