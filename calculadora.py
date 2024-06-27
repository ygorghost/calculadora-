print ('CALCULADORA DE MEDIA')

nome = input('Digite o nome do aluno: ')

print(nome)

print('Digite sua nota : ')

nota1 = float(input('primeira nota: '))
nota2 = float(input('segunda nota: '))
nota3 = float(input('terceira nota: '))
nota4 = float(input('quarta nota: '))


notas = (nota1 + nota2 + nota3 + nota4)
resutado = (notas /4)

if resutado >= 6:
    print (nome,'aprovado/aprovada, nota final: ')
else:
    print (nome,'reprovado/reprovada, notal final: ')

print (resutado)