import json
import os


caminhoArquivoAnimal = "C:..\\Adoption_Management\\data\\Animais.json"
caminhoArquivoAdocoes = "C:..\\Adoption_Management\\data\\Adocoes.json"
caminhoArquivoVoluntario = "C:..\\Adoption_Management\\data\\Voluntario.json"

idAdocao = 0
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
        global idAdocao
        os.system('cls' if os.name == 'nt' else 'clear')
        mostrar_menuAdocoes()
        escolhaOpcao = int(input('Escolha uma das opções: '))

        match(escolhaOpcao):
            case 1:
                while True:
                        choice = int(input('Deseja adotar um animal?(1-Sim / 2-Não): '))
                        if choice == 1:
                            with open(caminhoArquivoAnimal, 'r') as arquivo:
                                dados = json.load(arquivo)
                                print("\n---Animais para Adoção----\n", json.dumps(dados, indent=4))

                                cpf = input('Insira o seu cpf: ')

                                with open(caminhoArquivoVoluntario,'r') as arquivo:
                                    dados = json.load(arquivo)

                                if cpf not in dados:
                                    print('CPF não encontrado. Cadastre-se primeiro.')
                                    return

                                id = input('Selecione o ID do animal que deseja adotar: ')
                                with open(caminhoArquivoAnimal, 'r') as arquivo:
                                    dadosExistentes = json.load(arquivo)
                                    if id not in dadosExistentes:
                                        print(f'Id {id} não encontrado')
                                        return

                                usuarios = {
                                    'nome': usuarios[cpf]['nome'],
                                    'contato': usuarios[cpf]['contato'],
                                    'email': usuarios[cpf]['email']
                                }
                                animais = {
                                    'nome': animais[id]['nome'],
                                    'idade': animais[id]['idade'],
                                    'tipo': animais[id]['tipo'],
                                    'raça': animais[id]['raça'],
                                    'sexo': animais[id]['sexo']
                                }
                                # Cria registro de adoção
                                adocao = {
                                    'cpf_adotante': cpf,
                                    'id_animal': id,
                                    'dados_usuario': usuarios,
                                    'dados_animal': animais,
                                    'status-adocao': 'Concluída'
                                }

                                # Carrega ou cria arquivo de adoções
                                try:
                                    with open(caminhoArquivoAdocoes, 'r') as arquivo_adocoes:
                                        adocoes = json.load(arquivo_adocoes)
                                except FileNotFoundError:
                                    adocoes = {}

                                    # Determina o próximo ID disponível
                                    if adocoes:
                                        # Pega o maior ID existente e soma 1
                                        proximo_id = max(int(k) for k in adocoes.keys()) + 1
                                    else:
                                        # Primeira adoção
                                        proximo_id = 1

                                    # Adiciona nova adoção com ID numérico sequencial
                                    adocoes[str(proximo_id)] = adocao
                                    print(f'Seu número de Id de adoção é {adocoes[str(proximo_id)]}')

                                # Salva no arquivo
                                with open(caminhoArquivoAdocoes, 'w') as arquivo_adocoes:
                                    json.dump(adocoes, arquivo_adocoes, indent=4)

                                print("\n--- Adoção realizada com sucesso! ---")
                                print(f"Animal: {animais['nome']}")
                                print(f"Adotante: {usuarios['nome']}")
                                print("Detalhes da adoção foram armazenados.")

                        elif choice == 2:
                            print('Voltando ao menu principal...')
                            break

                        else:
                            print('Opção inválida, tente novamente...')
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

