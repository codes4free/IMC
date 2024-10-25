<!doctype html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Lista de Registros</title>
</head>
<body>
    <h1>Lista de Registros</h1>
    <a href="{{ url_for('criar') }}">Criar Novo Registro</a>
    <table border="1" cellpadding="5">
        <tr>
            <th>ID</th>
            <th>Nome</th>
            <th>Peso (kg)</th>
            <th>Altura (m)</th>
            <th>IMC</th>
            <th>Ações</th>
        </tr>
        {% for registro in registros %}
        <tr>
            <td>{{ loop.index0 }}</td>
            <td>{{ registro['nome'] }}</td>
            <td>{{ registro['peso'] }}</td>
            <td>{{ registro['altura'] }}</td>
            <td>{{ "%.2f" | format(registro['imc']) }}</td>
            <td>
                <a href="{{ url_for('atualizar', id=loop.index0) }}">Editar</a>
                <a href="{{ url_for('deletar', id=loop.index0) }}" onclick="return confirm('Tem certeza que deseja deletar este registro?');">Deletar</a>
            </td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
