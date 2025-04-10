nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))

media = (nota1 + nota2)/2
print(media)
if media > 6:
    print("Aprovado (a)")
elif media == 6:
    print("Recuparação")
else:
    print("Reprovado!")
