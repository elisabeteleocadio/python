def exibirmenu() :
    print("calculadora básica!")
    print("\nmenu de operações: ")
    print("1. soma")
    print("2. subtração")
    print("3. multiplicação")
    print("4. divisão")
    print("5. resto da divisão")
    print("6. sair")
    escolha = int(input("digite uma opção: "))
    return escolha

# funções:

def soma (n1,n2):
    return n1 + n2    

def subtração (n1,n2):
    return n1 - n2

def multiplicação (n1,n2):
    return n1 * n2

def divisão (n1,n2):
    if n2 != 0:
     return n1 / n2
    else:
     return "erro: divisão por 0 não é permitida :( "

def restodivisão (n1,n2):
    if n2 != 0:
        return n1 % n2
    else:
        return "erro: divisão por 0 não é permitida :( "

# declaração de variàveis

opcao = 0
n1 = 0
n2 = 0

# código principal

while opcao != 6:
    opcao = exibirmenu()

    if opcao in [1,2,3,4,5]:
        n1 = float(input("digite o primeiro número: "))
        n2 = float(input("digite o segundo número: "))
    if opcao == 1:
        print(f"a soma dos valores é: {soma(n1, n2)}\n")
    elif opcao == 2:
        print(f"a subtração dos valores é: {subtracao(n1,n2)}\n")
    elif opcao == 3:
        print(f"a multiplicação dos valores é: {multiplicação(n1,n2)}/n")
    elif opcao == 4:
        print(f"a divisão dos valores é: {divisão(n1,n2)}/n")
    elif opcao == 5:
        print(f"o resto da divisão dos valores é: {restodivisão(n1,n2)}/n")
    elif opcao == 6:
        print(f"saindo do sistema...")
    else:
        print("você escolheu uma opção inválida...  tente novamente! :/")