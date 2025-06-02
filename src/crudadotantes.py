import json
import os

caminhoArquivoadotantes = 'C:..\\Adoption_Management\\data\\adotantes.json'

if not os.path.exists(caminhoArquivoadotantes):
    with open(caminhoArquivoadotantes,'w') as arquivo:
        json.dump({},arquivo)

def obterInputValido(mensagem, tipo=str):
     
     while True:
          entrada = input(mensagem).strip()

          if entrada == '' or entrada == None:
               print('\n❌ Este campo é obrigatório. Por favor, preencha.\n') 
               continue

          if tipo == int:
               if entrada.isdigit():
                    return int(entrada)
               
               else:
                    print("\n❌ Digite um número válido.\n")
                    continue
          return entrada
     
     
def buscar_animais_preferidos(preferencias, caminho_animais):
      
     with open(caminho_animais, 'r') as arq:
          dados_animais = json.load(arq)

     encontrados = []
     for id_animal, animal in dados_animais.items():
          if (
               animal['Tipo'].lower() == preferencias['tipo']
               and animal['Porte'].lower() == preferencias['porte']
               and animal['Sexo'].lower() == preferencias['sexo']
          ):
               encontrados.append({id_animal: animal})
     return encontrados
 
 
def menuadotantes():
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\033[1;36m")  
        print("╔══════════════════════════════╗")
        print("║    \033[1;33m🐾 MENU ADOTANTE 🐾\033[1;36m       ║")
        print("╠══════════════════════════════╣")
        print("║ \033[1;32m1. Cadastrar novo adotante \033[1;36m  ║")
        print("║ \033[1;32m2. Listar usuários        \033[1;36m   ║")
        print("║ \033[1;32m3. Atualizar perfil       \033[1;36m   ║")
        print("║ \033[1;32m4. Preferências de adoção \033[1;36m   ║")
        print("║ \033[1;32m5. Excluir conta          \033[1;36m   ║")
        print("║ \033[1;31m0. Sair                   \033[1;36m   ║")
        print("╚══════════════════════════════╝")
        print("\033[0m")  
        global opcao
        opcao = int(input("\033[1;34mEscolha uma opção: \033[0m"))
        
def executar_menuAdotantes():
    while True:
     menuadotantes()
     match (opcao):
          case (1):

               def menucadastro():
                    
                    nome = obterInputValido('- Digite seu nome completo --> ')
                    idade = obterInputValido('- Digite sua idade (em anos) --> ', tipo=int)
                    contato = obterInputValido('- Insira seu contato--> ')
                    cpf = obterInputValido('- Digite seu CPF --> ')
                    email = obterInputValido('- Digite seu email -->')
                    senha = obterInputValido('- Informe uma senha para seu login --> ')

                    return {
                         f'{cpf}':{
                              'nome': f'{nome}',
                              'idade': f'{idade}',
                              'contato': f'{contato}',
                              'email': f'{email}',
                              'senha': f'{senha}',
                         }
                    }
               with open(caminhoArquivoadotantes,'r') as arquivo:
                    dadosexistentes = json.load(arquivo)
                    menu_cadastro = menucadastro()
                    dadosexistentes.update(menu_cadastro) 
               with open(caminhoArquivoadotantes, 'w') as arquivo:
                         json.dump(dadosexistentes,arquivo,indent = 4)
               print("\n✅ Usuário cadastrado com sucesso!\n")
               continuar = input('\n🔙 Pressione enter para continuar.')

          case (2): # completo 
               
               with open(caminhoArquivoadotantes,'r') as arquivo:
                    dados = json.load(arquivo)
                    print ('- Os usuários cadastrados são: \n',json.dumps(dados,indent=4))
                    continuar = input('\n🔙 Pressione enter para continuar.')

          case (3): # completo com verificação

               with open(caminhoArquivoadotantes, 'r') as arquivo:
                    try: 
                         dadosexistentes = json.load(arquivo) 
                    except json.JSONDecodeError:
                         dadosexistentes = {}
               
               def menuAlterar():
                    print("╔═════════════════════════════════╗")
                    print("║       😎 ALTERAR USUÁRIO        ║")
                    print("╠═════════════════════════════════╣")
                    print("║ [1] Alterar nome                ║")
                    print("║ [2] Alterar idade               ║")
                    print("║ [3] Alterar Contato             ║")
                    print("║ [4] Alterar E-mail              ║")
                    print("║ [5] Alterar senha               ║")
                    print("║ [0] Voltar                      ║")
                    print("╚═════════════════════════════════╝")

               cpf = obterInputValido('Insira o cpf do pessoa que deseja atualizar -->')

               if cpf not in dadosexistentes:
                    print('-\n❌ CPF não existente na base de dados.')
                    continuar = input("\n🔙 Pressione Enter para continuar...")
                    continue

               else:
                    while True:
                         menuAlterar()
                         opcao2 = obterInputValido('👉 Digite a atualização desejada--> ')
                         
                         if opcao == '0':
                              print('Saindo...')
                              continuar = input("\n🔙 Pressione Enter para continuar...")
                              break

                         elif opcao2 == '1':
                              dadosexistentes[cpf]['nome'] = obterInputValido('- Alterar nome -->')

                         elif opcao2 == '2':
                              dadosexistentes[cpf]['idade'] = obterInputValido('- Alterar idade -->')

                         elif opcao2 == '3':
                              dadosexistentes[cpf]['contato'] = obterInputValido('- Alterar contato -->')

                         elif opcao2 == '4':
                              dadosexistentes[cpf]['email'] = obterInputValido('- Alterar E-mail -->')

                         elif opcao2 == '5':
                              dadosexistentes[cpf]['senha'] = obterInputValido('- Alterar senha -->')

                         else:
                              print('\n ❌ Opcão inválida ❌')
                              continuar = input("\n🔙 Pressione Enter para continuar...")
                              continue


                         with open(caminhoArquivoadotantes, 'w') as arquivo:
                              json.dump(dadosexistentes,arquivo,indent=4)
                         print('\n✅ Alterações salvas!')
                         continuar = input("\n🔙 Pressione Enter...")
                         break

          case (4):
               with open(caminhoArquivoadotantes, 'r') as arquivo:
                    adotantes = json.load(arquivo)

               cpf = input('Digite seu CPF: ')
               if cpf in adotantes:
                    tipo = input('Tipo desejado (ex: cachorro, gato): ').lower()
                    porte = input('Porte (pequeno, médio, grande): ').lower()
                    sexo = input('Sexo (macho/fêmea): ').lower()

                    preferencias = {
                        'tipo': tipo,
                        'porte': porte,
                        'sexo': sexo
                    }

                    adotantes[cpf]['preferencias'] = preferencias

                    with open(caminhoArquivoadotantes, 'w') as arquivo:
                         json.dump(adotantes, arquivo, indent=4)

                    print('\nPreferências registradas.')

                    caminho_animais = os.path.join('..', 'data', 'Animais.json')
                    sugeridos = buscar_animais_preferidos(preferencias, caminho_animais)

                    if sugeridos:
                         print('\nAnimais compatíveis:')
                         for animal in sugeridos:
                              print(json.dumps(animal, indent=4))
                    else:
                         print('\nNenhum animal disponível corresponde ao perfil desejado.')
               else:
                    print('CPF não encontrado.')
                    input('\n🔙 Pressione enter para continuar.')



          case(5):
               
               while True:
                    with open(caminhoArquivoadotantes,'r') as arquivo:
                         try:
                              dadosexistentes = json.load(arquivo)
                         except json.JSONDecodeError:
                              dadosexistentes = {}

                    cpf = input('\nInsira o CPF dao usuário que vai ser excluido \n--> ')

                    if cpf in dadosexistentes:
                         del dadosexistentes[cpf]
                         with open(caminhoArquivoadotantes,'w') as arquivo:
                              json.dump(dadosexistentes,arquivo,indent=4)
                         print('\n=== Usuário removido com sucesso ===')
                         continuar = input('\n🔙 Pressione enter para continuar.') 
                         break

                    else:
                         print('\n ===== Esse usuário não existe! =====')
                         continuar = input('\n🔙 Pressione enter para continuar.')
                         break

          case _:

               print('Opção Inválida!')
               continue