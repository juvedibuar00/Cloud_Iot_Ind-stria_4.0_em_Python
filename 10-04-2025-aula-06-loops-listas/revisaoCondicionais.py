# # # timeCoracao ="Fortaleza"
# # # if timeCoracao == "Fortaleza":
# # # 	print("Torce pelo Laion")


# # # Condicional atraves da entrada do usuario
# # timeCoracao = input("Qual time você torce? ")
# # if timeCoracao == "Fortaleza":
# #     print("Torce pelo Laion")



# # # Condicional composta
# # timeCoracao = "Fortaleza"
# # if timeCoracao == "Fortaleza":
# #     print("Torce pelo Laion")
# # else:
# #     print("Não é um time que eu conheço")


    
# # # Condicional atraves da entrada do usuario
# # timeCoracao = input("Qual time você torce? ")
# # if timeCoracao == "Fortaleza":
# #     print("Torce pelo Laion")
# # else:
# #     print("Não é um time que eu conheço")

# # Condicional composta usando elif

# nota = 5
# if nota >= 9:
#     print("Aprovado")
# elif nota >= 7:
#     print("Recuperação")
# else:
#     print("Reprovado")


# # Condicional composta, entrada pelo usuario
# nota = float(input("Qual a sua nota? "))
# if nota >= 9:
#     print("Aprovado")
# elif nota >= 7:
#     print("Recuperação")
# else:
#     print("Reprovado")


# Tratamento de notas inválidas
# Condicional composta, entrada pelo usuário
nota = float(input("Qual a sua nota? "))

if nota <= 0 or nota > 10:
    print("Erro: Nota inválida. Digite um valor entre 0 e 10.")
elif nota >= 9:
    print("Aprovado")
elif nota >= 7:
    print("Recuperação")
else:
    print("Reprovado")
