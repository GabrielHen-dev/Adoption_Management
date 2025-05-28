import json
import os


caminhoArquivoAdocoes = "C:..\\Adoption_Management\\data\\Adocoes.json"

if not os.path.exists(caminhoArquivoAdocoes):
    with open(caminhoArquivoAdocoes, 'w') as arquivo:
        json.dump({}, arquivo)

def mostrar_menuAdocoes():
    print("╔═════════════════════════════════╗")
    print("║      🏠 MENU DE ADOÇÔES 🐶🐱   ║")
    print("╠═════════════════════════════════╣")
    print("║ [1] 📝 Registrar nova adoção    ║")
    print("║ [2] 📋 Listar todas as adoções  ║")
    print("║ [3] 🔄 Atualizar adoção         ║")
    print("║ [4] 🧠 Adoção inteligente       ║")
    print("║ [5] ❌ Remover adoção           ║")
    print("║ [0] ↩️ Voltar ao menu principal ║")
    print("╚═════════════════════════════════╝")


def executar_menuAdocoes():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        mostrar_menuAdocoes()
        escolhaOpcao = int(input('Escolha uma das opções: '))

        match(escolhaOpcao):
            case 1:
                while True:
                    try:
                        choice = int(input('Deseja adotar um animal?(1-Sim / 2-Não): '))
                        if choice == 1:
                            with open(caminhoArquivoAnimal, 'r') as arquivo:
                                dados = json.load(arquivo)
                                print("\n---Animais para Adoção----\n", json.dumps(dados, indent=4))
                                id = input('Selecione o ID do animal que deseja adotar: ')
                                if id in dados:
                                    nome_animal = dados[id]['nome']
                                    print(f"Nome do usuário: {nome_animal}")
                                else:
                                    print(f"ID {id} não encontrado.")

                        elif choice == 2:
                            print('Voltando ao menu principal...')
                            break

                        else:
                            print('Opção inválida, tente novamente...')
                    except ValueError:
                        print('Insira um valor númerico, tente novamente...')
                        continue
            case 2:
                with open(caminhoArquivoAdocoes, 'r') as arquivo:
                    dados = json.load(arquivo)
                print(dados)
            case 3:
                print('a')
            case 4:
                print('a')
            case 5:
                print('a')
            case 0:
                print('Voltando ao menu principal...')
                break
            case _:
                print('Opção inválida, tente novamente...')

executar_menuAdocoes()