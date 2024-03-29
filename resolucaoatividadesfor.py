# -*- coding: utf-8 -*-
"""ResolucaoatividadesFOR.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GXUcEQ47yt_3rjRlGSJBicbsmPv1zbcV
"""



# 1. Faça um programa que leia 5 números e informe o maior número

#leia 5 numeros
#saber qual numero e o maior
#informe o maior

maior_numero = float ('-inf')

for contador in range(5): #inicio de bloco
  numero = float(input(f"Digite o {contador+1} numero"))
  if numero > maior_numero:
    maior_numero = numero # maior numero recebe o valor da variavel numero
#final do bloco
print(f"O maior numero e: {maior_numero}")

#2. Faça um programa que verifique e mostre os números entre 1.000 e 2.000 (inclusive) que, quando divididos por 11 produzam resto igual a 2.

#verificar numeros
# mostrar numeros
# entre 1000 e 2000 INCLUSIVE
# quando divididos por 11, precisam ter o resto IGUAL a 2

for abacate in range(1000,2001):
  if abacate % 11 == 2:
    print(abacate)

##3. Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0

for i in range(5):
  numero = float(input("Digite qualquer numero: "))
  soma += numero
  print("Soma = ",soma)

media = soma/5
print("Media =", media)

#4. Faça um programa que receba um número e usando laços de repetição calcule e mostre a tabuada desse número

numero = int(input("Digite o numero que vc quer a tabuada"))
print(f"Tabuada do {numero}")

for i in range(1,11):
  resultado = numero * i
  print(f"{numero}*{i}={resultado}")

#5. Faça um programa que mostre as tabuadas dos números de 1 a 10 usando laços de repetição

# mostrar tabuadas
# tabuadas de 1 a 10
# usar laco de repeticao


for num in range(1,11): #Laco de 1 a 10
  for i in range(1,11): #Laco para a multiplicacao de 1 a 10
    print(f"{num} X {i} = {num * i}")

#6. Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.

# imprimir os numeros de 1 a 20
# um embaixo do outro
# um do lado do outro

for i in range(1,21):
  print(i)
print(list(range(1,21)))

#7.Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

for i in range(1,51):
  if i% 2 != 0:
    print(i)

#8. Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))

for i in range(n1 +1,n2):
  print(i)

#9. Uma loja deseja cadastrar 5 clientes e verificar se o faturamento da loja foi superior a loja B (faturamento = 54000).
# Se o faturamento atingir esse valor mostre na tela uma mensagem contendo em quanto foi superado o faturamento.

lojaB = 54000
lojaA = 0

for cliente in range(5):
  gasto = float(input(f"Digite o gasto do cliente {cliente+1}"))
  lojaA += gasto

if lojaA > lojaB:
  print(f"A loja A superou o faturamento da loja B com um valor arredadado maior de R${}")
elif lojaB > lojaA:
  print(f"A loja B superou o faturamento da loa A com um valor arrecadado maior de R$")
else
  print(f"As duas lojas arrecadaram o mesmo valor de R${LojaA}")

#10. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

numeros_pares = 0
numeros_impares = 0

for i in range(1,11):
  numero = int(input(f"Digite o {i} numero interio:"))

  if numero % 2 == 0:
    numeros_pares += 1 #incrementa a contagem de numeros pares
  else:
    numeros_impares += 1 #incrementa a contagem de numeros impares
print(f"A quantidade de numeros pares e {numeros_pares} e a quantidade de numeros impares e {numeros_impares}")

"""11. Um funcionário de uma empresa recebe aumento salarial anualmente:
Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao
dobro do percentual do ano anterior. Faça um programa que determine o
salário atual desse funcionário. Após concluir isto, altere o programa
permitindo que o usuário digite o salário inicial do funcionário.
"""

# recebe aumento anualmente
# foi contratado em 1995
# salario inicial de 1.000
# em 1996 recebeu 1,5%
# 1997 inclusive dobro do ano anterior %

salario = float(input("Digite o salario inicial do funcionario:"))
percentual = 0.015

for i in range(1996,2025):
  aumento = salario * percentual
  salario += aumento
  percentual *=2
  print(f"Salario em {i} = {salario: .2f}")

"""12. Faça um programa que peça uma nota, entre zero e dez. Mostre uma
mensagem caso o valor seja inválido e continue pedindo até que o usuário
informe um valor válido.
"""

for i in range(999):
  nota = int(input("Digite uma nota entre 0 e 10: "))
  if nota >= 0 and nota <= 10:
    break
  else:
    print("\nValor e invalido.")

while True:
  nota = int(input("Digite uma nota entre 0 e 10:"))
  if nota >= 0 and nota <= 10:
    break
  else:
    print("\nValor e invalido.")

"""13. Uma loja tem tem uma política de descontos de acordo com o valor da
compra do cliente. Os descontos começam acima dos R$500. A cada 100
reais acima dos R$500,00 o cliente ganha 1% de desconto cumulativo até
25%.
Por exemplo: R$500 = 1% || R$600,00 = 2% … etc…
Faça um programa que exiba essa tabela de descontos no seguinte formato:
Valordacompra – porcentagem de desconto – valor fina
"""

valor = float(input("Digite o valor do produto: R$:"))

contador = 2

if valor >=600 and contador:
  reduzido = valor - 500
  if reduzido >= 100 or contador <=24:
    for x in range(999):
      contador += 1
      reduzido -= 100
      if reduzido < 100 or contador == 24:
        break

porcentagem = contador / 100
desconto = valor * porcentagem
final = valor - desconto
print(f'O produto de R${valor:.2f} ficará a partir de R${final:.2f} com {desconto:.0f}% de desconto.')

"""14. Faça um programa que receba a idade de 15 pessoas e que calcule e
mostre:
a) A quantidade de pessoas em cada faixa etária;
b) A percentagem de pessoas na primeira e na última faixa etária, com relação
ao total de pessoas:
 Até 15 anos
 De 16 a 30 anos
 De 31 a 45 anos
 De 46 a 60 anos
 Acima de 61 anos
"""

ate15 = 0
de16a30 = 0
de31a45 = 0
de46a60 = 0
mais60 = 0

for pessoa in range(15):
  idade = int(input(f"Digite a idade da pessoa {pessoa+1}"))
  if idade <= 15:
    ate15 += 1
  elif 16 <= idade <= 30:
    de16a30 += 1
  elif 31 <= idade <= 45:
    de31a45

"""15. Faça um programa que peça dois números, base e expoente, calcule e
mostre o primeiro número elevado ao segundo número. Não utilize a
função de potência da linguagem.
"""

base = int(input("Digite o valor base: "))
expoente = int(input("Digite o expoente: "))
result = 1

for i in range(expoente):
  if base == 1:
    result = base
  else:
    result *= base
print(f"Resultado {result}")

"""16. Faça um programa que mostre todos os primos entre 1 e N sendo N um
número inteiro fornecido pelo usuário. O programa deverá mostrar também
o número de divisões que ele executou para encontrar os números primos.
Serão avaliados o funcionamento, o estilo e o número de testes (divisões)
executados.
"""

n = int(input("Digite um numero: "))

for numeroTestado in range(1, n+1):
  for numeroDivisor in range(numeroTestado):
    print(f"{numeroTestado} / {numeroDivisor}= {numeroTestado/numeroDivisor} com o resto)
    if numeroTestado % (numeroDivisor+1) == 0
      if 1 != numeroDivisor+1 != numeroTestado:
        print("nao e primo\n")
        break
      elif numeroDivisor+1 == numeroTestado:
        print("numero [e primo\n]")