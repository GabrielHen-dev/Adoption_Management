import os
import src.crudAdocoes as crudAdocao
import src.crudadotantes as crudAdotantes
import src.crudAnimal as crudAnimal 

def mostrar_menu():
    os.system('cls' if os.name == 'nt' else 'clear') 
    print("╔══════════════════════════════╗")
    print("║      📋 MENU PRINCIPAL       ║")
    print("╠══════════════════════════════╣")
    print("║ [1] 🐶 Menu animais          ║")
    print("║ [2] 👤 Menu adotantes        ║")
    print("║ [3] 🏠 Menu adoções          ║")
    print("║ [0] 🚪 Sair                  ║")
    print("╚══════════════════════════════╝")


def executar_menu():
    while True: 
        mostrar_menu() 
        opcao = int(input("\n👉 Digite a opção desejada: "))

        match (opcao):
            case (1): 
                crudAnimal.executar_menuAnimais()
                        
            case (2):
                crudAdotantes.executar_menuAdotantes()

            case (3):
                crudAdocao.executar_menuAdocoes()

            case (0):
                print("\nSaindo do sistema... 👋")
                break

executar_menu()