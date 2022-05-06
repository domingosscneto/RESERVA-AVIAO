#Domingos Neto 3203288-9
#João Vitor Lipert 3208887-6
import sys
voos=[["SP",105,'MG',0],['RJ',101,'MG',10],['MG',103,'SP',50],['PR',111,'SP',0],
      ['MG',123,'SP',2],['MG',145,'RJ',20],['PR',109,'MG',10],['PR',199,'RJ',5],
      ['SP',100,'PR',0],['MG',189,'PR',15],['RJ',176,'PR',6],['RJ',177,'SP',7]]
def print_menu():
    print (30* "-" , "MENU" , 30 * "-")
    print ("1. CONSULTAR")
    print ("2. EFETUAR RESERVA")
    print ("3. SAIR")
    print (67 * "-")
def consultar():
    print (30* "-" , "CONSULTAR" , 30 * "-")
    print ("1. POR NUMERO DE VOO")
    print ("2. POR ORIGEM")
    print ("3. POR DESTINO")
    print (67 * "-")
    choice = int(input("Entre sua escolha [1-3]: "))
    if choice==1:   
        print ("Numero de voo selecionado")
        num=int(input('Digite o Numero do Voo: '))
        for i in range (12):
            if num == (voos[i][1]):
                print(voos[i])
    elif choice==2:
        print ("Por origem selecionado")
        orig=str(input('Digite a Origem do Voo: '))
        for i in range(12):
            if orig in (voos[i][0]):
                print(voos[i])     
    elif choice==3:
        print ("Por destino selecionado")
        dest=str(input('Digite o Destino do Voo: '))
        for i in range(12):
            if dest in (voos[i][2]):
                print(voos[i])
def reserva():
    reserv=int(input('Qual Voo Gostaria de Reservar: '))
    for i in range(12):
        if reserv == voos[i][1] and voos[i][3] == 0:
            print('Voo não possui lugares')
            break
        if reserv == voos[i][1]:
            if voos[i][3] > 0:
                print(f'Voo Possui {voos[i][3]} lugares')
                lug=int(input('Digite o Numero De lugares Que Gostaria de reservar: '))
                if lug > voos[i][3]:
                    print('Lugares excedem o límite')
                    break
                elif lug <= voos[i][3]:
                    voos[i][3] -= lug
                    print(f'O Total de {lug} lugares foi reservado')
                    break
    else:
        print('Voo inexistente')
print(voos)
print('NESSE PROGRAMA A ORDEM DOS VETORES SÃO AS SEGUINTES:\n[ORIGEM,NÚMERO DO VOO,DESTINO,LUGARES]')
while True:
    print_menu()
    choice = int(input("Entre sua escolha [1-3]: "))
    if choice==1:   
        print ("Consultar foi selecionado")
        consultar()
    elif choice==2:
        print ("Efetuar reserva foi selecionado")
        reserva()
    elif choice==3:
        sys.exit('Até Mais!!')
        break
        
