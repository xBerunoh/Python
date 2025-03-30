# FAÇA UM PROGRAMA QUE LEIA ALGO PELO TECLADO E MOSTRE NA TELA O SEU TIPO PRIMITIVO E TODAS AS INFORMAÇÕES POSSIVELS
n = (input("Digite algo: "))

print('valor {} é um número inteiro ?',n.isnumeric())
print('valor {} possui letras alfabeticas ?',n.isalpha())
print('valor {} compostas de letras minusculas ?',n.islower())
print('valor {} compostas de letras maiusculas ?',n.isupper())
print('valor {} todas os caracteres da string são decimais ?',n.isdecimal())

