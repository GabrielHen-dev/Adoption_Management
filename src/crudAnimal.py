import json 
import os  
import uuid 

caminhoArquivoAnimal = "C:..\\Adoption_Management\\data\\Animais.json" 

if not os.path.exists(caminhoArquivoAnimal):
    with open(caminhoArquivoAnimal, 'w') as arquivo: 
        json.dump({}, arquivo)

def obterInputValido(mensagem, tipo=str):
    while True:
        entrada = input(mensagem).strip()

        if entrada == "" or entrada == None:
            print("\n❌ Este campo é obrigatório. Por favor, preencha.\n")
            continue

        if tipo == int:
            if entrada.isdigit():
                return int(entrada)
            else:
                print("\n❌ Digite um número válido.\n")
                continue    
        return entrada
                    
def mostrar_menuAnimais():
    os.system('cls' if os.name == 'nt' else 'clear') 
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
    while True: 
        mostrar_menuAnimais() 
        opcao = int(input("\n👉 Digite a opção desejada: "))
  
        match (opcao):
            case (1):
                    with open(caminhoArquivoAnimal, 'r') as arquivo: 
                        dados = json.load(arquivo)
                        print("\nAnimais Cadastrados:\n", json.dumps(dados, indent=4))
                    continuar = input("\nPressione Enter para continuar")

            case (2):
                    
                def novoAnimal(): 
                    ID = uuid.uuid4() 
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

                with open(caminhoArquivoAnimal, 'r') as arquivo: 
                    try: 
                        dadosExistentes = json.load(arquivo) 
                    except json.JSONDecodeError: 
                        dadosExistentes = {}
                    novo_animal = novoAnimal() 
                    dadosExistentes.update(novo_animal) 
                with open(caminhoArquivoAnimal, 'w') as arquivo:
                    json.dump(dadosExistentes, arquivo, indent=4) 
                print("\n✅ Animal cadastrado com sucesso!\n")
                continuar = input("\n🔙 Pressione Enter para continuar...")

            case (3):
                with open(caminhoArquivoAnimal, 'r') as arquivo: 
                        try: 
                            dadosExistentes = json.load(arquivo) 
                        except json.JSONDecodeError:
                            dadosExistentes = {}
                
                def escolhaAlterar():
                    os.system('cls' if os.name == 'nt' else 'clear') 
                    print("╔═════════════════════════════════╗")
                    print("║       🐾 ALTERAR ANIMAL         ║")
                    print("╠═════════════════════════════════╣")
                    print("║ [1] 🐶 Alterar nome             ║")
                    print("║ [2] 🎂 Alterar idade            ║")
                    print("║ [3] 🐾 Alterar espécie          ║")
                    print("║ [4] 🧬 Alterar raça             ║")
                    print("║ [5] 📏 Alterar porte            ║")
                    print("║ [6] ⚧️ Alterar sexo              ║")
                    print("║ [7] 💉 Alterar vacinação        ║")
                    print("║ [8] 📝 Alterar descrição        ║")
                    print("║ [0] 🔙 Voltar                   ║")
                    print("╚═════════════════════════════════╝")

                def alterarAnimal(ID, nome, idade, tipo, raca, porte, sexo, vacinado, descricao): 
                   while True:
                             
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
                   
                def enviarDados():
                    dadosExistentes.update(alterar_animal)
                    with open(caminhoArquivoAnimal, 'w') as arquivo:
                            json.dump(dadosExistentes, arquivo, indent=4) 
                    print("\n✅ Informações atualizadas com sucesso!\n")
                
                    continuar = input("\n🔙 Pressione Enter para continuar...")
                   
                def alterarInput():
                    global alterar_animal
                    global ID
                    while True:
                        escolhaAlterar()
                        opcao = int(input("\n👉 Digite a opção desejada: "))
                        if opcao == 1:
                            ID = obterInputValido("\n🆔 Digite o ID do animal que deseja alterar: ")                 
                            if ID in dadosExistentes:     
                                alterar_animal = alterarAnimal(
                                    ID,
                                    nome = obterInputValido("\n📛 Nome do animal: "),
                                    idade = dadosExistentes[ID]['Idade'],
                                    tipo = dadosExistentes[ID]['Tipo'],
                                    raca = dadosExistentes[ID]['Raca'],
                                    porte = dadosExistentes[ID]['Porte'],
                                    sexo = dadosExistentes[ID]['Sexo'],
                                    vacinado = dadosExistentes[ID]['Vacinado'],
                                    descricao = dadosExistentes[ID]['Descricao']
                                    )
                                enviarDados()
                            else:
                                print("\n⚠️  ID não encontrado nos registros.")
                                continuar = input("\n🔙 Pressione Enter para continuar...")
                                

                        elif opcao == 2:
                            ID = obterInputValido("\n🆔 Digite o ID do animal que deseja alterar: ")                 
                            if ID in dadosExistentes:     
                                alterar_animal = alterarAnimal(
                                    ID,
                                    nome = dadosExistentes[ID]['Nome'],
                                    idade = obterInputValido("🎂 Idade (em anos): ", tipo=int),
                                    tipo = dadosExistentes[ID]['Tipo'],
                                    raca = dadosExistentes[ID]['Raca'],
                                    porte = dadosExistentes[ID]['Porte'],
                                    sexo = dadosExistentes[ID]['Sexo'],
                                    vacinado = dadosExistentes[ID]['Vacinado'],
                                    descricao = dadosExistentes[ID]['Descricao']
                                    )
                                enviarDados()
                            else:
                                print("\n⚠️  ID não encontrado nos registros.")
                                continuar = input("\n🔙 Pressione Enter para continuar...")
                                

                        elif opcao == 3:    
                            ID = obterInputValido("\n🆔 Digite o ID do animal que deseja alterar: ")                 
                            if ID in dadosExistentes:     
                                alterar_animal = alterarAnimal(
                                    ID,
                                    nome = dadosExistentes[ID]['Nome'],
                                    idade = dadosExistentes[ID]['Idade'],
                                    tipo = obterInputValido("🐾 Espécie (ex: cachorro, gato): "),
                                    raca = dadosExistentes[ID]['Raca'],
                                    porte = dadosExistentes[ID]['Porte'],
                                    sexo = dadosExistentes[ID]['Sexo'],
                                    vacinado = dadosExistentes[ID]['Vacinado'],
                                    descricao = dadosExistentes[ID]['Descricao']
                                    )
                                enviarDados()
                            else:
                                print("\n⚠️  ID não encontrado nos registros.")
                                continuar = input("\n🔙 Pressione Enter para continuar...")
                                
                        elif opcao == 4:
                            ID = obterInputValido("\n🆔 Digite o ID do animal que deseja alterar: ")                 
                            if ID in dadosExistentes:     
                                alterar_animal = alterarAnimal(
                                    ID,
                                    nome = dadosExistentes[ID]['Nome'],
                                    idade = dadosExistentes[ID]['Idade'],
                                    tipo = dadosExistentes[ID]['Tipo'],
                                    raca = obterInputValido("🧬 Raça: "),
                                    porte = dadosExistentes[ID]['Porte'],
                                    sexo = dadosExistentes[ID]['Sexo'],
                                    vacinado = dadosExistentes[ID]['Vacinado'],
                                    descricao = dadosExistentes[ID]['Descricao']
                                    )
                                enviarDados()
                            else:
                                print("\n⚠️  ID não encontrado nos registros.")
                                continuar = input("\n🔙 Pressione Enter para continuar...")
                                

                        elif opcao == 5:
                            ID = obterInputValido("\n🆔 Digite o ID do animal que deseja alterar: ")                 
                            if ID in dadosExistentes:     
                                alterar_animal = alterarAnimal(
                                    ID,
                                    nome = dadosExistentes[ID]['Nome'],
                                    idade = dadosExistentes[ID]['Idade'],
                                    tipo = dadosExistentes[ID]['Tipo'],
                                    raca = dadosExistentes[ID]['Raca'],
                                    porte = obterInputValido("📏 Porte (pequeno, médio, grande): "),
                                    sexo = dadosExistentes[ID]['Sexo'],
                                    vacinado = dadosExistentes[ID]['Vacinado'],
                                    descricao = dadosExistentes[ID]['Descricao']
                                    )
                                enviarDados()
                            else:
                                print("\n⚠️  ID não encontrado nos registros.")
                                continuar = input("\n🔙 Pressione Enter para continuar...")
                                

                        elif opcao == 6:
                            ID = obterInputValido("\n🆔 Digite o ID do animal que deseja alterar: ")                 
                            if ID in dadosExistentes:     
                                alterar_animal = alterarAnimal(
                                    ID,
                                    nome = dadosExistentes[ID]['Nome'],
                                    idade = dadosExistentes[ID]['Idade'],
                                    tipo = dadosExistentes[ID]['Tipo'],
                                    raca = dadosExistentes[ID]['Raca'],
                                    porte = dadosExistentes[ID]['Porte'],
                                    sexo = obterInputValido("⚧️ Sexo (macho/fêmea): "),
                                    vacinado = dadosExistentes[ID]['Vacinado'],
                                    descricao = dadosExistentes[ID]['Descricao']
                                    )
                                enviarDados()
                            else:
                                print("\n⚠️  ID não encontrado nos registros.")
                                continuar = input("\n🔙 Pressione Enter para continuar...")
                                

                        elif opcao == 7:
                            ID = obterInputValido("\n🆔 Digite o ID do animal que deseja alterar: ")                 
                            if ID in dadosExistentes:     
                                alterar_animal = alterarAnimal(
                                    ID,
                                    nome = dadosExistentes[ID]['Nome'],
                                    idade = dadosExistentes[ID]['Idade'],
                                    tipo = dadosExistentes[ID]['Tipo'],
                                    raca = dadosExistentes[ID]['Raca'],
                                    porte = dadosExistentes[ID]['Porte'],
                                    sexo = dadosExistentes[ID]['Sexo'],
                                    vacinado = obterInputValido("💉 Está vacinado? (s/n): "),
                                    descricao = dadosExistentes[ID]['Descricao']
                                    )
                                enviarDados()
                            else:
                                print("\n⚠️  ID não encontrado nos registros.")
                                continuar = input("\n🔙 Pressione Enter para continuar...")
                                

                        elif opcao == 8:
                            ID = obterInputValido("\n🆔 Digite o ID do animal que deseja alterar: ")                 
                            if ID in dadosExistentes:     
                                alterar_animal = alterarAnimal(
                                    ID,
                                    nome = dadosExistentes[ID]['Nome'],
                                    idade = dadosExistentes[ID]['Idade'],
                                    tipo = dadosExistentes[ID]['Tipo'],
                                    raca = dadosExistentes[ID]['Raca'],
                                    porte = dadosExistentes[ID]['Porte'],
                                    sexo = dadosExistentes[ID]['Sexo'],
                                    vacinado = dadosExistentes[ID]['Vacinado'],
                                    descricao = input("📝 Descreva o comportamento ou histórico (opcional): ")
                                    )
                                enviarDados()
                            else:
                                print("\n⚠️  ID não encontrado nos registros.")
                                continuar = input("\n🔙 Pressione Enter para continuar...")
                                

                        elif opcao == 0:
                            break

                        else:
                            print("\n❌ Opção inválida!\n")
            
                            continuar = input("\n🔙 Pressione Enter para continuar...")
                alterarInput()
                
            case (4):
                with open(caminhoArquivoAnimal, 'r') as arquivo: 
                        try: 
                            dadosExistentes = json.load(arquivo) 
                        except json.JSONDecodeError: 
                            dadosExistentes = {}
                        
                while True:
                         ID = obterInputValido("\n🆔 Digite o ID do animal que deseja remover: ")                 
                         if ID in dadosExistentes: 
                            del dadosExistentes[ID]
                            with open(caminhoArquivoAnimal, 'w') as arquivo:
                                json.dump(dadosExistentes, arquivo, indent=4) 
                            print("\n🗑️  Animal removido com sucesso!\n")
                            continuar = input("\n🔙 Pressione Enter para continuar...")
                            break
                         else:
<<<<<<< HEAD
                            print("\n⚠️  ID não encontrado nos registros.")
=======
                            print("\n⚠️ ID não encontrado nos registros.\n")
>>>>>>> b29ab459c2d4f874f13e73150b6e2780ac5104c2
                            continuar = input("\n🔙 Pressione Enter para continuar...")
                         continue
                
            case (0):
                print("\n👋 Voltando ao menu principal...")
                break

            case (_):
                print("\n")
                print("\n❌ Opção inválida! Tente (1,2,3,4 ou 0)")
                print("\n")
                continuar = input("\n🔙 Pressione Enter para continuar...")
