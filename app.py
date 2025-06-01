import google.generativeai as genai
from flask import Flask, render_template, url_for, request, redirect
from markupsafe import Markup
import csv
import markdown

# Configuração da API Gemini
GOOGLE_API_KEY = "AIzaSyAdkPiWFviYfdDrmJmoyqF0uI9Ox10BV7U"  
genai.configure(api_key=GOOGLE_API_KEY)

app = Flask(__name__)

@app.route('/') 
def ola():
    return render_template('index.html')

@app.route('/sobre-equipe')
def sobre_equipe():
    return render_template('sobre_equipe.html')

# Rotas para as páginas de conteúdo Python
@app.route('/estruturas-selecao')
def estruturas_selecao():
    return render_template('estruturas_selecao.html')

@app.route('/estruturas-repeticao')
def estruturas_repeticao():
    return render_template('estruturas_repeticao.html')

@app.route('/vetores-matrizes')
def vetores_matrizes():
    return render_template('vetores_matrizes.html')

@app.route('/funcoes-procedimentos')
def funcoes_procedimentos():
    return render_template('funcoes_procedimentos.html')

@app.route('/tratamentos-excecao')
def tratamentos_excecao():
    return render_template('tratamentos_excecao.html')

# Rotas para o glossário
@app.route('/glossario')
def glossario():
    glossario_de_termos = []

    try:
        with open('bd_glossario.csv', 'r', newline='', encoding='utf-8') as arquivo:
            reader = csv.reader(arquivo, delimiter=';')
            for linha in reader:
                glossario_de_termos.append(linha)
    except FileNotFoundError:
        # Cria o arquivo se não existir
        with open('bd_glossario.csv', 'w', newline='', encoding='utf-8') as arquivo:
            pass
    return render_template('glossario.html', glossario=glossario_de_termos)

@app.route('/novo-termo')
def novo_termo():
    return render_template('novo_termo.html')

@app.route('/criar_termo', methods=['POST'])
def criar_termo():
    termo = request.form['termo']
    definicao = request.form['definicao']

    with open('bd_glossario.csv', 'a', newline='', encoding='utf-8') as arquivo:
        writer = csv.writer(arquivo, delimiter=';')
        writer.writerow([termo, definicao])

    return redirect(url_for('glossario'))

@app.route('/editar-termo/<int:indice>')
def editar_termo_form(indice):
    glossario_de_termos = []
    
    with open('bd_glossario.csv', 'r', newline='', encoding='utf-8') as arquivo:
        reader = csv.reader(arquivo, delimiter=';')
        for linha in reader:
            glossario_de_termos.append(linha)
    
    if indice < 0 or indice >= len(glossario_de_termos):
        return redirect(url_for('glossario'))
    
    termo = glossario_de_termos[indice]
    return render_template('editar_termo.html', termo=termo, indice=indice)

@app.route('/atualizar-termo/<int:indice>', methods=['POST'])
def atualizar_termo(indice):
    termo = request.form['termo']
    definicao = request.form['definicao']
    
    glossario_de_termos = []
    
    with open('bd_glossario.csv', 'r', newline='', encoding='utf-8') as arquivo:
        reader = csv.reader(arquivo, delimiter=';')
        for linha in reader:
            glossario_de_termos.append(linha)
    
    if indice < 0 or indice >= len(glossario_de_termos):
        return redirect(url_for('glossario'))
    
    # Atualiza o termo na lista
    glossario_de_termos[indice] = [termo, definicao]
    
    # Reescreve todo o arquivo com a lista atualizada
    with open('bd_glossario.csv', 'w', newline='', encoding='utf-8') as arquivo:
        writer = csv.writer(arquivo, delimiter=';')
        for linha in glossario_de_termos:
            writer.writerow(linha)
    
    return redirect(url_for('glossario'))

@app.route('/excluir-termo/<int:indice>')
def excluir_termo(indice):
    glossario_de_termos = []
    
    with open('bd_glossario.csv', 'r', newline='', encoding='utf-8') as arquivo:
        reader = csv.reader(arquivo, delimiter=';')
        for linha in reader:
            glossario_de_termos.append(linha)
    
    if indice < 0 or indice >= len(glossario_de_termos):
        return redirect(url_for('glossario'))
    
    # Remove o termo da lista
    del glossario_de_termos[indice]
    
    # Reescreve todo o arquivo com a lista atualizada
    with open('bd_glossario.csv', 'w', newline='', encoding='utf-8') as arquivo:
        writer = csv.writer(arquivo, delimiter=';')
        for linha in glossario_de_termos:
            writer.writerow(linha)
    
    return redirect(url_for('glossario'))


# Rotas para a seção de tirar dúvidas
@app.route('/tirar-duvidas')
def tirar_duvidas():
    return render_template('tirar_duvidas.html')

@app.route('/responder-duvida', methods=['POST'])
def responder_duvida():
    pergunta = request.form['pergunta']
    
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Contextualizar o Gemini par que ele elabore respostas focadas
        prompt = f"""
        Você é um assistente especializado em programação Python. 
        Por favor, responda à seguinte pergunta de forma clara, 
        com exemplos de código quando apropriado:
        
        {pergunta}
        """
        
        # Gerar resposta
        response = model.generate_content(prompt)
        
        # Converter a resposta para HTML usando Markdown
        resposta_html = Markup(markdown.markdown(response.text))
        
        return render_template('tirar_duvidas.html', 
                              pergunta=pergunta, 
                              resposta=resposta_html)
    
    except Exception as e:
        erro = f"Ocorreu um erro ao processar sua pergunta: {str(e)}"
        return render_template('tirar_duvidas.html', 
                              pergunta=pergunta, 
                              resposta=Markup(f"<p class='text-danger'>{erro}</p><p>Talvez a API esteja desativada.</p>"))

if __name__ == '__main__':
    app.run(debug=True)
