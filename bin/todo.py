from flask import Flask, jsonify, request, render_template
import json
from pathlib import Path

app = Flask(__name__)

DATA_FILE = Path(__file__).parent / 'todos.json'

# Seed data — used only on first run, before todos.json exists
INITIAL_TODOS = [ ]


def load_todos():
    if not DATA_FILE.exists():
        todos = [{'id': i + 1, 'text': t, 'done': False}
                 for i, t in enumerate(INITIAL_TODOS)]
        save_todos(todos)
        return todos
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_todos(todos):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)

@app.route('/api/todos', methods=['GET'])
def get_todos():
    return jsonify(load_todos())

@app.route('/api/todos', methods=['POST'])
def add_todo():
    data = request.get_json() or {}
    text = (data.get('text') or '').strip()
    if not text:
        return jsonify({'error': 'empty'}), 400
    todos = load_todos()
    todo = {
        'id': max([t['id'] for t in todos], default=0) + 1,
        'text': text[:300],
        'done': False
    }
    todos.append(todo)
    save_todos(todos)
    return jsonify(todo), 201


@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.get_json() or {}
    todos = load_todos()
    for t in todos:
        if t['id'] == todo_id:
            if 'text' in data:
                t['text'] = data['text'].strip()[:300]
            if 'done' in data:
                t['done'] = bool(data['done'])
            save_todos(todos)
            return jsonify(t)
    return jsonify({'error': 'not found'}), 404


@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todos = load_todos()
    filtered = [t for t in todos if t['id'] != todo_id]
    if len(filtered) == len(todos):
        return jsonify({'error': 'not found'}), 404
    save_todos(filtered)
    return jsonify({'ok': True})


if __name__ == '__main__':
    app.run(debug=True, port=5000)