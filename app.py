from flask import Flask, render_template, request

app = Flask(__name__)

# Dados simulados (No futuro virão do Banco de Dados)
cardapio_db = [
    {"id": 1, "nome": "Macarrão Tradicional", "descricao": "Massa artesanal e legumes frescos.", "preco": 25.00},
    {"id": 2, "nome": "Especial de Bacon", "descricao": "Bacon crocante e muito queijo.", "preco": 32.00},
    {"id": 3, "nome": "Frango com Catupiry", "descricao": "Frango desfiado com Catupiry original.", "preco": 28.50},
    {"id": 3, "nome": "Frango com Catupiry", "descricao": "Frango desfiado com Catupiry original.", "preco": 28.50}
]

@app.route('/')
def index():
    return render_template('cardapio.html', pratos=cardapio_db)

@app.route('/index')
def carrinho():
    return render_template('carrinho.html')

@app.route('/final', methods=['POST'])
def finalizado():
    pagamento_escolhido = request.form.get('metodo_pagamento')
    return render_template('finalizado.html', pagamento=pagamento_escolhido)


if __name__ == '__main__':
    # host='0.0.0.0' permite que você acesse pelo IP do PC no celular
    app.run(debug=True, host='0.0.0.0')