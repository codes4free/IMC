
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

<h2>Conclusão</h2>

<p>
    Este código representa uma aplicação web básica que permite gerenciar registros de indivíduos e calcular seus IMCs. Serve como um exemplo introdutório para aplicações Flask que implementam operações CRUD. Com melhorias adicionais, pode ser expandido para um sistema mais robusto e completo.
</p>



<!-- ... As seções anteriores permanecem as mesmas ... -->

<hr>

<h2>Desenvolvimento do Projeto no Google Cloud Shell Editor</h2>

<p>
    Esta seção descreve como o projeto foi desenvolvido utilizando o <strong>Google Cloud Shell Editor</strong>, uma ferramenta baseada em navegador que fornece um ambiente de desenvolvimento completo na nuvem.
</p>

<h3>Passo a Passo para Criar o Projeto</h3>

<ol>
    <li>
        <strong>Acessar o Google Cloud Shell</strong>:
        <p>
            Faça login na sua conta do Google Cloud Platform e acesse o Cloud Shell clicando no ícone do terminal no canto superior direito da console.
        </p>
        <!-- Descrição da imagem -->
        <p><em>[Imagem: Captura de tela do ícone do Cloud Shell na console do Google Cloud]</em></p>
        ![Alt text](https://i.ibb.co/XZBtTLW/ggl-shell-editor.jpg)
        <img src="https://i.ibb.co/XZBtTLW/ggl-shell-editor.jpg" width="300" />
    </li>
    </li>
    <li>
        <strong>Iniciar o Cloud Shell Editor</strong>:
        <p>
            Uma vez que o terminal do Cloud Shell estiver aberto, clique no botão "Open Editor" para abrir o editor integrado.
        </p>
        <!-- Descrição da imagem -->
        <p><em>[Imagem: Botão "Open Editor" no terminal do Cloud Shell]</em></p>
    </li>
    <li>
        <strong>Criar um Novo Projeto Flask</strong>:
        <p>
            No editor, crie uma nova pasta para o projeto e abra um novo arquivo chamado <code>app.py</code>.
        </p>
        <!-- Descrição da imagem -->
        <p><em>[Imagem: Estrutura de pastas no Cloud Shell Editor mostrando o arquivo app.py]</em></p>
    </li>
    <li>
        <strong>Escrever o Código</strong>:
        <p>
            Insira o código da aplicação Flask no arquivo <code>app.py</code> conforme descrito nas seções anteriores.
        </p>
        <!-- Descrição da imagem -->
        <p><em>[Imagem: Código sendo escrito no arquivo ap


<hr>

FERNANDO FERREIRA MARQUES <br>
SUPERIOR DE TECNOLOGIA EM DEVOPS <br>
RA: 3778442502

</body>

