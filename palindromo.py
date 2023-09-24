def palindromo():

    loop = False

    while loop == False:
        palavra = input("Digite um palavra:\n")
        contrario = palavra[::-1]
        if palavra == contrario:
            loop = True
            print("Essa palavra é palíndromo!!")
        else:
            print("Não é palíndromo\n")


palindromo()
