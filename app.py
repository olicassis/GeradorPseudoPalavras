# Imports
from flask import Flask, render_template, request, json
from gerador import busca_palavras as bp

# App
app = Flask(__name__)

## Routes
# Página inicial
@app.route('/')
def index():
    myString = 'form_words.html'
    return render_template('index.html',myString=myString)

# Exibe a lista de palavras encontradas
@app.route('/listarPalavras',methods=['GET','POST'])
def listarPalavras():
    _canonicidade = request.form['canonicity']
    _tonicidade = request.form['tonicity']
    lista_palavras = bp(_canonicidade,_tonicidade)
    with open('templates/words_list.html','w') as html:
        html.write('<form action="/gerarPseudoPalavras" method="POST">\n')
        html.write('    Escolha as palavras fonte desejadas para gerar pseudo-palavras:\n')
        html.write('    <br><br>\n')
        html.write('    <div class="form-group"> \n')
        for p in lista_palavras:
            html.write('    <input type="checkbox" id="{}" name="{}" value="{}">\n  <label for="{}"> {} </label><br>'.format(p,p,p,p,p))
        html.write('    </div>')
        html.write('    <button type="submit" class="btn btn-default">Gerar Pseudo-Palavras</button>')
        html.write('</form>')
    myString = 'words_list.html'
    return render_template('index.html',myString=myString)

# Roda a aplicação
if __name__ == '__main__':
    app.run(debug=True)