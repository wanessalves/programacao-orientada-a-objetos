print ("Advinhação")

numero_secreto = 15

chute = input("Digite seu chute: ")
chute_inteiro = int(chute)
print("Seu chute eh: ", chute)

print(type(numero_secreto))
print(type(chute))

if(numero_secreto == chute_inteiro):
    print("Você acertou")
elif(chute_inteiro < numero_secreto):
	print("Chute mais alto que:", chute_inteiro)
elif(chute_inteiro > numero_secreto):
	print("Chute mais baixo que:", chute_inteiro)	
else:
    print("erro")    
