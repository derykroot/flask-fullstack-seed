"""
Ponto de entrada da aplicação Flask.
Apenas cria a instância do app e registra os blueprints.
"""


from flask import Flask
from flask_cors import CORS

from todo import todo_bp       # importa o blueprint do módulo todo.py

def create_app() -> Flask:
    app = Flask(__name__)
    CORS(app)

    # registre cada blueprint que você criar
    app.register_blueprint(todo_bp, url_prefix="/api")

    return app


# Instância global usada pelo comando `flask run`
app = create_app()

# Execução direta (p.ex. `python app.py`) — opcional no Docker
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
