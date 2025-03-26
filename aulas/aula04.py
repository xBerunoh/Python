#TIPOS DE DADOS DO PYTHON
x=1
nome="Bruno Eduardo"
decimal=3.14
a=False
b=True
# Numeros complexos
n1=5;n2=2;x2=complex(n1,n2) 
# Coleçoes
lista=["carro","avião","navio","moto",1,True,4.1551] # List <Array>
lista[0] = "onibus"
exm=("cachorro","papagaio","gato","tucano",4,44.1551) #Tuple
# exm[0] = "dasdsa" Não permite eu alterar os indices

u=range(0,100) # criou uma lista de 0 a 100
dicionario={ #Dicionario
    "nome":"Bruno Eduardo",
    "idade":"23",
    "curso":"Ciência da computação",
    "cidade":"Manaus"
}

xa={6,5,4,7,9,7} #Set
xb=frozenset({4,5,6,7,8,9}) #frozenSet
# TIPOS - VALOR
print("Valor "+str(x))
print("TIpo "+str(type(x)))
print("Valor "+str(nome))
print("TIpo "+str(type(nome)))
print("Valor "+str(decimal))
print("TIpo "+str(type(decimal)))
print("Valor "+str(a))
print("TIpo "+str(type(a)))
print("Valor "+str(b))
print("TIpo "+str(type(b)))
print(x2.real) # numero real
print(x2.imag) # numero imaginario
print("Valor:"+lista[0])
print("Valor:"+exm[0])
print(dicionario["nome"])
print(dicionario["idade"])
print("TIpo "+str(type(dicionario)))
print("Valor"+str(xa)) # Não repete Valores
print("TIpo "+str(type(xa)))
print("Valor"+str(xb)) # FrozenSet ele congela
print("TIpo "+str(type(xb)))
