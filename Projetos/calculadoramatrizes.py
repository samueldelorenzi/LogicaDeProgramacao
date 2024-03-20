#Aluno: Samuel De Lorenzi Ribeiro

#Calculadora de matrizes: as 4 operações executadas em duas matrizes dadas pelo usuário.

#Para soma ser realizada as duas matrizes precisam ter o mesmo tamanho + limitar as matrizes para maior que 2x2
LINHASMATRIZES=0
COLUNASMATRIZES=0

while LINHASMATRIZES<=1 or COLUNASMATRIZES<=1:
    LINHASMATRIZES=int(input("Insira o número de linhas das matrizes: "))
    COLUNASMATRIZES=int(input("Insira o número de colunas das matrizes: "))
    if COLUNASMATRIZES<=1 or LINHASMATRIZES<=1:
        print("\033[1;31mERRO: as matrizes devem ter pelo menos 2x2\033[0m")
        print("") 
print("")
#while usando contadores para declarar a matriz 1
M1=[]
CONTADOR1=0
DISPLAY=1

while CONTADOR1!=LINHASMATRIZES:
    CONTADOR2=0
    LINHASM1=[]
    while CONTADOR2!=COLUNASMATRIZES:
        NUMERO=int(input(f"Insira o {DISPLAY} dígito da matriz 1: "))
        LINHASM1.append(NUMERO)
        DISPLAY+=1
        CONTADOR2+=1
    M1.append(LINHASM1)
    CONTADOR1+=1

#mostra a primeira matriz
print("")
print("\033[1;36mMatriz 1:\033[0m")
for i in M1:
    print(" | ".join(map(str, i)))
print("")

#for usando y e z como variaveis para calcular a matriz 2
M2=[]
DISPLAY=1

for y in range(LINHASMATRIZES):
    LINHASM2=[]
    for z in range(COLUNASMATRIZES):
        NUMERO=int(input(f"Insira o {DISPLAY} dígito da matriz 2: "))
        LINHASM2.append(NUMERO)
        DISPLAY+=1
    M2.append(LINHASM2)

#printa a segunda matriz
print("")
print("\033[1;36mMatriz 2:\033[0m")
for i in M2:
    print(" | ".join(map(str, i)))
print("")

#Operações usando as matrizes

OPERACAO=0
while OPERACAO<1 or OPERACAO>3:
    OPERACAO=int(input("Deseja somar(1), subtrair(2) ou multiplicar(3) as matrizes? "))
    if OPERACAO==1:
        SOMA=[]
        for i in range(LINHASMATRIZES):
            LINHAS=[]
            for j in range(COLUNASMATRIZES):
                CONTA=M1[i][j]+M2[i][j]
                LINHAS.append(CONTA)
            SOMA.append(LINHAS)
        print("")
        print("\033[1;36mSoma:\033[0m")
        for i in SOMA:
            print(" | ".join(map(str, i)))
        print("")

    elif OPERACAO==2:
        SUBTRACAO=[]
        for i in range(LINHASMATRIZES):
            LINHAS=[]
            for j in range(COLUNASMATRIZES):
                CONTA=M1[i][j]-M2[i][j]
                LINHAS.append(CONTA)
            SUBTRACAO.append(LINHAS)
        print("")
        print("\033[1;36mSubtração:\033[0m")
        for i in SUBTRACAO:
            print(" | ".join(map(str, i)))
        print("")
    elif OPERACAO==3:
        MULTIPLICACAO=[]
        CONTADOR=0
        for i in range(LINHASMATRIZES):
            LINHAS=[]
            for j in range(COLUNASMATRIZES):
                CONTA=0
                for CONTADOR in range(COLUNASMATRIZES):
                    CONTA= CONTA + M1[i][CONTADOR]*M2[CONTADOR][j]
                    CONTADOR+=1
                LINHAS.append(CONTA)
            MULTIPLICACAO.append(LINHAS)
        print("")
        print("\033[1;36mMultiplicação:\033[0m")
        for i in MULTIPLICACAO:
            print(" | ".join(map(str, i)))
        print("")
    else:
        print("\033[1;31mERRO: resultados aceitos: 1, 2 ou 3.\033[0m")
        print("")
    AGAIN=input("Deseja fazer outra operação com as mesmas matrizes? (\033[1;32mS\033[0m/\033[1;31mN\033[0m) ")
    AGAIN=AGAIN.lower()
    if AGAIN=="s":
        OPERACAO=0
        print("")
        continue
    else:
        quit()
