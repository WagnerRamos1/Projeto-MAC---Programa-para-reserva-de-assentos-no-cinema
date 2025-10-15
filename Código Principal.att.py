from datetime import datetime
import Funções
sala_1 = Funções.criar_sala_cinema(6, 6)
sala_2 = Funções.criar_sala_cinema(6, 6)
sala_3 = Funções.criar_sala_cinema(6, 6)
cadeiras_sala1, cadeiras_sala2, cadeiras_sala3 = 36, 36, 36
while True:
       print ("\n-----Bem vindo ao Cine Carajá!-----\n\n"
              "Qual opção deseja realizar?\n\n"
              "1 - Ver catálogo;\n"
              "2 - Sair.\n")

       limite_menu = 2
       #Cada catálogo possuirá um limite, que será pré definido

       opcao_menu = input(f"Digite uma opção: ")
       
       while not opcao_menu.isnumeric():
              print ("Erro: Apenas números são permitidos")
              print ("\n-----Bem vindo ao Cine Carajá!-----\n\n"
                     "Qual opção deseja realizar?\n\n"
                     "1 - Ver catálogo;\n"
                     "2 - Sair.\n")

              opcao_menu = input(f"Digite uma opção: ")
       
       opcao_menu = int (opcao_menu)

       opcao_menu = Funções.validacao(opcao_menu, limite_menu) #Ultilização da função de validação
       
       if opcao_menu == 1:
       
              catalogo = ["Ednaldo Pereira contra o mundo", "Clash Royale vs Clash of Clans: A batalha final","A múmia"] # Catálogo de filmes

              print ("\nCatálogo:\n\n"
                     f"1 - {catalogo[0]}:\n"
                     f"2 - {catalogo[1]}:\n"
                     f"3 - {catalogo[2]}:\n")
              limite_filme = 3

              opcao_filme = input("Digite a opção de filme que deseja realizar reserva: ")
              
              while not opcao_filme.isnumeric():
                     print("Erro: Apenas números são permitidos")
                     print ("\nCatálogo:\n\n"
                     f"1 - {catalogo[0]}:\n"
                     f"2 - {catalogo[1]}:\n"
                     f"3 - {catalogo[2]}:\n")
                     opcao_filme = input("Digite a opção de filme que deseja realizar reserva: ")
              
              opcao_filme = int (opcao_filme)
              Funções.validacao(opcao_filme, limite_filme)

              print ("\nNome e Sobrenome:")
              nome = input("\nNome: ")
              sobrenome = input("Sobrenome: ")
              nome_completo = (f"{nome} {sobrenome}")
              nome_sem_espacos = nome_completo.replace(" ", "")

              #Validação de nome
              while not nome_sem_espacos.isalpha():
                     print ("Erro: Apenas letras são permitidas")
                     nome = input("\nNome: ")
                     sobrenome = input("Sobrenome: ")
                     nome_completo = (f"{nome} {sobrenome}")
                     nome_sem_espacos = nome_completo.replace(" ", "")

              print("\nDigite sua data de nascimento:\n ")
              
              dia = int(input("Dia: "))
              mes = int(input("Mês: "))
              ano = int(input("Ano: "))

              #Calculo de idade baseado na data atual
              data_nascimento = datetime(ano, mes, dia)
              data_atual = datetime.now()

              idade = data_atual.year - data_nascimento.year

              if (data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day):
                     idade -= 1
              
              #Validação de idade
              while idade < 0 or idade >= 150:
                     print ("Idade inválida, digite novamente!")

                     print("\nDigite sua data de nascimento: ")
                     dia = int(input("\nDia: "))
                     mes = int(input("Mês: "))
                     ano = int(input("Ano: "))
                     
                     # recalcula a idade caso ele digite uma idade inválida
                     data_nascimento = datetime(ano, mes, dia)
                     data_atual = datetime.now()

                     idade = data_atual.year - data_nascimento.year
                     if (data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day):
                        idade -= 1
                     #Adiconar linha do cálculo
              
              acessoliberado = Funções.validar_idade(opcao_filme, nome_completo, idade)
              
              if not acessoliberado:
                     print("Retornando ao menu principal...\n")
                     continue  # Volta para o menu principal

              if opcao_filme == 1:
                     cadeiras_sala1 = Funções.reservar_assentos(sala_1, cadeiras_sala1)
              elif opcao_filme == 2:
                     cadeiras_sala2 = Funções.reservar_assentos(sala_2, cadeiras_sala2)
              elif opcao_filme == 3:
                     cadeiras_sala3 = Funções.reservar_assentos(sala_3, cadeiras_sala3)

       #Finalização do programa
       if opcao_menu == 2:
              print("Programa Encerrado!")
              break