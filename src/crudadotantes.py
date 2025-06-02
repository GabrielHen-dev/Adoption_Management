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
      


def menuadotantes():
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\033[1;36m")  
        print("╔══════════════════════════════╗")
        print("║    \033[1;33m🐾 MEN6U ADOTANTE 🐾\033[1;36m     ║")
        print("╠══════════════════════════════╣")
        print("║ \033[1;32m1. Cadastrar novo adotante \033[1;36m ║")
        print("║ \033[1;32m2. Listar usuários        \033[1;36m ║")
        print("║ \033[1;32m3. Atualizar perfil       \033[1;36m ║")
        print("║ \033[1;32m4. Preferências de adoção \033[1;36m ║")
        print("║ \033[1;32m5. Excluir conta          \033[1;36m ║")
        print("║ \033[1;31m0. Sair                   \033[1;36m ║")
        print("╚══════════════════════════════╝")
        print("\033[0m")  
        global opcao
        opcao = int(input("\033[1;34mEscolha uma opção: \033[0m"))
        


while True:
     menuadotantes()
     match (opcao):
          case (1): # Não completo
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

          case (2): #completo
               
               with open(caminhoArquivoadotantes,'r') as arquivo:
                    dados = json.load(arquivo)
                    print ('- Os usuários cadastrados são: \n',json.dumps(dados,indent=4))
                    continuar = input('\n🔙 Pressione enter para continuar.')

        

          case (3): #Não completo 
               with open(caminhoArquivoadotantes, 'r') as arquivo:
                    try: 
                         dadosexistentes = json.load(arquivo) 
                    except json.JSONDecodeError:
                         dadosexistentes = {}
               cpfalterar= input('Digite o CPf do usuário que vai ter os dados atualizados -->')

               def menualterar():
                    os.system('cls' if os.name == 'nt' else 'clear') 
                    print("╔═════════════════════════════════╗")
                    print("║       🐾 ALTERAR ANIMAL         ║")
                    print("╠═════════════════════════════════╣")
                    print("║ [1] Alterar nome                ║")
                    print("║ [2] Alterar idade               ║")
                    print("║ [3] Alterar Contato             ║")
                    print("║ [4] Alterar CPF                 ║")
                    print("║ [5] Alterar E-mail              ║")
                    print("║ [6] Alterar senha               ║")
                    print("║ [0] Voltar                      ║")
                    print("╚═════════════════════════════════╝")
                         
               

               def alterarUsuario(nome,idade,contato,cpf,email,senha):

                    return{ 
                         f'{cpf}':{
                              'Nome': f'{nome}',
                              'Idade': f'{idade}',
                              'Contato': f'{contato}',
                              'E-mail':f'{email}',
                              'senha':f'{senha}'
                              }
                         }

               def enviarDados():
                    dadosexistentes.updade(alterar_usuario)
                    with open(caminhoArquivoadotantes, 'w') as arquivo:
                         json.dump(dadosexistentes,arquivo,indent=4)
                    print("\n✅ Informações atualizadas com sucesso!\n")


               def alterarInput():
                    global alterar_usuario
                    while True:
                         menualterar()
                         opcao = obterInputValido('\n👉 Digite a opção desejada: ')

                         match(opcao):

                              case (1):
                                   cpf = input('Digite o CPF da pessoa que deseja alterar -->')

                                   if cpf in dadosexistentes:
                                        alterar_usuario = alterarUsuario

                         

          


              

          case(4): #NÃO FEITO(adoção inteligente)
               
               print


          case(5): #Completo
               
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
               print('Opção inválida!')
               continue
          