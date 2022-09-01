while True:
    print()
    num1 = input('Digite um número :')
    num2 = input('Digite outro número :')
    operador = input('Digite um operador :')
    pergunta = input('Deseja continuar [s] ou [n] ?')
    if pergunta == 's':
        print('sair')
        break
    elif pergunta == 'n':
        print('sua resposta é.')

    if not num1.isnumeric() or not num2.isnumeric():
        print('você precisa digitar um número')
        continue
    num1 = int(num1)
    num2 = int(num2)

    if operador == '+':
        print(num1 + num2)
    elif operador == '-':
        print(num1 - num2)
    elif operador == '/':
        print(num1 / num2)
