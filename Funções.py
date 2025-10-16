def criar_sala_cinema(linhas, colunas):
    sala = []   
    contador = 1    #Númeração da cadeira
    corredor = colunas // 2
    for i in range(linhas):     #Gerar linhas da matriz principal
        linha = []
        linha_inferior = []     #Linha inferior ao número dos assentos
        for j in range(colunas):    #Gerar colunas da matriz principal
            if j == corredor:
                 linha.append("|  |".center(0))    
                 linha_inferior.append("|  |".center(0))    
            cadeira = f"{contador:02}"      #Número com 2 dígitos 
            linha.append(cadeira) 
            linha_inferior.append("  ") #Adiciona espaços vazios na linha inferior
            contador += 1
        sala.append(linha)
        sala.append(linha_inferior)
    cadeiras = linhas * colunas
    return sala, cadeiras

def mostrar_sala(sala):
    print("TELA".center(len(sala[0]) * 3 + 1 , "-"))
    for  linha in sala:
        for assentos in linha:
            print(assentos, end=" ")
        print()


#Validação de opção utilizando função
def validacao (opcao_menu, limite):
       while opcao_menu < 1 or opcao_menu > limite:
              print("Opção inválida, tente novamente!")
              opcao_menu = int(input(f"Digite uma opção (1-{limite}): "))
       return opcao_menu


#Atualizar o assento para ocupado
def atualizar_matriz(sala, cadeira):
    encontrou = True
    for i in range(len(sala)):
        for j in range(len(sala[i])):
            if sala[i][j] != "❌":
                if sala[i][j] == cadeira and sala[i + 1][j] != "❌":
                    sala[i + 1][j] = "❌"
                    print("Assento reservado com sucesso!")
                    encontrou = False
                    return True
    if encontrou:
        print("Assento ocupado!")
        return


def validar_idade(opcao_filme, nome_completo, idade):
    catalogo = ["Ednaldo Pereira contra o mundo", "Clash Royale vs Clash of Clans: A batalha final","A múmia"]
    classificacao_filme = [18, 12, 0]

    if opcao_filme == 1 and idade >= classificacao_filme[0]:
        print(f"{nome_completo}\n"
            f"\nSeu acesso para o filme: \033[1m{catalogo[0]}\033[0m foi aprovado!") # Ultilização de código ANSI para deixar texto em negrito
        return True
    elif opcao_filme == 2 and idade >= classificacao_filme[1]:
        print(f"{nome_completo}\n"
            f"\nSeu acesso para o filme: \033[1m{catalogo[1]}\033[0m foi aprovado!") 
        return True
    elif opcao_filme == 3 and idade >= classificacao_filme[2]:
        print(f"{nome_completo}\n"
            f"\nSeu acesso para o filme: \033[1m{catalogo[2]}\033[0m foi aprovado!") 
        return True
    else:
        print("\nA idade não é correspondente com classificação indicativa!")
        return False
    

def reservar_assentos(sessao, cadeiras_sala):
    qntd_ingressos = 0
    escolha = 0
    while escolha != 2:          
        qntd_ingressos = int(input("\nQuantidade de ingressos: "))
        if qntd_ingressos >= 1 and qntd_ingressos <= cadeiras_sala:       
            cont_ingresso = 0
            while cont_ingresso < qntd_ingressos:
                    mostrar_sala(sessao)
                    cadeira = input(f"Número do {cont_ingresso + 1}° assento: ")
                    confirmar = atualizar_matriz(sessao, cadeira)
                    if confirmar:
                            cont_ingresso += 1
            cadeiras_sala -= qntd_ingressos
            mostrar_sala(sessao)
            escolha = int(input("Comprar mais ingressos? (1 - Sim / 2 - Não)"))
            escolha = validacao(escolha, 2)
        else:
            if cadeiras_sala == 0:
                 print("Sala lotada!")
                 return cadeiras_sala
            print(f"\nQuantidade de ingressos inválida!")
            print(f"\nA quantidade de ingressos disponíveis são: {cadeiras_sala}")       
    return cadeiras_sala
