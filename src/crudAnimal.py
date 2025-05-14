import json 
import os  
import uuid # Gera id all

caminhoArquivoAnimal = "C:..\\Adoption_Management\\data\\Animais.json" # Alterar isso para o crud que for ser feito

if not os.path.exists(caminhoArquivoAnimal):
    with open(caminhoArquivoAnimal, 'w') as arquivo: # Vai verificar se existe ou não o animal.json, se não houver ele cria!
        json.dump({}, arquivo)


def mostrar_menuAnimais():
    os.system('cls' if os.name == 'nt' else 'clear') # Limpa o terminal, para não ficar bagunçado!
    print("╔═════════════════════════════════╗")
    print("║      🐾 MENU DOS ANIMAIS        ║")
    print("╠═════════════════════════════════╣")
    print("║ [1] 🐶 Ver todos os animais     ║")
    print("║ [2] 🐱 Cadastrar novo animal    ║")
    print("║ [3] 🐰 Editar informações       ║")
    print("║ [4] 🐢 Remover do sistema       ║")
    print("║ [0] 🔙 Voltar ao menu principal ║")
    print("╚═════════════════════════════════╝")



def executar_menuAnimais():
    while True: #Enquanto a pessoa não sair vai ficar repetindo esse sistema
        mostrar_menuAnimais() #Executa o Menu Animais
        opcao = int(input("\n👉 Digite a opção desejada: "))
  
        match (opcao):
            case (1):
                    with open(caminhoArquivoAnimal, 'r') as arquivo: # ler e exibe os dados no terminal
                        dados = json.load(arquivo)
                        print("\n", "Animais Cadastrados: ", "\n", json.dumps(dados, indent=4))
                    continuar = input("\nPrecione Enter para continuar")

            case (2):
                def obterInputValido(mensagem, tipo=str):
                    while True:
                        entrada = input(mensagem).strip()

                        if entrada == "" or entrada == None:
                            print("\n❌ Este campo é obrigatório. Por favor, preencha.")
                            continue

                        if tipo == int:
                            if entrada.isdigit():
                                return int(entrada)
                            else:
                                print("\n❌ Digite um número válido.")
                                continue    
                        return entrada
                    
                def novoAnimal(): # Função para criar novo animal
                    ID = uuid.uuid4() # Importa o uuid, onde ele cria um id único para cada animal!
                    nome = obterInputValido("\n📛 Nome do animal: ")
                    idade = obterInputValido("🎂 Idade (em anos): ", tipo=int)
                    tipo = obterInputValido("🐾 Espécie (ex: cachorro, gato): ")
                    raca = obterInputValido("🧬 Raça: ")
                    porte = obterInputValido("📏 Porte (pequeno, médio, grande): ")
                    sexo = obterInputValido("⚧️ Sexo (macho/fêmea): ")
                    vacinado = obterInputValido("💉 Está vacinado? (s/n): ")
                    descricao = input("📝 Descreva o comportamento ou histórico (opcional): ")
                    
                    return {
                        f'{ID}': {
                            'Nome': f'{nome}',
                            'Idade': f'{idade}',
                            'Tipo': f'{tipo}',
                            'Raca': f'{raca}',
                            'Porte': f'{porte}',
                            'Sexo': f'{sexo}',
                            'Vacinado': f'{vacinado}',
                            'Descricao': f'{descricao}'
                        }
                    }

                with open(caminhoArquivoAnimal, 'r') as arquivo: # Aqui ele vai ler o arquivo
                    try: 
                        dadosExistentes = json.load(arquivo) 
                    except json.JSONDecodeError: # Caso o arquivo estiver em branco, corrompido ou em formato errado ele vai definir como vazio
                        dadosExistentes = {}
                    novo_animal = novoAnimal() 
                    dadosExistentes.update(novo_animal) # Adicionando os novos animais nos dados já existentes
                with open(caminhoArquivoAnimal, 'w') as arquivo:
                    json.dump(dadosExistentes, arquivo, indent=4) # Ele reescreve o arquivo com novos dados! 
                print("\n✅ Animal cadastrado com sucesso!\n")
                continuar = input("\n🔙 Pressione Enter para continuar...")

            case (3):
                def alterarAnimal(): # Função para alterar animal
                    def obterInputValido(mensagem, tipo=str): # validação input == null, verifica para não mandar em branco para o banco
                        while True:
                            entrada = input(mensagem).strip()

                            if entrada == "" or entrada == None:
                                print("\n❌ Este campo é obrigatório. Por favor, preencha.")
                                continue

                            if tipo == int:
                                if entrada.isdigit():
                                    return int(entrada)
                                else:
                                    print("\n❌ Digite um número válido.")
                                    continue    
                            return entrada
                    ID = obterInputValido("\n🆔 Digite o ID do animal que deseja alterar: ") # Fazer verificação do id no banco de dados @JP   
                    nome = obterInputValido("\n📛 Nome do animal: ")
                    idade = obterInputValido("🎂 Idade (em anos): ")
                    tipo = obterInputValido("🐾 Espécie (ex: cachorro, gato): ")
                    raca = obterInputValido("🧬 Raça: ")
                    porte = obterInputValido("📏 Porte (pequeno, médio, grande): ")
                    sexo = obterInputValido("⚧️ Sexo (macho/fêmea): ")
                    vacinado = obterInputValido("💉 Está vacinado? (s/n): ")
                    descricao = input("📝 Descreva o comportamento ou histórico (opcional): ")
                    return {
                        f'{ID}': {
                            'Nome': f'{nome}',
                            'Idade': f'{idade}',
                            'Tipo': f'{tipo}',
                            'Raca': f'{raca}',
                            'Porte': f'{porte}',
                            'Sexo': f'{sexo}',
                            'Vacinado': f'{vacinado}',
                            'Descricao': f'{descricao}'
                        }
                    }
                with open(caminhoArquivoAnimal, 'r') as arquivo: # Aqui ele vai ler o arquivo
                        try: 
                            dadosExistentes = json.load(arquivo) 
                        except json.JSONDecodeError: # Caso o arquivo estiver em branco, corrompido ou em formato errado ele vai definir como vazio
                            dadosExistentes = {}
                        alterar_animal = alterarAnimal() 
                        dadosExistentes.update(alterar_animal)# Adicionando os novos animais nos dados já existentes
                with open(caminhoArquivoAnimal, 'w') as arquivo:
                        json.dump(dadosExistentes, arquivo, indent=4) # Ele reescreve o arquivo com novos dados! 
                print("\n✅ Informações atualizadas com sucesso!\n")
                    
                continuar = input("\n🔙 Pressione Enter para continuar...")

            case (4):
                ID = input("\n🆔 Digite o ID do animal que deseja remover: ")
                with open(caminhoArquivoAnimal, 'r') as arquivo: # Aqui ele vai ler o arquivo
                        try: 
                            dadosExistentes = json.load(arquivo) 
                        except json.JSONDecodeError: # Caso o arquivo estiver em branco, corrompido ou em formato errado ele vai definir como vazio
                            dadosExistentes = {}
                        if ID in dadosExistentes:
                            del dadosExistentes[ID]
                            with open(caminhoArquivoAnimal, 'w') as arquivo:
                                json.dump(dadosExistentes, arquivo, indent=4) # Ele reescreve o arquivo com novos dados! 
                            print("\n🗑️  Animal removido com sucesso!")
                continuar = input("\n🔙 Pressione Enter para continuar...")

            case (0):
                print("\n👋 Voltando ao menu principal...")
                break

            case (_):
                print("\n")
                print("\n❌ Opção inválida! Tente (1,2,3,4 ou 0)")
                print("\n")
                continuar = input("\n🔙 Pressione Enter para continuar...")
