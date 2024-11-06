#soliticita os 5 números aos usuários
alunos = []
notas = []

for i in range(5):
  nome = input(f"Digite o nome do aluno {i+1}: ")
  nota = float(input(f"Digite a nota do aluno {i+1}: "))
  alunos.append((nome, nota))

print("\nDados dos alunos: ")
for nome, nota in alunos:
    print(f"Aluno: {nome} \n Nota: {nota}")