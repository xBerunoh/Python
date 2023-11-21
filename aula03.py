#ESCOPO DE VARIAVEIS 
num1=0
num2=0
res=0
#Variaveis Globais

curso="Ciência da computação"
#Função para exemplificar Variaveis Globais.
def cn():
    print(curso)


cn()

def exemplo():
    curso2="Economia"
    print(curso2)

exemplo()

#print(curso2)  Não vai funcionar, pois a variavel está sendo declarada dentro de uma função, ela fica especifica de uma função
