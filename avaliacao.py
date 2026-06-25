#Declare uma variável do tipo lista para guardar notas
#Peça para o usuário digitar as notas.
#Para quando o usuário digitar -1 (ou um valor negativo)
#Ao final calcule a média das notas.

notas = []
soma = 0

while(True):
    nota = int(input("Digite a nota:"))
    if (nota < 0):
        break
    elif(nota > 10):
        continue
    else:
        notas.append(nota)

for nota in notas:
    soma+= nota

if(len(notas)==0):
   print('Não há notas na avaliação')
else:
   print("A média das notas é:", (soma/len(notas)))