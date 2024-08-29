#Atribuiçãode variáveis
nome = "Elisabete"
idade = 15
altura = 1.63

#exibir mensagem na tela
print(" Nome: ", nome, "Idade: ", idade, " Altura ", altura)
# formação com f-string
print(f"Nome: {nome}  | Idade: {idade} | Altura: {altura}")

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: ")) 
altura = float(input("Digite a sua altura: "))

print(f"Nome: {nome}  | Idade: {idade} | Altura: {altura}")