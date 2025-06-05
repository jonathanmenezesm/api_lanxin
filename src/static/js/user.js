// Função para inserir usuários
document.getElementById('inserir_usuario').addEventListener('submit', async function(e) {
    e.preventDefault(); // Impede o envio tradicional do formulário (recarregar a página)

    // Pega os valores dos campos do formulário
    const nome = document.getElementById('nome').value; // Pega o valor do campo nome
    const email = document.getElementById('email').value; // Pega o valor do campo email

    // Envia os dados para o backend usando fetch, no formato JSON
    const resposta = await fetch('/user/', {
        method: 'POST', // Método HTTP POST
        headers: {
            'Content-Type': 'application/json' // Informa que está enviando JSON
        },
        body: JSON.stringify({ nome, email }) // Converte os dados para JSON
    });

    if (resposta.ok) {
        atualizarTabelaUsuarios(); // Atualiza a tabela sem recarregar a página
        // Limpa os campos do formulário
        document.getElementById('nome').value = '';
        document.getElementById('email').value = '';
    } else {
        alert('Erro ao inserir usuário!');
    }
});

// Função para atualizar a tabela de usuários dinamicamente
async function atualizarTabelaUsuarios() {
    // Busca a lista de usuários em formato JSON
    const resposta = await fetch('/user/json');
    const usuarios = await resposta.json();

    // Seleciona o corpo da tabela
    const tbody = document.querySelector('tbody');
    tbody.innerHTML = ''; // Limpa a tabela

    // Para cada usuário, cria uma linha na tabela
    usuarios.forEach(user => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <th>${user.id}</th>
            <td>${user.nome}</td>
            <td>${user.email}</td>
            <td>
                <button id="edit">Editar</button>
                <button id="delete">Deletar</button>
            </td>
        `;
        tbody.appendChild(tr);
    });
}

// Atualiza a tabela ao carregar a página
window.addEventListener('DOMContentLoaded', atualizarTabelaUsuarios);

// ----------------------------------------------------------------------------------------------

// Função para deletar um usuário
document.querySelector('tbody').addEventListener('click', async function(e) {
    if (e.target.id === 'delete') {
        const tr = e.target.closest('tr'); // Pega a linha do usuário
        const id = tr.querySelector('th').textContent; // Pega o ID do usuário

        // Envia uma requisição DELETE para o backend
        const resposta = await fetch(`/user/${id}`, {
            method: 'DELETE'
        });

        if (resposta.ok) {
            atualizarTabelaUsuarios(); // Atualiza a tabela após deletar
        } else {
            alert('Erro ao deletar usuário!');
        }
    }
});