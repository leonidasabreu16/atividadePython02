import math
opcao=0
print("ATIVIDADE 2 PYTHON\n")
print("Clique na questão a ser resolvida:\n")
while opcao != 7:
    print("QUESTÕES ATIVIDADE 2\n[1] NUMERO MAIOR\n[2] RAIZ QUADRADA\n[3] VERIFICAR CARGA\n[4] CONJUNTO DE OPERAÇÕES\n[5] EQUAÇÃO DE SEGUNDO GRAU\n[6] ORDEM CRESCENTE\n[7] SAIR DO PROGRAMA\n")
    opcao = int(input("Digite sua opção: "))
    if opcao == 1:
        print("Informe 2 numeros")
        num1 = int(input("Primeiro Valor: "))
        num2 = int(input("Segundo Valor: "))
        if num1 > num2:
            print("O numer:",num1,"é o maior!" )
        else:
            print("O numero:", num2, "é o maior!")
    elif opcao == 2:
        num1 = int(input("Digite um numero: "))
        if num1 >= 0:
            raiz = math.sqrt(num1)
            print("O resuldado da raiz é:\n", raiz)
        else:
            print("Número invalido para raiz\n")
    elif opcao == 3:
        num1 = int(input("Digite um numero: "))
        if num1 > 0:
            print("O numero é positivo")
        elif num1==0:
            print("O numero é igual 0")
        else:
            print("O numero é negativo")
    elif opcao == 4:
        print("Informe dois numeross")
        num1 = int(input("Primeiro Valor: "))
        num2 = int(input("Segundo Valor: "))
        opcao1 = 0
        print("Para voltar ao menu principal digite 5\n")

        while opcao1 != 6:
            print("[1] SOMA\n[2] DIFERENÇA\n[3] MULTIPLICAÇÃO\n[4] DIVISÃO\n[5] ALTERAR NUMEROS\n[6] VOLTAR AO MENU PRINCIPAL")
            opcao1 = int(input("Digite sua opção"))
            if opcao1 == 1:
                soma = num1 + num2
                print("O valor da soma entre {} e {} é {}".format(num1, num2, soma))
            elif opcao1 == 2:
                if num1 > num2:
                    diferenca = num1 - num2
                    print("O resultado sa subtração de {} por {} é {}".format(num1,num2,diferenca))
                else:
                    diferenca = num2 - num1
                    print("O resultado da subtração entre {} por {} é {}".format(num1, num2, diferenca))
            elif opcao1 == 3:
                    multiplicacao = num1 * num2
                    print("A multiplicação de {} por {} é igual a {}".format(num1, num2, multiplicacao))
            elif opcao1 == 4:
                    if num2 != 0:
                        divisao = num1 / num2
                        print("O resultado da divisão entre {} por {} é {}".format(num1, num2, divisao))
                    else:
                        print("Não existe!")
            elif opcao1 == 5:
                num1 = int(input("Primeiro Valor: "))
                num2 = int(input("Segundo Valor: "))
            else:
                 print("Valor Inválido! Digite novamente!\n")
    elif opcao == 5:
        num1 = int(input("Digite o Valor de A: "))
        num2 = int(input("Digite o Valor de B: "))
        num3 = int(input("Digite o Valor de C: "))

        delta = math.pow(num2,2) - 4*num1*num3
        if delta < 0:
            print("O delta é negativo, portanto não existe!")
        else:
            raiz1 = (- num2 + math.sqrt(delta)) / 2 * num1
            raiz2 = (- num2 - math.sqrt(delta)) / 2 * num1
            print("As raizes da função é {} e {}".format(raiz1, raiz2))

    elif opcao == 6:
        num1 = int(input("Digite o numero 1: "))
        num2 = int(input("Digite o numero 2: "))
        num3 = int(input("Digite o numero 3: "))

        numeros = [num1,num2,num3]
        numeros.sort()
        print(numeros)

    elif opcao == 7:
        print("Fim do programa! Volte sempre.")
    else:
        print("Valor Inválido! Digite Novamente!")












