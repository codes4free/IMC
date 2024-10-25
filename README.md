
<body>

<h1>Documentação do Código</h1>

<p>
    Este documento descreve detalhadamente o funcionamento do código fornecido, que é uma aplicação web construída usando o framework <strong>Flask</strong> em Python. A aplicação permite ao usuário realizar operações <strong>CRUD</strong> (Criar, Ler, Atualizar e Deletar) relacionadas ao cálculo do <strong>Índice de Massa Corporal (IMC)</strong> de diferentes indivíduos.
</p>

<hr>

<h2>Importações e Configuração Inicial</h2>

<pre><code>from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)</code></pre>

<ul>
    <li><strong>Flask</strong>: Framework web utilizado para criar a aplicação.</li>
    <li><strong>render_template</strong>: Função para renderizar templates HTML.</li>
    <li><strong>request</strong>: Objeto que lida com dados da requisição HTTP.</li>
    <li><strong>redirect</strong>: Função para redirecionar o usuário para outra rota.</li>
    <li><strong>url_for</strong>: Função para construir URLs para funções específicas.</li>
</ul>

<p>
    A aplicação é inicializada criando uma instância da classe <code>Flask</code>.
</p>

<hr>

<h2>Armazenamento de Dados</h2>

<pre><code>registros = []</code></pre>

<ul>
    <li><strong>registros</strong>: Lista que armazena os dados dos usuários. Cada item é um dicionário contendo informações sobre um indivíduo (nome, peso, altura e IMC).</li>
</ul>

<hr>

<h2>Função para Cálculo do IMC</h2>

<pre><code>def calcular_imc(peso, altura):
    return peso / (altura ** 2)</code></pre>

<ul>
    <li><strong>calcular_imc</strong>: Função que recebe o peso e a altura de um indivíduo e retorna o cálculo do IMC.</li>
</ul>

<hr>

<h2>Rotas da Aplicação</h2>

<h3>Rota Principal (<code>/</code>)</h3>

<pre><code>@app.route('/')
def index():
    return render_template('index.html', registros=registros)</code></pre>

<ul>
    <li><strong>Descrição</strong>: Renderiza a página inicial da aplicação.</li>
    <li><strong>Funcionalidade</strong>: Exibe a lista de registros armazenados.</li>
</ul>

<hr>

<h3>Rota para Criar um Novo Registro (<code>/criar</code>)</h3>

<pre><code>@app.route('/criar', methods=['GET', 'POST'])
def criar():
    if request.method == 'POST':
        nome = request.form['nome']
        peso = float(request.form['peso'])
        altura = float(request.form['altura'])
        imc = calcular_imc(peso, altura)
        registro = {'nome': nome, 'peso': peso, 'altura': altura, 'imc': imc}
        registros.append(registro)
        return redirect(url_for('index'))
    return render_template('criar.html')</code></pre>

<ul>
    <li><strong>Métodos HTTP Permitidos</strong>: <code>GET</code> e <code>POST</code>.</li>
    <li><strong>GET</strong>: Renderiza o formulário para criação de um novo registro.</li>
    <li><strong>POST</strong>:
        <ul>
            <li>Recebe os dados do formulário.</li>
            <li>Converte <b>peso</b> e altura para <b>float</b>.</li>
            <li>Calcula o IMC utilizando a função <b>calcular_imc</b>.</li>
            <li>Cria um dicionário <b>registro</b> com os dados fornecidos.</li>
            <li>Adiciona o novo registro à lista <b>registros</b>.</li>
            <li>Redireciona o usuário para a página inicial.</li>
        </ul>
    </li>
</ul>

<hr>

<h3>Rota para Atualizar um Registro Existente (<code>/atualizar/&lt;int:id&gt;</code>)</h3>

<pre><code>@app.route('/atualizar/&lt;int:id&gt;', methods=['GET', 'POST'])
def atualizar(id):
    if id >= len(registros) or id &lt; 0:
        return "Registro não encontrado", 404
    registro = registros[id]
    if request.method == 'POST':
        nome = request.form['nome']
        peso = float(request.form['peso'])
        altura = float(request.form['altura'])
        imc = calcular_imc(peso, altura)
        registros[id] = {'nome': nome, 'peso': peso, 'altura': altura, 'imc': imc}
        return redirect(url_for('index'))
    return render_template('atualizar.html', id=id, registro=registro)</code></pre>

<ul>
    <li><strong>Parâmetro</strong>: <code>id</code> (índice do registro na lista).</li>
    <li><strong>Métodos HTTP Permitidos</strong>: <code>GET</code> e <code>POST</code>.</li>
    <li><strong>Validação</strong>: Verifica se o <code>id</code> fornecido é válido.</li>
    <li><strong>GET</strong>: Renderiza o formulário pré-preenchido com os dados atuais do registro.</li>
    <li><strong>POST</strong>:
        <ul>
            <li>Recebe os dados atualizados do formulário.</li>
            <li>Atualiza o registro correspondente na lista <code>registros</code>.</li>
            <li>Redireciona o usuário para a página inicial.</li>
        </ul>
    </li>
</ul>

<hr>

<h3>Rota para Deletar um Registro (<code>/deletar/&lt;int:id&gt;</code>)</h3>

<pre><code>@app.route('/deletar/&lt;int:id&gt;')
def deletar(id):
    if id >= len(registros) or id &lt; 0:
        return "Registro não encontrado", 404
    registros.pop(id)
    return redirect(url_for('index'))</code></pre>

<ul>
    <li><strong>Parâmetro</strong>: <code>id</code> (índice do registro na lista).</li>
    <li><strong>Validação</strong>: Verifica se o <code>id</code> fornecido é válido.</li>
    <li><strong>Funcionalidade</strong>: Remove o registro correspondente da lista <code>registros</code> e redireciona para a página inicial.</li>
</ul>

<hr>

<h2>Execução da Aplicação</h2>

<pre><code>if __name__ == '__main__':
    app.run(debug=True)</code></pre>

<ul>
    <li><strong>Modo de Depuração</strong>: O aplicativo é executado com <code>debug=True</code>, o que permite atualizações em tempo real e fornece um debugger interativo em caso de erros.</li>
</ul>

<hr>

<h2>Considerações Gerais</h2>

<ul>
    <li><strong>Armazenamento em Memória</strong>: Os dados são armazenados em uma lista na memória volátil. Isso significa que todos os registros serão perdidos quando a aplicação for reiniciada.</li>
    <li><strong>Validação de Dados</strong>: Não há validação robusta dos dados inseridos pelo usuário. Em um ambiente de produção, seria necessário implementar verificações adicionais.</li>
    <li><strong>Templates HTML</strong>: A aplicação depende de templates HTML (<code>index.html</code>, <code>criar.html</code>, <code>atualizar.html</code>) para renderizar as páginas. Esses arquivos devem estar presentes na pasta <code>templates</code>.</li>
</ul>

<hr>

<h2>Fluxo da Aplicação</h2>

<ol>
    <li>
        <strong>Página Inicial</strong>:
        <ul>
            <li>Exibe todos os registros armazenados.</li>
            <li>Oferece opções para criar, atualizar ou deletar registros.</li>
        </ul>
    </li>
    <li>
        <strong>Criar Registro</strong>:
        <ul>
            <li>O usuário acessa <code>/criar</code>.</li>
            <li>Preenche o formulário com nome, peso e altura.</li>
            <li>Submete o formulário para adicionar um novo registro.</li>
        </ul>
    </li>
    <li>
        <strong>Atualizar Registro</strong>:
        <ul>
            <li>O usuário acessa <code>/atualizar/&lt;id&gt;</code>, onde <code>&lt;id&gt;</code> é o índice do registro.</li>
            <li>O formulário é pré-preenchido com os dados atuais.</li>
            <li>O usuário modifica os campos desejados e submete o formulário.</li>
        </ul>
    </li>
    <li>
        <strong>Deletar Registro</strong>:
        <ul>
            <li>O usuário acessa <code>/deletar/&lt;id&gt;</code>.</li>
            <li>O aplicativo remove o registro e atualiza a lista exibida.</li>
        </ul>
    </li>
</ol>

<hr>

<h2>Possíveis Melhorias</h2>

<ul>
    <li><strong>Persistência de Dados</strong>: Implementar um banco de dados (por exemplo, SQLite ou MySQL) para armazenar os registros de forma persistente.</li>
    <li><strong>Validação e Sanitização</strong>: Adicionar validação de entrada para prevenir erros e possíveis vulnerabilidades de segurança.</li>
    <li><strong>Interface do Usuário</strong>: Melhorar a aparência e usabilidade das páginas HTML utilizando CSS e JavaScript.</li>
    <li><strong>Mensagens de Feedback</strong>: Fornecer mensagens claras de sucesso ou erro após cada operação.</li>
</ul>

<hr>

<h2>Desenvolvimento do Projeto no Google Cloud Shell</h2>

<p>
    Esta seção descreve como o projeto foi desenvolvido utilizando o <strong>Google Cloud Shell</strong>, um ambiente de desenvolvimento integrado baseado em navegador.
</p>


<li>
<strong>Criar o Projeto Flask</strong>:

<p>
    No editor, crie uma nova pasta para o projeto e crie o arquivo <code>app.py</code> com o código da aplicação.
</p>
<a href="https://ibb.co/BVDBR3f"><img src="https://i.ibb.co/XZBtTLW/ggl-shell-editor.jpg" alt="ggl-shell-editor" border="0"></a>

</li>

<li>
<strong>Instalar Dependências</strong>:

<p>
    No terminal, instale o Flask usando o comando:
</p>

<pre><code>pip install Flask</code></pre>



<li>
<strong>Executar a Aplicação</strong>:

<p>
    Execute a aplicação com o comando:
</p>

<pre><code>python app.py</code></pre>

<p>
    A aplicação será iniciada e estará acessível através de uma URL fornecida pelo Cloud Shell.
</p>

<p><em>[Imagem: Terminal mostrando a aplicação em execução]</em></p>
<p>![Executar a Aplicação](link-da-imagem)</p>
</li>

<li>
<strong>Acessar a Aplicação</strong>:

<p>
    Clique na URL fornecida para abrir a aplicação em uma nova aba do navegador e interaja com ela.
</p>

<p><em>[Imagem: Página inicial da aplicação no navegador]</em></p>
<p>![Acessar a Aplicação](link-da-imagem)</p>
</li>
</ol>

<hr>

<h2>Feedback sobre o Programa</h2>

<p>
    O programa funciona conforme esperado, permitindo que os usuários:
</p>

<ul>
    <li><strong>Criem</strong> novos registros com nome, peso e altura.</li>
    <li><strong>Visualizem</strong> a lista de registros e seus respectivos IMCs.</li>
    <li><strong>Atualizem</strong> registros existentes.</li>
    <li><strong>Deletem</strong> registros indesejados.</li>
</ul>

<p>
    A interface é simples e direta, facilitando a interação do usuário com a aplicação.
</p>

<hr>

<h2>Possíveis Melhorias</h2>

<ul>
    <li><strong>Persistência de Dados</strong>: Implementar um banco de dados para armazenar os registros de forma persistente.</li>
    <li><strong>Validação de Dados</strong>: Adicionar validações para garantir a integridade dos dados inseridos.</li>
    <li><strong>Interface do Usuário</strong>: Melhorar o design das páginas HTML usando CSS e frameworks como Bootstrap.</li>
    <li><strong>Mensagens de Feedback</strong>: Fornecer feedback ao usuário após cada operação (por exemplo, mensagens de sucesso ou erro).</li>
</ul>

<hr>

<h2>Licença</h2>

<p>
    Este projeto está licenciado sob os termos da licença MIT.
</p>

<hr>

</body>
</html>




<h2>Conclusão</h2>

<p>
    Este código representa uma aplicação web básica que permite gerenciar registros de indivíduos e calcular seus IMCs. Serve como um exemplo introdutório para aplicações Flask que implementam operações CRUD. Com melhorias adicionais, pode ser expandido para um sistema mais robusto e completo.
</p>



<!-- ... As seções anteriores permanecem as mesmas ... -->







FERNANDO FERREIRA MARQUES <br>
SUPERIOR DE TECNOLOGIA EM DEVOPS <br>
RA: 3778442502

</body>

