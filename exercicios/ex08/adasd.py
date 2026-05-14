lista = []


def alunos():
    
    qtd = int(input('Quantos alunos existem na turma: '))
    for alunos in range(qtd):
        nome = str(input(f'Digite o nome do {alunos + 1} aluno: '))
        nota = int(input(f'Digite uma nota de 0 a 10 para o aluno {nome}: '))
    
        dic = {'nome': nome, 'nota': nota}
        lista.append(dic)
    

    maior = menor = lista[0]['nota']
    for pessoas in lista:
        if pessoas['nota'] > maior:
            maior = pessoas['nota']
        if pessoas['nota'] < menor:
            menor = pessoas['nota'] 
    
    soma = 0 
    for conta in lista:
        soma += conta['nota']

    media = soma / len(lista)

    somamedia = 0

    for pm in lista:
        if pm['nota'] > media:
            somamedia += 1
    
    return lista, maior, menor, media, somamedia

lista, maior, menor, media, somamedia = alunos()

print("\n--- Resultado da Turma ---")
print(f"Maior nota: {maior}")
print(f"Menor nota: {menor}")
print(f"Média: {media:.2f}")
print(f"Alunos acima da média: {somamedia}")