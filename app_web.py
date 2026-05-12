import os
from flask import Flask, jsonify
from datetime import date
from src.feriados import buscar_feriados

app = Flask(__name__)


@app.route("/")
def index():
    return """
    <html>
    <head><title>Organizador de Estudos</title></head>
    <body style="font-family: sans-serif; max-width: 600px; margin: 40px auto; padding: 20px;">
        <h1>📚 Organizador de Tarefas de Estudo</h1>
        <p>Aplicação CLI para gerenciar tarefas de estudo por matéria e prazo.</p>
        <h2>Endpoints disponíveis:</h2>
        <ul>
            <li><a href="/feriados">/feriados</a> — lista feriados nacionais do ano atual</li>
        </ul>
        <hr>
        <p><a href="https://github.com/Caua-Godoy/organizador-de-estudos">Repositório no GitHub</a></p>
    </body>
    </html>
    """


@app.route("/feriados")
def feriados():
    data = buscar_feriados(date.today().year)
    return jsonify(data)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
