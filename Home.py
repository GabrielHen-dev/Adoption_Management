def mostrar_menu():
    print("╔══════════════════════════════╗")
    print("║      📋 MENU PRINCIPAL       ║")
    print("╠══════════════════════════════╣")
    print("║ [1] 🐶 Adicionar animais     ║")
    print("║ [2] 👤 Adicionar tutores     ║")
    print("║ [3] 🏠 Adicionar adoções     ║")
    print("║ [0] 🚪 Sair                  ║")
    print("╚══════════════════════════════╝")


def executar_menu():
    while True: #Enquanto a pessoa não sair vai ficar repetindo esse sistema
        mostrar_menu() #Executa o Menu principal
        opcao = int(input("\nDigite a opção desejada: "))

        match (opcao):
            case (1):
                def mostrar_menuAdicionarAnimais():
                    print("╔══════════════════════════════╗")
                    print("║       📋 MENU PRINCIPAL      ║")
                    print("╠══════════════════════════════╣")
                    print("║ [1] 📁 Ver arquivos          ║")
                    print("║ [2] ➕ Adicionar item        ║")
                    print("║ [3] 🖊️ Editar item            ║")
                    print("║ [4] ❌ Remover item          ║")
                    print("║ [5] 🔍 Buscar item           ║")
                    print("║ [0] 🚪 Sair                  ║")
                    print("╚══════════════════════════════╝")


                def executar_menuAdicionarAnimais():
                    while True: #Enquanto a pessoa não sair vai ficar repetindo esse sistema
                        mostrar_menuAdicionarAnimais() #Executa o Menu principal
                        opcao = int(input("\nDigite a opção desejada: "))

                        match (opcao):
                            case (1):

                                print("Salve1")

                            case (2):
                                print("Salve2")


                            case (3):
                                print("Salve3")


                            case (0):
                                print("\nSaindo do sistema... 👋")
                                break

                                    ##sdsdsdsdsd

                executar_menuAdicionarAnimais()
                        

            case (2):
                print("Salve")


                #Coloca o crud aqui!!!



            case (3):
                print("Salve")

                #Coloca o crud aqui!!!



            case (0):
                print("\nSaindo do sistema... 👋")
                break
executar_menu() #Executa os dois 



#Menu de cada CRUD!!!
print("╔══════════════════════════════╗")
print("║       📋 MENU PRINCIPAL      ║")
print("╠══════════════════════════════╣")
print("║ [1] 📁 Ver arquivos          ║")
print("║ [2] ➕ Adicionar item         ║")
print("║ [3] 🖊️ Editar item            ║")
print("║ [4] ❌ Remover item           ║")
print("║ [5] 🔍 Buscar item            ║")
print("║ [0] 🚪 Sair                  ║")
print("╚══════════════════════════════╝")