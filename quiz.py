print("Seja muito bem-vindo ao quiz do Raoni!")
answer_user = input("Quer começar? (S/N) ")


if answer_user != "S":
    quit()

score = 0

print("Começando...")
print("Quem desenvolveu o jogo Grand Theft Auto (GTA)? \n (A) Rockstar Games \n (B) Ubisoft \n (C) Activision \n (D) EA \n")
answer_1 = input("Resposta: ")

if answer_1 == "A":
    print("Correct")
else:

    print("Incorreto")
    score = score + 1

print("Qual o nome do protagonista do jogo GTA San Andreas? \n (A) Carlos John \n (B) Carl Johnson \n (C) Carlos Johnson \n ")
answer_2 = input("Resposta: ")

if answer_2 == "B":
    print("Correto") 

else:

     print("Incorreto")

print(f"Quiz acabou... Pontuação: {score}/2 ")