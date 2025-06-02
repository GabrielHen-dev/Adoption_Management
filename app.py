# # menu: 
# # [1] Gerenciar animais
# # [2] Gerenciar adotantes
# # [3] Gerenciar adoções
# # [0] Sair
# # TESTE
# import json
# import os
# import uuid

# os.makedirs("data", exist_ok=True)

# ARQUIVO_ANIMAIS = "data/Animais.json"
# ARQUIVO_ADOTANTES = "data/Usuarios.json"
# ARQUIVO_ADOCOES = "data/Adocoes.json"

# for caminho in [ARQUIVO_ANIMAIS, ARQUIVO_ADOTANTES, ARQUIVO_ADOCOES]:
#     if not os.path.exists(caminho):
#         with open(caminho, 'w') as f:
#             json.dump({}, f)

# def carregar_dados(caminho):
#     with open(caminho, 'r') as f:
#         try:
#             return json.load(f)
#         except json.JSONDecodeError:
#             return {}

# def salvar_dados(caminho, dados):
#     with open(caminho, 'w') as f:
#         json.dump(dados, f, indent=4)

# def input_valido(mensagem, tipo=str, opcoes=None, obrigatorio=True):
#     while True:
#         valor = input(mensagem).strip()
#         if not valor and obrigatorio:
#             print("❌ Este campo é obrigatório.")
#             continue
#         if tipo == int:
#             if valor.isdigit():
#                 return int(valor)
#             print("❌ Digite um número válido.")
#             continue
#         if opcoes and valor.lower() not in opcoes:
#             print(f"❌ Opções válidas: {', '.join(opcoes)}")
#             continue
#         return valor

# def exibir_animais(animais):
#     if not animais:
#         print("Nenhum animal cadastrado.")
#         return
#     print("\nAnimais cadastrados:")
#     for id, a in animais.items():
#         print(f"ID: {id}")
#         print(f"  Nome: {a['Nome']}")
#         print(f"  Idade: {a['Idade']} anos")
#         print(f"  Tipo: {a['Tipo']}")
#         print(f"  Raça: {a.get('Raca', '-')}")
#         print(f"  Porte: {a.get('Porte', '-')}")
#         print(f"  Sexo: {a.get('Sexo', '-')}")
#         print(f"  Vacinado: {a.get('Vacinado', '-')}")
#         print(f"  Descrição: {a.get('Descricao', '-')}")
#         print("-" * 30)

# def menu_animais():
#     while True:
#         print("\n🐾 MENU ANIMAIS")
#         print("1. Listar Animais")
#         print("2. Cadastrar Animal")
#         print("3. Editar Animal")
#         print("4. Remover Animal")
#         print("0. Voltar")
#         opcao = input("Escolha: ")

#         animais = carregar_dados(ARQUIVO_ANIMAIS)

#         if opcao == "1":
#             exibir_animais(animais)

#         elif opcao == "2":
#             nome = input_valido("Nome: ")
#             idade = input_valido("Idade (anos): ", int)
#             especie = input_valido("Espécie: ")
#             raca = input_valido("Raça: ")
#             porte = input_valido("Porte (pequeno/médio/grande): ")
#             sexo = input_valido("Sexo (macho/fêmea): ", opcoes=["macho", "fêmea", "femea"])
#             vacinado = input_valido("Vacinado? (s/n): ", opcoes=["s", "n"])
#             descricao = input("Descrição (opcional): ").strip()
#             id_animal = str(uuid.uuid4())
#             animais[id_animal] = {
#                 "nome": nome,
#                 "idade": idade,
#                 "especie": especie,
#                 "raca": raca,
#                 "porte": porte,
#                 "sexo": sexo,
#                 "vacinado": vacinado,
#                 "descricao": descricao
#             }
#             salvar_dados(ARQUIVO_ANIMAIS, animais)
#             print("✅ Animal cadastrado!")

#         elif opcao == "3":
#             exibir_animais(animais)
#             id_edit = input_valido("ID do animal a editar: ")
#             if id_edit in animais:
#                 a = animais[id_edit]
#                 print("Deixe em branco para manter o valor atual.")
#                 nome = input(f"Novo nome [{a['nome']}]: ").strip() or a['nome']
#                 idade = input(f"Nova idade [{a['idade']}]: ").strip()
#                 idade = int(idade) if idade.isdigit() else a['idade']
#                 especie = input(f"Nova espécie [{a['especie']}]: ").strip() or a['especie']
#                 raca = input(f"Nova raça [{a.get('raca', '')}]: ").strip() or a.get('raca', '')
#                 porte = input(f"Novo porte [{a.get('porte', '')}]: ").strip() or a.get('porte', '')
#                 sexo = input(f"Novo sexo [{a.get('sexo', '')}]: ").strip() or a.get('sexo', '')
#                 vacinado = input(f"Vacinado? [{a.get('vacinado', '')}]: ").strip() or a.get('vacinado', '')
#                 descricao = input(f"Nova descrição [{a.get('descricao', '')}]: ").strip() or a.get('descricao', '')
#                 animais[id_edit] = {
#                     "nome": nome,
#                     "idade": idade,
#                     "especie": especie,
#                     "raca": raca,
#                     "porte": porte,
#                     "sexo": sexo,
#                     "vacinado": vacinado,
#                     "descricao": descricao
#                 }
#                 salvar_dados(ARQUIVO_ANIMAIS, animais)
#                 print("✅ Animal editado!")
#             else:
#                 print("❌ ID não encontrado.")

#         elif opcao == "4":
#             exibir_animais(animais)
#             id_remover = input_valido("ID do animal a remover: ")
#             if id_remover in animais:
#                 del animais[id_remover]
#                 salvar_dados(ARQUIVO_ANIMAIS, animais)
#                 print("✅ Animal removido!")
#             else:
#                 print("❌ ID não encontrado.")

#         elif opcao == "0":
#             break
#         else:
#             print("❌ Opção inválida.")

# # Os menus de adotantes e adoções podem ser melhorados de forma semelhante, se desejar.

# def menu_principal():
#     while True:
#         print("\n====== SISTEMA DE ADOÇÃO DE ANIMAIS ======")
#         print("1. Gerenciar Animais")
#         print("2. Gerenciar Adotantes")
#         print("3. Gerenciar Adoções")
#         print("0. Sair")
#         opcao = input("Escolha: ")

#         if opcao == "1":
#             menu_animais()
#         # menu_adotantes() e menu_adocoes() permanecem iguais
#         elif opcao == "2":
#             menu_adotantes()
#         elif opcao == "3":
#             menu_adocoes()
#         elif opcao == "0":
#             print("Saindo... Até logo! 🐾")
#             break
#         else:
#             print("❌ Opção inválida.")

# # ...mantenha menu_adotantes e menu_adocoes como já estão, ou adapte para mais campos se quiser...

# if __name__ == "__main__":
#     menu_principal()