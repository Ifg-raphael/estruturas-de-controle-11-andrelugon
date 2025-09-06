#Programa recebe três valores, verifica se esses valores formam um triângulo e classifica-o como equilátero, isósceles e escaleno:

## Entrada de dados: o usuário fornece os valores a,b,c 
a = int(input("Forneça o valor de a: "))
b = int(input("Forneça o valor de b: "))
c = int(input("Forneça o valor de c: "))

#Estrutura condicional: Verifica se os valores informados formam ou não um triângulo
if (a < b + c) and (b < a + c) and (c < b + a):

    #Estrutura condicional: Verifica o tipo de triângulo formado
    if (a == b) and (b == c):
        print('equilátero')   #Saída de dados: informa que o triângulo é do tipo equilátero
    elif (a == b) or (a == c) or (b == c):
        print('isósceles')    #Saída de dados: informa que o triângulo é do tipo isósceles
    else:
        print('escaleno')     #Saída de dados: informa que o triângulo é do tipo escaleno
else:
    print(f"Não forma triângulo: {a}, {b}, {c}") #Saída de dados: informa que os valores não formam triângulo