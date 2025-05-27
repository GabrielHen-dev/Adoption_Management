# from flask import Flask, render_template, request, redirect, url_for
# import json
# import os
# import uuid

# app = Flask(__name__)
# caminhoArquivoAnimal = "../data/Animais.json"

# if not os.path.exists(caminhoArquivoAnimal):
#     with open(caminhoArquivoAnimal, 'w') as arquivo:
#         json.dump({}, arquivo)

# def carregar_animais():
#     with open(caminhoArquivoAnimal, 'r') as arquivo:
#         try:
#             return json.load(arquivo)
#         except json.JSONDecodeError:
#             return {}

# def salvar_animais(animais):
#     with open(caminhoArquivoAnimal, 'w') as arquivo:
#         json.dump(animais, arquivo, indent=4)

# @app.route('/')
# def index():
#     animais = carregar_animais()
#     return render_template('index.html', animais=animais)

# @app.route('/novo', methods=['GET', 'POST'])
# def novo():
#     if request.method == 'POST':
#         animais = carregar_animais()
#         ID = str(uuid.uuid4())
#         animais[ID] = {
#             'Nome': request.form['nome'],
#             'Idade': request.form['idade'],
#             'Tipo': request.form['tipo'],
#             'Raca': request.form['raca'],
#             'Porte': request.form['porte'],
#             'Sexo': request.form['sexo'],
#             'Vacinado': request.form['vacinado'],
#             'Descricao': request.form['descricao']
#         }
#         salvar_animais(animais)
#         return redirect(url_for('index'))
#     return render_template('novo.html')

# @app.route('/remover/<id>')
# def remover(id):
#     animais = carregar_animais()
#     if id in animais:
#         del animais[id]
#         salvar_animais(animais)
#     return redirect(url_for('index'))

# # Adicione rotas para editar se quiser

# if __name__ == '__main__':
#     app.run(debug=True)