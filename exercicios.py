#Interios
#print(6/4)
#print(6//4)
#print(6%4)

#String
#nome = " Cezar tamer "
#print(nome.upper())
#print(nome.strip())
#print(nome.lower())
#print(nome.strip().split(" "))

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
##1num1 = int(input("Primeiro numero a ser somado: "))
##1num2 = int(input("Segundo numero a ser somando: "))
##1soma = num1 + num2
##1print(f"A soma é {soma}")
# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
##2num1 = int(input("Primeiro numero: "))
##2resto = num1 % 5
##2print(f"O resto é {resto}")
# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
##3num1 = int(input("Primeiro numero a ser multiplicado: "))
##3num2 = int(input("Segundo numero a ser multiplicado: "))
##3mult = num1 * num2
##3print(f"A multiplicado é {mult}")
# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
##4num1 = int(input("Numero a ser dividido: "))
##4num2 = int(input("Divisor: "))
##4div = num1 // num2
##4print(f"Oresultado da divisão é {div}")
# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
##5num1 = int(input("Numero: "))
##5num2 = 2
##5quad = num1 ** num2
##5print(f"O quadrado do numero {num1} é {quad}")


# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
##6num1 = float(input("Primeiro numero a ser somado: "))
##6num2 = float(input("Segundo numero a ser somando: "))
##6soma = num1 + num2
##6print(f"A soma é {soma}")
# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
##7num1 = float(input("Primeiro numero a ser somado: "))
##7num2 = float(input("Segundo numero a ser somando: "))
##7div = 2
##7media = (num1 + num2) / div
##7print(f"A média é {media}")
# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
##8num1 = float(input("Base: "))
##8num2 = float(input("Potência: "))
##8pot = num1 ** num2
##8print(f"A potencia do número {num1} é {pot}")
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
##9celsius = float(input("Digite os graus Celsius para conversão: "))
##9fahrenheits = (celsius *9/5) + 32
##9print(f"O resultado da conversão para Fahrenheits é {fahrenheits}")
# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
##10pi = 3.14
##10r = float(input("Digite o raio do círculo: "))
##10result =  pi * r ** 2
##10print(f"O resultado da área do círculo é {result}")

# #### String (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
#string = input("Insira algo: ")
#print(string.upper())
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
#string = input("Insira seu nome: ")
#print(string.lower())
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
#string = input("Insira uma frase: ")
#print(string.strip())
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
#string = input("Insira uma data no formato dd/mm/aaaa: ")
#string = string.split("/")
#print(f"dia {string[0]} e mês {string[1]}")
# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
#string1 = input("Insira uma frase: ")
#string2 = input("Insira outra frase: ")
#print(string1 + " " + string2)

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# num1 = True
# num2 = False
# resultado = (num1 and num2)
# print(resultado)
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# num1 = True
# num2 = False
# resultado = (num1 or num2)
# print(resultado)
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# num1 = True
# resultado = not num1 
# print(resultado)
# 19. Faça um programa que compare se dois números fornecidos pelo usuário se forem são iguais.
# num1 = 2
# num2 = 2
# resultado = (num1 == num2)
# print(resultado)

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
# num1 = 2
# num2 = 1
# resultado = (num1 != num2)
# print(resultado)


# #### try-except e if

# 21: Conversor de Temperatura

# temp = float(input("Digite a temperatura para conversão: "))
# fouc = str(input("Deseja a sua temperatura em F ou C?(Digite C ou F)"))
# if fouc == 'F':
#     result = (temp *9/5) + 32
# else:
#     result = (temp - 32)/(9/5)

# print(f"O resultado da conversão para {fouc} é {result}")

# # 22: Verificador de Palíndromo
# try:
#     palin = input("Digite a temperatura para conversão: ")
#     palin_reverso = palin[::-1]
#     if palin == palin_reverso:
#         print("É um palindromo!")
#     else : 
#         print("Não é um palindromo!")
# except:
#     print("Valor imputado não pode ser verificado, insira uma string.")

# 23: Calculadora Simples
# try:
#     num1 = float(input("Digite o número: "))
#     num2 = float(input("Digite o segundo número: "))
#     tipo = input("Digite o perador (+,-,*,/): ")
#     if tipo == '*':
#        resultado = num1 * num2   
#     elif tipo == '/':
#         resultado = num1 / num2 
#     elif tipo == '+':
#         resultado = num1 + num2 
#     elif tipo == '-':        
#         resultado = num1 - num2
#     else:
#         raise ValueError('Valor imputado não pode ser verificado, insira uma string.')
#     print(resultado)
# except ValueError:
#     print("Valor imputado não pode ser verificado, insira uma string.")

# 24: Classificador de Números
# try:
#     num = int(input("Digite um número: "))
#     if num > 0:
#         print("positivo")
#     elif num < 0:
#         print("Negativo")
#     else:
#         print("Zero")
#     if num %2 ==0:
#         print("Par")
#     else: 
#         print("Ímpar")
    

# except ValueError:
#     print("Por favor, digitar um valor válido!")

# 25: Conversão de Tipo com Validação
lista = '1,2,3,4,5' #input("Digite uma lista de numeros separados por ,:")
lista_separada = lista.strip(",")
numeros_int = []


for num in lista_separada:
    if isinstance(num, int):
        numeros_int.append(int(num.strip()))
print(f"Lista de numeros inteiros: {numeros_int}")
    # except ValueError:
    #     print("Por favor, digitar um valor válido!")
