from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
  return render_template('index.html',
                         title='Avaliação Contínua: Aula 030',
                         options=["Home", "Identificacao", "requisicao"])


@app.route('/identificacao')
def identificacao():
  return render_template('identificacao.html',
                         title='Avaliação contínua: Aula 030',
                         aluno='Gustavo Lopes',
                         prontuario='PT3019896',
                         instituicao='IFSP')


@app.route('/contextorequisicao')
def contexto_requisicao():
  navegador = request.user_agent.browser
  ip = request.remote_addr
  host = request.host

  return render_template('contextorequisicao.html',
                         title='Avaliação contínua: Aula 030',
                         navegador=navegador,
                         ip=ip,
                         host=host)
