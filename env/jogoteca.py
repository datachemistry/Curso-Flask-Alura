from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = "datachemistry"

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo("Super Mario", "Ação", "Snes")
jogo2 = Jogo("Pokemon", "Ação", "GBA")
jogo3 = Jogo("Mortal Kombat 2", "Ação", "Snes")
jogo4 = Jogo("Farcry Primal", "Tiro", "Xbox")
lista = [jogo1 , jogo2, jogo3]

@app.route('/')
def ola():
  
    return render_template('lista.html', 
                           titulo ='Jogos', 
                           jogos = lista)


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo ='Adicionar Jogo')

@app.route('/criar', methods = ['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome,categoria,console)
    lista.append(jogo)
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods = ['POST',])
def autenticar():
    if 'mestra'== request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(request.form['usuario'] + ' logou com sucesso')
        return redirect('/')
    else:
        flash('Não logado, tente novamente!')
        return redirect('/login')

@app.route('/logout')
def logout():
    session['usuario'] = None
    flash('Nenhum usuário Logado')
    return redirect('/')

app.run(debug=True)