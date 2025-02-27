"""
Programa: eq_linear
Descrição: Este programa resolve uma equação linear com termos à escolha do usuário
Autor: Filipe Eich
Data: 27/02/2025
Versao: 0.0.1
"""

#Alocaçao de memoria

a=""
x=""
b=""


#Entrada de dados

a = float(input("\nOlá! Vamos achar o valor de X em uma equação linear? Considere o formato a.x = b , Qual valor de a?: "))
b = float(input("\nAgora, me diga o valor para b: "))

# Processamento de dados
x=(b/a)


#Saida de dados

print(f"\nAqui está o valor do X: {x}")
