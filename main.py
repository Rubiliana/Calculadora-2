def calculator():
    while True:
        
        num1 = input("Digite o primeiro número: ")
        if num1 == 'sair':
            break
        elif not num1.replace('.','',1).isdigit():
            print("Erro: Digite um número válido.")
            continue
        
        num2 = input("Digite o segundo número: ")
        if num2 == 'sair':
            break
        elif not num2.replace('.','',1).isdigit():
            print("Erro: Digite um número válido.")
            continue
        
        op = input("Digite o operador (+, -, *, /): ")
        if op == 'sair':
            break
        elif op not in ['+', '-', '*', '/']:
            print("Erro: Operador inválido.")
            continue
        
        # Realizar cálculo
        if op == '+':
            resultado = float(num1) + float(num2)
        elif op == '-':
            resultado = float(num1) - float(num2)
        elif op == '*':
            resultado = float(num1) * float(num2)
        elif op == '/':
            resultado = float(num1) / float(num2)
        
      
        print(f"Resultado: {round(resultado, 2)}")

calculator()
