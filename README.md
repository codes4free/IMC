
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


<head>
    <title>Documentação do Código</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
        }
        h1, h2, h3, h4 {
            color: #2F4F4F;
        }
        code {
            background-color: #F5F5F5;
            padding: 5px;
            font-family: Consolas, monospace;
        }
        pre {
            background-color: #F5F5F5;
            padding: 15px;
            overflow: auto;
            font-family: Consolas, monospace;
            font-size: 12pt;
            white-space: pre-wrap;
            line-height: 1.5;
        }
        hr {
            border: none;
            height: 1px;
            background-color: #D3D3D3;
            margin: 20px 0;
        }
        ul {
            margin-left: 20px;
        }
    </style>
</head>
<body>

<h1>Documentação do Código</h1>

<!-- ... As seções anteriores permanecem as mesmas ... -->

<hr>

<h2>Desenvolvimento do Projeto no GitHub</h2>

<p>
    Esta seção descreve como o projeto foi desenvolvido e versionado utilizando o <strong>GitHub</strong>, uma plataforma de hospedagem de código-fonte e colaboração em projetos de software.
</p>

<h3>Passo a Passo para Criar o Projeto</h3>

<ol>
    <li>
        <strong>Criar um Repositório no GitHub</strong>:
        <p>
            Acesse o GitHub e crie um novo repositório para o projeto, fornecendo um nome e uma descrição adequados.
        </p>
        <!-- Espaço para imagem -->
        <p><em>[Imagem: Captura de tela da criação de um novo repositório no GitHub]</em></p>
    </li>
    <li>
        <strong>Clonar o Repositório Localmente</strong>:
        <p>
            Utilize o comando <code>git clone</code> para clonar o repositório em sua máquina local.
        </p>
        <pre><code>git clone https://github.com/usuario/nome-do-repositorio.git</code></pre>
        <!-- Espaço para imagem -->
        <p><em>[Imagem: Terminal mostrando o comando git clone sendo executado]</em></p>
    </li>
    <li>
        <strong>Criar o Ambiente de Desenvolvimento</strong>:
        <p>
            Navegue até o diretório do projeto e crie um ambiente virtual para gerenciar as dependências.
        </p>
        <pre><code>cd nome-do-repositorio
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate</code></pre>
        <!-- Espaço para imagem -->
        <p><em>[Imagem: Terminal mostrando a ativação do ambiente virtual]</em></p>
    </li>
    <li>
        <strong>Instalar Dependências</strong>:
        <p>
            Instale o Flask utilizando o pip.
        </p>
        <pre><code>pip install Flask</code></pre>
        <!-- Espaço para imagem -->
        <p><em>[Imagem: Terminal mostrando a instalação do Flask]</em></p>
    </li>
    <li>
        <strong>Adicionar o Código ao Repositório</strong>:
        <p>
            Crie o arquivo <code>app.py</code> e insira o código da aplicação Flask conforme descrito nas seções anteriores.
        </p>
        <!-- Espaço para imagem -->
        <p><em>[Imagem: Editor de código mostrando o arquivo app.py com o código]</em></p>
    </li>
    <li>
        <strong>Criar a Estrutura de Templates</strong>:
        <p>
            Crie uma pasta chamada <code>templates</code> e adicione os arquivos <code>index.html</code>, <code>criar.html</code> e <code>atualizar.html</code>.
        </p>
        <!-- Espaço para imagem -->
        <p><em>[Imagem: Estrutura de pastas mostrando a pasta templates e os arquivos HTML]</em></p>
    </li>
    <li>
        <strong>Testar a Aplicação Localmente</strong>:
        <p>
            Execute a aplicação para verificar se tudo está funcionando corretamente.
        </p>
        <pre><code>python app.py</code></pre>
        <!-- Espaço para imagem -->
        <p><em>[Imagem: Terminal mostrando a aplicação em execução]</em></p>
    </li>
    <li>
        <strong>Fazer Commit e Push das Alterações</strong>:
        <p>
            Adicione os arquivos ao controle de versão, faça commit e envie as alterações para o GitHub.
        </p>
        <pre><code>git add .
git commit -m "Inicialização do projeto"
git push origin main</code></pre>
        <!-- Espaço para imagem -->
        <p><em>[Imagem: Terminal mostrando os comandos git add, git commit e git push]</em></p>
    </li>
    <li>
        <strong>Configurar o GitHub Pages (Opcional)</strong>:
        <p>
            Se desejar hospedar a aplicação estática no GitHub Pages, configure as opções no repositório.
        </p>
        <!-- Espaço para imagem -->
        <p><em>[Imagem: Configurações do GitHub Pages no repositório]</em></p>
    </li>
</ol>

<h3>Vantagens de Usar o GitHub</h3>

<ul>
    <li><strong>Controle de Versão</strong>: Histórico completo das alterações feitas no projeto.</li>
    <li><strong>Colaboração</strong>: Facilita o trabalho em equipe através de pull requests e issues.</li>
    <li><strong>Hospedagem Centralizada</strong>: O código está acessível de qualquer lugar.</li>
</ul>

<p>
    Utilizando o GitHub, o projeto ganha em organização, rastreabilidade e colaboração, permitindo que desenvolvedores trabalhem juntos de forma eficiente.
</p>

<hr>




FERNANDO FERREIRA MARQUES <br>
SUPERIOR DE TECNOLOGIA EM DEVOPS <br>
RA: 3778442502

</body>

