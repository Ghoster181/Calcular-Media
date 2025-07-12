"""variável em formato de lista, onde as notas serão armazenadas"""

dados = [[], [[], []], []]

"""input e armazenamento dos dados de um ou mais alunos"""

while True:
    dados[0].append(str(input('Nome do aluno: ')).title())
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    dados[1][0].append(n1)
    dados[1][1].append(n2)
    dados[2].append(media)
    resp = str(input('Deseja continuar? (S/N): ')).upper()
    if resp == 'N' or resp != 'S':
        break

"""Criação de um menu para otimização da visualização dos dados"""

print('-=' * 30)
print(f'{'No.':^5}', end='')
print(f'{'NOME':^7}', end='')
print(f'{'MEDIA':^20}')
print('-' * 30)
for i, p in enumerate(dados[0]):
    print(f'{i:^5}', end='')
    print(f'{p:^7}', end='')
    print(f'{dados[2][i]:^20}')

print('-' * 40)

"""Programa principal"""

while True:
    na = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if na != 999:
        print(f'Notas de {dados[0][na]} são {dados[1][0][na] , dados[1][1][na]} ')
    else:
        break

print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')