def impar():

    lista_aleatoria = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lista_impar = []

    for itens in (lista_aleatoria):
        if itens % 2 != 0:
            lista_impar.append(itens)

    return print(lista_impar)


impar()
