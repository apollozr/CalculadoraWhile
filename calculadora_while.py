while True:
    try:
      n1 = (int(input('Digite um numero: ')))     # n1 = número 1
      n2 = (int(input('Digite outro numero: ')))  # n2 = número 2
      op = input('Digite o operador (+-/*): ')    # op = operador
    except ValueError:
         print('Numeros incorretos tente novamente')
         continue 
    
    opp = '+-/*'   # opp = operador permitido

    if op not in opp:
        print('O operador e invalido.')
        continue    

    if len(op) > 1:
        print('Digite apenas um operador.')
        continue   

    print('Realizando a conta, confira o resultado abaixo: ')
    if op == '+':
        print(n1 + n2)
    elif op == '-':
        print(n1 - n2)
    elif op == '/': 
         print(n1 / n2)
    else: 
        print(n1 * n2)

    sair = input("Quer sair? [s]im: ").lower().startswith('s')  

    if sair:
        break
  