Documentação do Projeto - Caderno de Python

Estrutura do Site e Conteúdo

O site "Caderno de Python" é uma aplicação web interativa desenvolvida com Flask, contendo as seguintes seções:

1.
Página Inicial: Apresentação do site com links para as principais seções.

2.
Conteúdo Python: Seção informativa com páginas detalhadas sobre:

•
Estruturas de seleção (if, elif, else)

•
Estruturas de repetição (for, while)

•
Vetores e matrizes (listas e arrays)

•
Funções e procedimentos

•
Tratamentos de exceção



3.
Dicionário de Termos: Sistema CRUD completo para gerenciar termos de programação:

•
Visualização de todos os termos

•
Adição de novos termos

•
Edição de termos existentes

•
Exclusão de termos



4.
Tirar Dúvidas: Integração com a API do Gemini para responder perguntas sobre programação Python.

5.
Sobre a Equipe: Informações sobre os desenvolvedores do projeto.

Tecnologias Utilizadas

•
Linguagem de Programação: Python 3.x

•
Framework Web: Flask

•
Frontend: HTML, CSS, Bootstrap 5

•
Persistência de Dados: Arquivo CSV

•
Integração de IA: API Gemini (Google)

•
Bibliotecas Python:

•
Flask: Framework web

•
csv: Manipulação de arquivos CSV

•
google.generativeai: Integração com a API Gemini

•
markdown: Conversão de texto para HTML



Integração com a API do Gemini

A integração com a API do Gemini foi implementada da seguinte forma:

1.
Configuração: A API é configurada no início da aplicação usando uma chave de API.

2.
Interface de Usuário: Um formulário permite que os usuários enviem perguntas.

3.
Processamento: A pergunta é enviada para a API Gemini com um prompt contextual.

4.
Exibição: A resposta é formatada usando Markdown e exibida na página.

5.
Tratamento de Erros: Mensagens de erro são exibidas caso ocorra algum problema na comunicação com a API.

Como Executar a Aplicação

1.
Pré-requisitos:

•
Python 3.x instalado

•
Pip (gerenciador de pacotes Python)



2.
Instalação de Dependências:

3.
Configuração da API Gemini:

•
Obtenha uma chave de API do Google AI Studio

•
Substitua a variável GOOGLE_API_KEY no arquivo app.py pela sua chave



4.
Execução da Aplicação:

5.
Acesso:

•
Abra um navegador e acesse: http://localhost:5000



Principais Partes do Código

1.
Configuração da Aplicação Flask:

2.
Rotas para Páginas de Conteúdo:

3.
Manipulação do Dicionário de Termos:

4.
Integração com a API Gemini:

5.
Sistema de Templates:

•
Uso de herança de templates com Jinja2

•
Template base (modelo.html) com navegação e estrutura comum

•
Templates específicos para cada funcionalidade



Observações Importantes

•
A aplicação usa Bootstrap 5 para garantir responsividade em diferentes dispositivos.

•
O sistema de persistência utiliza arquivos CSV, o que é adequado para projetos educacionais, mas para aplicações em produção, um banco de dados seria mais apropriado.

•
Para usar a API Gemini, é necessário obter uma chave de API válida.

•
O código inclui tratamento de erros para lidar com problemas comuns, como arquivo não encontrado ou falha na API.

