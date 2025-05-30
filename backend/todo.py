"""
Rotas da To-Do List em um blueprint independente.
"""

from flask import Blueprint, jsonify, request

todo_bp = Blueprint("todo", __name__)   # nome + módulo

# ---- Armazenamento em memória -------------------------------
todos = [
    {"id": 1, "text": "Write docs",  "done": False},
    {"id": 2, "text": "Build API",   "done": False},
]

def next_id() -> int:
    return max((t["id"] for t in todos), default=0) + 1

# ---- Rotas ---------------------------------------------------

@todo_bp.route("/todos", methods=["GET"])
def list_todos():
    """Retorna a lista completa."""
    return jsonify(todos)


@todo_bp.route("/todos", methods=["POST"])
def create_todo():
    """Adiciona um novo item."""
    data = request.get_json() or {}
    if "text" not in data:
        return {"error": "Campo 'text' obrigatório."}, 400

    todo = {"id": next_id(), "text": data["text"], "done": False}
    todos.append(todo)
    return jsonify(todo), 201


@todo_bp.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id: int):
    """Remove um item pelo id."""
    global todos
    todos = [t for t in todos if t["id"] != todo_id]
    return "", 204


@todo_bp.route("/todos/<int:todo_id>", methods=["PUT"])
def toggle_done(todo_id: int):
    """Inverte o status done/undone."""
    for t in todos:
        if t["id"] == todo_id:
            t["done"] = not t["done"]
            return jsonify(t)
    return "", 404
