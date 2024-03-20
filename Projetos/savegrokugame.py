import tkinter
import random
from random import randint
from tkinter import Tk, messagebox, simpledialog, ttk

DICA=0
NUMBER=1
CHOICE=0
NUMBER2=1
CHOICE2=0
WIN=0
JAKKUCOMPLET=0
CORUSCANTCOMPLET=0
VITÓRIA=0
FINAL=0


while VITÓRIA==0:
    tkinter.messagebox.showinfo("Save Groku","Bem vindo ao jogo Save Groku.")
    CONFIRMAR=tkinter.messagebox.askyesno(title="Save Groku", message="Você deseja iniciar essa jornada?")
    if CONFIRMAR==True:
        tkinter.messagebox.showinfo("Início","Vamos nessa! Que a força esteja com você.")
        tkinter.messagebox.showwarning("Dica","Abaixe o volume do sistema para 0, caso não queira ser incomodado.")
        tkinter.messagebox.showwarning("Dica","Este jogo funciona com um sistema de placar, ao atingir 2000 pontos, você será vencedor, a cada desafio seus pontos totais serão mostrados.")
        tkinter.messagebox.showinfo("Início","Você é um mandaloriano viajando pelo universo. Seu objetivo é transportar em segurança Groku para que o império não o encontre. Afinal, ele é o último Jedi da galáxia.")
        tkinter.messagebox.showinfo("Início","Vocês se encontram em uma nave, rumo ao outro lado do universo, mesmo com a viagem rápida, você sabe que não será uma missão fácil.")
        GAME=0
        while GAME!=2:
            PLANETA=tkinter.simpledialog.askinteger("Início","Você tem que passar por alguns planetas que estão entre você e seu destino que é a base da resistência, escolha seu primeiro desafio:\n\n1) Jakku \n2) Coruscant")
            if PLANETA==1 and JAKKUCOMPLET==0:
                tkinter.messagebox.showinfo("Jakku","Vocês iniciam sua viagem rumo a Jakku                ")
                tkinter.messagebox.showinfo("Jakku","Jakku apresenta um lugar semelhante a um grande deserto de areia e dunas enormes, sem civilizações, mas ainda com uma pequena parte de habitantes (humanos e outras criaturas), Jakku é um planeta sem leis e inóspito em meio a galáxia.")
                i=0
                while i==0:
                    JAKKU=4
                    while JAKKU>3 or JAKKU<1:
                        JAKKU=tkinter.simpledialog.askinteger("Jakku","Para onde quer ir em Jakku?                           \n\n1) Bar do Ergel\n2) Cratertown\n3) Tuanul ")
                    if JAKKU==1:
                        tkinter.messagebox.showinfo("Bar do Ergel","Bar do Ergel é um bar localizado no planeta, você pede uma gelada e segue seu caminho.")
                        continue
                    if JAKKU==2:
                        tkinter.messagebox.showinfo("Cratertown","Cratertown era uma cidade em Jakku, exatamente, era, você só encontra um lugar deserto onde ficava a antiga cidade.")
                        continue
                    if JAKKU==3:
                        tkinter.messagebox.showinfo("Tuanul","Tuanul é um assentamento em Jakku, localizado na Ravina Kelvin. Era habitada por membros da Igreja da Força, que evitavam a tecnologia moderna e, em vez disso, criaram a sua própria, a fim de se colocarem mais em contato com a natureza.")
                        tkinter.messagebox.showinfo("Tuanul","Você encontra alguns comerciantes que lhe oferecem propostas, a principal delas, comprar o Groku por 20 mil créditos.")
                        CONFIRMAR=tkinter.messagebox.askyesno(title="Tuanul", message="Aceitar proposta?")
                        if CONFIRMAR==True:
                            tkinter.messagebox.showwarning("Banco","Conta bancária: 20.234 créditos.")
                            tkinter.messagebox.showerror(title="Derrota", message="Você realmente vendeu seu protegido?")
                            break
                        else: 
                            tkinter.messagebox.showinfo("Tuanul","Parabéns, por fazer o mínimo.")
                            tkinter.messagebox.showwarning("Tuanul","Você não achou que ia sair barato né? Você não quis vender então eles vão tentar tomar ele de você. Derrote os comerciantes.")
                            while CHOICE != NUMBER:
                                CHOICE=tkinter.simpledialog.askinteger("Duelo","Você deve lutar contra dois comerciantes, um deles te golpeia com um bastão. O que você faz? \n\n1) Esquiva \n2) Defende \n3) Ataca")
                                NUMBER=random.randint(1,3)
                                if CHOICE != NUMBER:
                                    tkinter.messagebox.showerror("Duelo","Movimento errado, tente novamente.")
                                    while DICA==0:
                                        tkinter.messagebox.showwarning("Dica","A opção errada pode não ser a errada da próxima vez.")
                                        DICA=1
                            tkinter.messagebox.showinfo("Duelo","Boa escolha. Porém...")
                            if CHOICE == NUMBER:
                                while CHOICE2 != NUMBER2:
                                    CHOICE2=tkinter.simpledialog.askinteger("Duelo","O segundo comerciante conseguiu te surpreender pelas costas. Para qual lado você desvia? \n\n1) Esquerda \n2) Direita \n3) Baixo")
                                    NUMBER2=random.randint(1,3)
                                    if CHOICE2 != NUMBER2:
                                        tkinter.messagebox.showerror("Duelo","Movimento errado, tente novamente.")
                            WIN=WIN+1000
                            i=1
                            GAME=GAME+1
                            JAKKUCOMPLET=1
                            PONTOSJAKKU=f"Placar total: {WIN}"
                            tkinter.messagebox.showinfo("Duelo","O comerciante não esperava essa esquiva, então ele fica em uma posição vulnerável para tomar um soco, que é o que acontece, o comerciante cai desacordado.")
                            tkinter.messagebox.showinfo("Duelo","Groku bate palmas para você.")
                            tkinter.messagebox.showinfo("Parabéns", PONTOSJAKKU)
                            tkinter.messagebox.showinfo("Continuar", "Você pega Groku em seu colo e o leva de volta a nave, seguindo seu rumo.")
                    
            elif PLANETA==2 and CORUSCANTCOMPLET==0:
                tkinter.messagebox.showinfo("Coruscant","O planeta-cidade Coruscant é o coração pulsante da galáxia, abrigando uma diversidade de cidadãos e culturas. Possui altíssimas torres de edifícios, fluxos de tráfego aéreo cheios de speeders e níveis internos que se estendem muito abaixo da superfície do planeta.")
                i=0
                while i==0:
                    tkinter.messagebox.showinfo("Coruscant","Seu objetivo nesse planeta é mais intelectual, você vai entender mais para frente.")
                    tkinter.messagebox.showinfo("Coruscant","Para conseguir proteger Groku dos perigos, além de braço forte, você vai precisar de um cérebro forte.")
                    tkinter.messagebox.showinfo("Coruscant","Em Coruscant existe os Arquivos Jedai, que concentra os maiores conhecimentos e pesquisas do universo, então vocês partem até lá.")
                    tkinter.messagebox.showinfo("Arquivos Jedi","Chegando, você deixa Groku conhecer os arredores e vai procurar um livro chamado: Como proteger seu Jedi.")
                    LER=0
                    tkinter.messagebox.showinfo("Desafio","Seu objetivo é ler o livro e transcrever suas palavras. Memorize cada uma e escreva-as em ordem, cuidado com a pontuação!")
                    while LER==0:
                        PREPARADO=tkinter.messagebox.askyesno(title="Desafio", message="Preparado?")
                        if PREPARADO==True:
                            tkinter.messagebox.showinfo("Como proteger seu Jedi","Luke,")
                            tkinter.messagebox.showinfo("Como proteger seu Jedi","você descobrirá")
                            tkinter.messagebox.showinfo("Como proteger seu Jedi","que muitas das verdades")
                            tkinter.messagebox.showinfo("Como proteger seu Jedi","às quais nos apegamos")
                            tkinter.messagebox.showinfo("Como proteger seu Jedi","dependem")
                            tkinter.messagebox.showinfo("Como proteger seu Jedi","muito de nosso")
                            tkinter.messagebox.showinfo("Como proteger seu Jedi","próprio ponto")
                            tkinter.messagebox.showinfo("Como proteger seu Jedi","de vista.")
                            FRASE="luke, você descobrirá que muitas das verdades às quais nos apegamos dependem muito de nosso próprio ponto de vista."
                            FRASEUSER=tkinter.simpledialog.askstring("Desafio", "Então, juntando os fragmentos do texto, qual frase é formada?")
                            FRASEUSER=FRASEUSER.lower()
                            if FRASE==FRASEUSER:
                                LER=1
                                tkinter.messagebox.showinfo("Parabéns","Você está aprendendo, mas ainda não é o fim, você deve passar por um quiz para provar seus conhecimentos")
                            else:
                                tkinter.messagebox.showerror("Desafio","Frase errada, tente novamente. Lembre se de cuidar com os pontos e acentos.")
                        else:
                            tkinter.messagebox.showinfo("Desafio","Vou te dar mais um tempo.")
                    COMPLETAR=0
                    while COMPLETAR==0:
                        KENOBI="kenobi"
                        KENOBIUSER=tkinter.simpledialog.askstring("Desafio 2", "Complete o nome:\n\nObi Wan ______.                                                          ")
                        KENOBIUSER=KENOBIUSER.lower()
                        if KENOBI==KENOBIUSER:
                            tkinter.messagebox.showinfo("Parabéns","Siga para o próximo.")
                        else:
                            tkinter.messagebox.showerror("Desafio","Nome errado, tente novamente.")
                        LUKE="skywalker"
                        LUKEUSER=tkinter.simpledialog.askstring("Desafio 2", "Complete o nome:\n\nLuke _________.                                                          ")
                        LUKEUSER=LUKEUSER.lower()
                        if LUKE==LUKEUSER:
                            tkinter.messagebox.showinfo("Parabéns","Siga para o próximo.")
                        else:
                            tkinter.messagebox.showerror("Desafio","Nome errado, tente novamente.")
                        HAN="han"
                        HANUSER=tkinter.simpledialog.askstring("Desafio 2", "Complete o nome:\n\n___ Solo.                                                          ")
                        HANUSER=HANUSER.lower()
                        if HAN==HANUSER:
                            WIN=WIN+1000
                            i=1
                            GAME=GAME+1
                            CORUSCANTCOMPLET=1
                            PONTOSCORUSCANT=f"Placar total: {WIN}"
                            tkinter.messagebox.showinfo("Parabéns", PONTOSCORUSCANT)
                            tkinter.messagebox.showinfo("Continuar", "Agora com muito conhecimento, você está pronto para continuar a missão.")
                            tkinter.messagebox.showinfo("Continuar", "Você procura Groku para partir, após 5 minutos procurando você percebe que ele estava escondido atrás de um livro.")
                            tkinter.messagebox.showinfo("Continuar", "Você pega Groku em seu colo e o leva de volta a nave, seguindo seu rumo.")
                            COMPLETAR=1
                        else:
                            tkinter.messagebox.showerror("Desafio","Nome errado, tente novamente.")
    

        tkinter.messagebox.showwarning("Atenção","Ao sair do planeta você avista uma nave seguindo a sua. Comunicaram sua aparição com Groku nos planetas ao império.")
        tkinter.messagebox.showwarning("Atenção","Você terá que derrotá-los, não há outra opção.")
        tkinter.messagebox.showinfo("Desafio","Precisamos de velocidade, clique o mais rápido possível em todos os OK que aparecerem.")
        for CONTADOR in range (10):
            tkinter.messagebox.showinfo("Desafio","CLIQUE OK"   )
            CONTADOR+=CONTADOR     
        tkinter.messagebox.showinfo("Desafio","Você conseguiu, atingiu a velocidade máxima, isso significa que tem espaço para uma manobra.")
        while FINAL==0:
            MANOBRA=tkinter.simpledialog.askinteger("Desafio","Qual manobra vai ser?                         \n\n1) Subir em looping e cair atrás da nave do império\n2) Mergulhar e ativar a viagem rápida\n3) Ativar o piloto automático e  usar as armas traseiras da nave\n4) Sacrificar Groku e livrar sua pele")
            if MANOBRA==1:
                tkinter.messagebox.showinfo("Final","Você executa a manobra com muita velocidade e cai atrás da nave do império.")
                tkinter.messagebox.showinfo("Final","Você prepara suas armas e abre fogo.")
                tkinter.messagebox.showinfo("Final","A nave do império é obliterada e sai flutando sem controle, como uma sucata no espaço.")
                tkinter.messagebox.showinfo("Final","Groku suspira aliviado e te agradece.")
                tkinter.messagebox.showinfo("Final","Você deixa ele nas mãos da resistência onde sabe que ele será bem cuidado.")
                tkinter.messagebox.showinfo("Final","Você volta a vagar pelo espaço sozinho, como sempre.")
                tkinter.messagebox.showinfo("Parabéns","Parabéns, você terminou o jogo com o final badass.")
                WIN=WIN+1000
                FINALBADASS=f"Placar final: {WIN}"
                tkinter.messagebox.showinfo("Parabéns", FINALBADASS)
                FINAL=1
            elif MANOBRA==2:
                tkinter.messagebox.showinfo("Final","Você executa a manobra com muita velocidade e ativa a viagem rápida.")
                tkinter.messagebox.showinfo("Final","Devido a rapidez, você despista a nave do império, podendo seguir seu caminho.")
                tkinter.messagebox.showinfo("Final","Você e Groku podem seguir a viagem tranquilos até onde a resistência se encontra.")
                tkinter.messagebox.showinfo("Final","Ao chegar lá você entrega na mão deles o último Jedi da galáxia e vai emboora sabendo que cumpriu sua missão.")
                tkinter.messagebox.showinfo("Final","Você volta a vagar pelo espaço sozinho, como sempre.")
                tkinter.messagebox.showinfo("Parabéns","Parabéns, você terminou o jogo com o final covarde.")
                WIN=WIN+500
                FINALCOVARDE=f"Placar final: {WIN}"
                tkinter.messagebox.showinfo("Parabéns", FINALCOVARDE)
                FINAL=1
            elif MANOBRA==3:
                tkinter.messagebox.showinfo("Final","Você ativa o piloto automático e parte para o controle das armas traseiras.")
                tkinter.messagebox.showinfo("Final","Com dois tiros você acerta os dois pilotos da nave do império.")
                tkinter.messagebox.showinfo("Final","A nave perde o controle e vai embora rumo ao infinito e além.")
                tkinter.messagebox.showinfo("Final","Você sente a paz do espaço vazio por alguns segundos, até lembrar que sua missão não está concluída.")
                tkinter.messagebox.showinfo("Final","Ao chegar na base da resistência você deixa seu companheiro de viagem são e salvo, onde ele será bem cuidado.")
                tkinter.messagebox.showinfo("Final","Parabéns você terminou o jogo com o final seguro.")
                WIN=WIN+700
                FINALSEGURO=f"Placar final: {WIN}"
                tkinter.messagebox.showinfo("Parabéns", FINALSEGURO)
                FINAL=1
            else:
                tkinter.messagebox.showinfo("Final","Você ACABOU com toda a missão.")
                tkinter.messagebox.showinfo("Final","O peso da força enfraquecer vai recair sobre você e você será culpado para todo sempre.")
                tkinter.messagebox.showinfo("Final","Você volta a vagar pelo espaço sozinho, como sempre.")
                tkinter.messagebox.showerror("Parabéns","Parabéns, você terminou o jogo com o pior final de todos onde tudo dá errado.")
                WIN=0
                FINALRUIM=f"Placar final: {WIN}"
                tkinter.messagebox.showinfo("Parabéns", FINALRUIM)
                FINAL=1
    else:
        tkinter.messagebox.showerror(title="Até mais", message="Que pena, fica pra próxima :((")
        break    
    
    NOVAMENTE=tkinter.messagebox.askyesno(title="De novo?", message="Deseja jogar novamente?")
    if NOVAMENTE==True:
        continue
    else:
        break
