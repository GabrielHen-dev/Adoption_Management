import json
import os


caminhoArquivoAnimal = "C:..\\Adoption_Management\\data\\Animais.json"
caminhoArquivoAdocoes = "C:..\\Adoption_Management\\data\\Adocoes.json"
caminhoArquivoadotantes = "C:..\\Adoption_Management\\data\\Adotantes.json"

idAdocao = 0
logado = False

if not os.path.exists(caminhoArquivoAdocoes):
    with open(caminhoArquivoAdocoes, 'w') as arquivo:
        json.dump({}, arquivo)

def mostrar_menuAdocoes():
    print("╔═════════════════════════════════╗")
    print("║       🐱 MENU DE ADOCOES 🐶     ║")
    print("╠═════════════════════════════════╣")
    print("║ [1] 🏠 Fazer Login              ║")
    print("║ [2] 📝 Registrar adoção         ║")
    print("║ [3] 📋 Listar todas as adoções  ║")
    print("║ [4] 🔄 Atualizar adoção         ║")
    print("║ [5] 🧠 Adoção inteligente       ║")
    print("║ [6] ❌ Remover adoção           ║")
    print("║ [0] ↩️ Voltar ao menu principal ║")
    print("╚═════════════════════════════════╝")

def login_usuario():
    while True:
        global logado
        with open(caminhoArquivoadotantes, 'r') as arquivo:
            try:
                dadosexistentes = json.load(arquivo)
            except json.JSONDecodeError:
                dadosexistentes = {}

        print('=======Login=======')
        cpf = input('Insira seu CPF --> ')
        senha = input('Insira sua senha --> ')

        if cpf in dadosexistentes:

            if senha == dadosexistentes[cpf]['senha']:
                print('Login realizado...')
                logado = True
                break

            else:
                print('Senha Incorreta, tente novamente...')
                logado = False

        else:
            print('- Usuário não cadastrado, tente novamente...')
        continuar = input('\n🔙 Pressione enter para continuar.')


def executar_menuAdocoes():
    while True:
        global idAdocao
        os.system('cls' if os.name == 'nt' else 'clear')
        mostrar_menuAdocoes()
        escolhaOpcao = int(input('Escolha uma das opções: '))

        try:
            escolhaOpcao = int(escolhaOpcao)
        except ValueError:
            print('Por favor, digite um número válido.')
            continue

        match(escolhaOpcao):
            case 1:
                if logado == False:
                    login_usuario()
                else:
                    print('Você já está logado, voltando ao menu...')
                    break
            case 2:
                while True:
                        if logado == False:
                            print('Você não está logado, realize o login')
                            print('Voltando ao menu...')
                            break
                        choice = int(input('Registrar adoção, confirma?(1-Sim / 2-Não): '))
                        if choice == 1:
                            try:
                                with open(caminhoArquivoAnimal, 'r') as arquivo:
                                    dadosexistentes = json.load(arquivo)
                                    print("\n---Animais para Adoção----\n", json.dumps(dados, indent=4))

                                    cpf = input('Insira o seu cpf: ')

                                    with open(caminhoArquivoadotantes,'r') as arquivo:
                                        dadosexistentes = json.load(arquivo)

                                    if cpf not in dados:
                                        print('CPF não encontrado ou dados estão incorretos.')
                                        break

                                    id = input('Selecione o ID do animal que deseja adotar: ')
                                    with open(caminhoArquivoAnimal, 'r') as arquivo:
                                        dadosExistentes = json.load(arquivo)
                                        if id not in dadosExistentes:
                                            print(f'Id {id} não encontrado')
                                            break

                                    with open(caminhoArquivoAdocoes, 'r') as arquivo:
                                        adocoes = json.load(arquivo)
                                        if id in adocoes:
                                            print('O animal não está disponível para adoção')
                                            break

                                    usuarios = {
                                        'nome': dadosexistentes[cpf]['nome'],
                                        'contato': dadosexistentes[cpf]['contato'],
                                        'email': dadosexistentes[cpf]['email']
                                    }
                                    animais = {
                                        'nome': dadosExistentes[id]['nome'],
                                        'idade': dadosExistentes[id]['idade'],
                                        'tipo': dadosExistentes[id]['tipo'],
                                        'raça': dadosExistentes[id]['raça'],
                                        'sexo': dadosExistentes[id]['sexo']
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
                                        with open(caminhoArquivoAdocoes, 'r') as arquivo:
                                            adocoes = json.load(arquivo)
                                    except (FileNotFoundError, json.JSONDecodeError):
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
                                    with open(caminhoArquivoAdocoes, 'w') as arquivo:
                                        json.dump(adocoes, arquivo, indent=4)

                                    print("\n--- Adoção realizada com sucesso! ---")
                                    print(f"Animal: {animais['nome']}")
                                    print(f"Adotante: {usuarios['nome']}")
                                    print("Detalhes da adoção foram armazenados.")
                            except Exception as e:
                                print(f'Ocorreu um erro: {str(e)}')

                        elif choice == 2:
                            print('Voltando ao menu principal...')
                            break

                        else:
                            print('Opção inválida, tente novamente...')
            case 3:
                if logado == False:
                    print('Você não está logado, realize o login')
                    print('Voltando ao menu...')
                    break
                with open(caminhoArquivoAdocoes, 'r') as arquivo:
                    dados = json.load(arquivo)
                    print("\n---Adoções registradas----\n", json.dumps(dados, indent=4))
            case 4:
                if logado == False:
                    print('Você não está logado, realize o login')
                    print('Voltando ao menu...')
                    break
                id = input('Digite o seu Id: ')
                if id in adocoes:
                    adocoes[id]['status-adocao'] = input('Insira o status da adoção: ')
            case 5:
                if logado == False:
                    print('Você não está logado, realize o login')
                    print('Voltando ao menu...')
                    break
            case 6:
                if logado == False:
                    print('Você não está logado, realize o login')
                    print('Voltando ao menu...')
                    break
            case 0:
                print('Voltando ao menu principal...')
                break
            case _:
                print('Opção inválida, tente novamente...')

