import json
import os
import uuid

caminhoArquivoAdocoes = "C:\\Adoption_Management\\data\\Adocoes.json"

if not os.path.exists(caminhoArquivoAdocoes):
    with open(caminhoArquivoAdocoes, 'w') as arquivo:
        json.dump({}, arquivo)

def valor_valido(valor):
    while True:
        if valor == "" or valor == None:
            valor = input('Valor inválido, tente novamente: ')








def mostrar_menuAdocoes():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("╔═════════════════════════════════╗")
    print("║      🏠 MENU DE ADOÇÔES 🐶🐱   ║")
    print("╠═════════════════════════════════╣")
    print("║ [1] 📝 Registrar nova adoção    ║")
    print("║ [2] 📋 Listar todas as adoções  ║")
    print("║ [3] 🔄 Atualiza status de adoção║")
    print("║ [4] 🧠 Adoção inteligente       ║")
    print("║ [5] ❌ Remove registro de adoção║")
    print("║ [0] ↩️ Voltar ao menu principal ║")
    print("╚═════════════════════════════════╝")


def executar_menuAdocoes():
    while True:
        mostrar_menuAdocoes()
        escolhaOpcao = int(input('Escolha uma das opções: '))

        match(escolhaOpcao):
            case 1:
                print('a')
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