const API_BASE = 'http://localhost:5000/api/todos';

async function fetchTodos() {
  const res = await fetch(API_BASE);
  const data = await res.json();
  renderTodos(data);
}

async function addTodo(text) {
  await fetch(API_BASE, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ text })
  });
  fetchTodos();
}

async function deleteTodo(id) {
  await fetch(`${API_BASE}/${id}`, { method: 'DELETE' });
  fetchTodos();
}

async function toggleTodo(id) {
  await fetch(`${API_BASE}/${id}`, { method: 'PUT' });
  fetchTodos();
}

function renderTodos(todos) {
  const list = document.getElementById('todo-list');
  list.innerHTML = '';
  todos.forEach(todo => {
    const li = document.createElement('li');
    if (todo.done) li.classList.add('done');

    const span = document.createElement('span');
    span.textContent = todo.text;
    span.addEventListener('click', () => toggleTodo(todo.id));

    const del = document.createElement('button');
    del.textContent = '✕';
    del.addEventListener('click', () => deleteTodo(todo.id));

    li.appendChild(span);
    li.appendChild(del);
    list.appendChild(li);
  });
}

document.getElementById('todo-form').addEventListener('submit', e => {
  e.preventDefault();
  const input = document.getElementById('todo-input');
  const text = input.value.trim();
  if (text) {
    addTodo(text);
    input.value = '';
  }
});

fetchTodos();
