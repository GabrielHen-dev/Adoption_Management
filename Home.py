import os
import src.crudAnimal as crudAnimal # importa os cruds

def mostrar_menu():
    os.system('cls' if os.name == 'nt' else 'clear') # Limpa o terminal, para não ficar bagunçado!
    print("╔══════════════════════════════╗")
    print("║      📋 MENU PRINCIPAL       ║")
    print("╠══════════════════════════════╣")
    print("║ [1] 🐶 Menu animais          ║")
    print("║ [2] 👤 Menu usuarios         ║")
    print("║ [3] 🏠 Menu adoções          ║")
    print("║ [0] 🚪 Sair                  ║")
    print("╚══════════════════════════════╝")


def executar_menu():
    while True: #Enquanto a pessoa não sair vai ficar repetindo esse sistema
        mostrar_menu() #Executa o Menu principal
        opcao = int(input("\n👉 Digite a opção desejada: "))

        match (opcao):
            case (1): 
                # ─────────────── 🐾 CRUD DE ANIMAIS ───────────────
                crudAnimal.executar_menuAnimais()
                        
            case (2):
                print("salve")


                #Coloca o crud aqui!!!



            case (3):
                print("Salve")

                #Coloca o crud aqui!!!



            case (0):
                print("\nSaindo do sistema... 👋")
                break
            
executar_menu() #Executa os dois 

"""
def mostrar_menuUsuarios():
    print("╔═════════════════════════════════╗")
    print("║     👤 CENTRAL DOS ADOTANTES     ║")
    print("╠═════════════════════════════════╣")
    print("║ [1] 🔍 Ver lista de usuários     ║")
    print("║ [2] 📝 Cadastrar novo usuário    ║")
    print("║ [3] ✏️ Editar um cadastro        ║")
    print("║ [4] ❌ Remover um usuário        ║")
    print("║ [0] 🔙 Voltar ao menu principal ║")
    print("╚═════════════════════════════════╝")

def mostrar_menuAdocoes():
    print("╔═════════════════════════════════╗")
    print("║     🏡 PAINEL DE ADOÇÕES         ║")
    print("╠═════════════════════════════════╣")
    print("║ [1] 📄 Ver todas as adoções      ║")
    print("║ [2] ➕ Registrar nova adoção      ║")
    print("║ [3] 🔄 Atualizar adoção           ║")
    print("║ [4] ❌ Cancelar adoção            ║")
    print("║ [0] 🔙 Voltar ao menu principal ║")
    print("╚═════════════════════════════════╝")

"""