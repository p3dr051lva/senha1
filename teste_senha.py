import random

num_sorteado = str(random.randint(10000, 99999))
print (num_sorteado)

print (" Ola bem vindo ao jogo do hacker man, \n \
o objetivo do jogo eh vc adivinhar qual eh a senha que foi sorteada pelo \n computador, voce ira digitar uma senha e o computador ira compara-la com a senha sorteada. Se o digito estiver na senha e na posiçao \n \
correta aparecera +1, se ele estver na senha mas na posiçao errada, aparecera 0, e se nao estiver na senha aparecera -1. \n \
Boa sorte !!!! \n \
*****\n \
=================================")
#estas sao as chances do usuario
chances = 10
while chances > 0:
    x = str(input("digite um numero de 5 casas: "))
    # estas sao as casas da senha informada 
    a = x[0]
    b = x[1]
    c = x[2]
    d = x[3]
    e = x[4]

    # estas sao os valores apresentados pelo programa apos o usuario digitar a sua senha
    r0 = 0
    r1 = 0
    r2 = 0
    r3 = 0
    r4 = 0

    # Se o dígito está contido na senha e está na mesma posição o programa vai apresentar o valor +1
    if a == num_sorteado [0]:
        r0 = +1
    elif a != num_sorteado [0] and a == num_sorteado [2] or a == num_sorteado [3] or a == num_sorteado [4] or a == num_sorteado [1]:
        r0 = 0
    elif a != num_sorteado [0] and a != num_sorteado [2] and a != num_sorteado [3] and a != num_sorteado [4] and a != num_sorteado [1]:
        r0 = -1
    
    if b == num_sorteado [1]:
        r1 = +1
    elif b != num_sorteado [1] and b == num_sorteado [0] or b == num_sorteado [2] or b == num_sorteado [3] or b == num_sorteado [4]:
        r1 = 0
    elif b != num_sorteado [0] and b != num_sorteado [2] and b != num_sorteado [3] and b != num_sorteado [4] and b != num_sorteado [1]:
        r1 = -1


    if c == num_sorteado [2]:
        r2 = +1
    elif c != num_sorteado [4] and c == num_sorteado [1] or c == num_sorteado [0] or c == num_sorteado [3] or c == num_sorteado [2]:
        r2 = 0
    elif c != num_sorteado [0] and c != num_sorteado [2] and c != num_sorteado [3] and c != num_sorteado [4] and c != num_sorteado [1]:
        r2 = -1

        
    if d == num_sorteado [3]:
        r3 = +1
    elif d != num_sorteado [4] and d == num_sorteado [0] or d == num_sorteado [1] or d == num_sorteado [2] or d == num_sorteado [3]:
        r3 = 0
    elif d != num_sorteado [0] and d != num_sorteado [2] and d != num_sorteado [3] and d != num_sorteado [4] and d != num_sorteado [1]:
        r3 = -1


    if e == num_sorteado [4]:
        r4 = +1
    elif e != num_sorteado [0] and e == num_sorteado [3] or e == num_sorteado [2] or e == num_sorteado [1] or e == num_sorteado [4]:
        r4 = 0
    elif e != num_sorteado [0] and e != num_sorteado [2] and e != num_sorteado [3] and e != num_sorteado [4] and e != num_sorteado [1]:
        r4 = -1

    print (r0, r1, r2, r3, r4)
    
    chances -= 1

    if x == num_sorteado:
        chances -= 10
        print("Parabens meu consagrado, voce eh mesmo um hacker man!!!!!")
        

    
    


    
