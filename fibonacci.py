def fibonacci():

    num = int(input("Digite quantos numero deve ter a sequência: \n"))
    i = 1

    if num == 0:
        fib = []
    elif num == 1:
        fib = [1]
    elif num == 2:
        fib = [1, 1]
    elif num > 2:
        fib = [1, 1]
        while i < (num - 1):
            fib.append(fib[i - 1] + fib[i])
            i += 1

    return print(fib)


fibonacci()
