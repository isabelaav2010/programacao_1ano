#Peça ao usuário um número inteiro n e mostre os quadrados dos números de 1 até n.

numero = int(input("Digite um número inteiro"))
for i in range (1, numero+1):
  print(f"O quadrado de {i} é = {i**2}")
  