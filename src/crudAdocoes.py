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
    print("║ [0] ↩️ Voltar ao menu principal  ║")
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
        global logado
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
            case 2:
                while True:
                        if logado == True:
                            choice = int(input('Registrar adoção, confirma?(1-Sim / 2-Não): '))
                            if choice == 1:
                                try:
                                    with open(caminhoArquivoAnimal, 'r') as arquivo:
                                        dadosexistentes = json.load(arquivo)
                                        print("\n---Animais para Adoção----\n", json.dumps(dadosexistentes, indent=4))

                                        cpf = input('Insira o seu cpf: ')

                                        with open(caminhoArquivoadotantes, 'r') as arquivo:
                                            dados = json.load(arquivo)


                                        if cpf not in dados:
                                            print('CPF não encontrado ou dados estão incorretos.')
                                            break

                                        id_animal = input('Selecione o ID do animal que deseja adotar: ')
                                        with open(caminhoArquivoAnimal, 'r') as arquivo:
                                            dadosExistentes = json.load(arquivo)
                                            if id_animal not in dadosExistentes:
                                                print(f'Id {id_animal} não encontrado')
                                                break

                                        animal_disponivel = True
                                        with open(caminhoArquivoAdocoes, 'r') as arquivo:
                                            adocoes = json.load(arquivo)
                                            for adocao in adocoes.values():
                                                if adocao["id_animal"] == id_animal:
                                                    print('O animal não está disponível para adoção')
                                                    animal_disponivel = False
                                                    break

                                        if not animal_disponivel:
                                            break

                                        usuarios = {
                                            "nome": dados[cpf]["nome"],
                                            "contato": dados[cpf]["contato"],
                                            "email": dados[cpf]["email"]
                                        }

                                        animais = {
                                            "nome": dadosExistentes[id_animal]["Nome"],
                                            "idade": dadosExistentes[id_animal]["Idade"],
                                            "tipo": dadosExistentes[id_animal]["Tipo"],
                                            "raça": dadosExistentes[id_animal]["Raca"],
                                            "sexo": dadosExistentes[id_animal]["Sexo"]
                                        }


                                        adocao = {
                                            "cpf_adotante": cpf,
                                            "id_animal": id_animal,
                                            "dados_usuario": usuarios,
                                            "dados_animal": animais,
                                            "status-adocao": "Concluída"
                                        }


                                        try:
                                            with open(caminhoArquivoAdocoes, 'r') as arquivo:
                                                adocoes = json.load(arquivo)
                                        except (FileNotFoundError, json.JSONDecodeError):
                                            adocoes = {}


                                        if adocoes:
                                            proximo_id = max(int(k) for k in adocoes.keys()) + 1
                                        else:
                                            proximo_id = 1

                                        adocoes[str(proximo_id)] = adocao

                                        with open(caminhoArquivoAdocoes, 'w') as arquivo:
                                            json.dump(adocoes, arquivo, indent=4)

                                        print("\n--- Adoção realizada com sucesso! ---")
                                        print(f'Seu número de Id de adoção é {proximo_id}')
                                        print(f"Animal: {animais["nome"]}")
                                        print(f"Adotante: {usuarios["nome"]}")
                                        print("Detalhes da adoção foram armazenados.")
                                        break
                                except Exception as e:
                                    print(f'Ocorreu um erro: {str(e)}')

                            elif choice == 2:
                                print('Voltando ao menu principal...')
                                break

                            else:
                                print('Opção inválida, tente novamente...')
                        else:
                            print('Você não está logado, realize o login. Voltando ao menu...')
                            break
            case 3:
                if logado == True:
                    with open(caminhoArquivoAdocoes, 'r') as arquivo:
                        dados = json.load(arquivo)
                        print("\n---Adoções registradas----\n", json.dumps(dados, indent=4))
                else:
                    print('Você não está logado, realize o login')
                    print('Voltando ao menu...')

            case 4:
                if logado == True:
                    id = input('Insira o ID da adoção: ')
                    with open(caminhoArquivoAdocoes, 'r') as arquivo:
                        adocoes = json.load(arquivo)
                    if id in adocoes:
                        adocoes[id]['status-adocao'] = input('Insira o status da adoção: ')
                        print('Salvando alteração...')
                        with open(caminhoArquivoAdocoes, 'w') as arquivo:
                            json.dump(adocoes, arquivo, indent=4)
                    else:
                        print('ID não encontrado, tente novamente...')
                else:
                    print('Você não está logado, realize o login')
            case 5:
                cpf = input('Digite o seu cpf: ')
                with open(caminhoArquivoadotantes, 'r') as arquivo:
                    dados = json.load(arquivo)
                if cpf not in dados:
                    print('CPF não encontrado ou dados estão incorretos.')
                    break
                preferencias = dados[cpf]['preferencias']
                print("-" * 30)
                print("Suas preferências:")
                print(f"Tipo: {preferencias['tipo']}")
                print(f"Porte: {preferencias['porte']}")
                print(f"Sexo: {preferencias['sexo']}")
                print("-" * 30)

                with open(caminhoArquivoAnimal, 'r') as arquivo:
                    dadosExistentes = json.load(arquivo)


                for id_animal, info in dadosExistentes.items():
                    nome = info.get("Nome", "Não informado")
                    tipo = info.get("Tipo") or info.get("especie", "Não informado")
                    porte = info.get("Porte", "Não informado")
                    sexo = info.get("Sexo", "Não informado")

                    if (preferencias['tipo'] == tipo and preferencias['porte'] == porte and preferencias['sexo'] == sexo):
                                print('O animal ideal para você:')
                                print(f"Animal ID: {id_animal}")
                                print(f"Nome: {nome}")
                                print(f"Tipo/Espécie: {tipo}")
                                print(f"Porte: {porte}")
                                print(f"Sexo: {sexo}")
                                print("-" * 30)

            case 6:
                if logado == True:
                    id = input('Insira o ID da adoção: ')
                    with open(caminhoArquivoAdocoes, 'r') as arquivo:
                        adocoes = json.load(arquivo)
                    if id in adocoes:
                        adocoes.pop(id)
                        with open(caminhoArquivoAdocoes, 'w') as arquivo:
                            json.dump(adocoes, arquivo, indent=4)
                        print('Apagando adocao, voltando ao menu...')
                    else:
                        print('Não há nenhum ID associado, voltando ao menu...')
                else:
                    print('Você não está logado, realize o login')

            case 0:
                print('Voltando ao menu principal...')
                break
            case _:
                print('Opção inválida, tente novamente...')

