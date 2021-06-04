from flask import render_template
from loja import app

@app.route('/') 
@app.route('/maisvendidos')
def homepage():
	return render_template('maisvendidos.html')

@app.route('/login')
def login():
	return "index.html"

@app.route('/atendimento')
def atendimento():
	return "<h1>Atendimento</h1>"

@app.route('/sobre')
def sobre():
	return "<h1>Sobre</h1>"

@app.route('/carrinho')
def carrinho():
	return "<h1>Carrinho</h1>"

