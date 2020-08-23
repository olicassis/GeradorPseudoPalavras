# Imports
from flask import Flask, render_template, request, json,send_file
from gerador import busca_palavras as bp
from gerador import gerar_silabas as gs
from gerador import get_pseudo_palavras as gpp
from random import seed,randint
from pandas import read_csv,ExcelWriter
from pre_processamento.funcoesAuxiliares import tonicidade,canonicidade
import os

# Caminho absoluto do arquivo de saída
path = os.path.relpath("files/pseudoPalavras.xlsx")

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
            html.write('    <input type="checkbox" id="{}" name="list" value="{}">\n  <label for="{}"> {} </label><br>'.format(p,p,p,p))
        html.write('    </div>')
        html.write('    <button type="submit" class="btn btn-default">Gerar Pseudo-Palavras</button>\n')
        html.write('</form>')
    myString = 'words_list.html'
    return render_template('index.html',myString=myString)

# Gera pseudo-palavras a partir das palavras escolhidas
@app.route('/gerarPseudoPalavras',methods=['GET','POST'])
def gerarPseudoPalavras():
    lista_palavras = request.form.getlist('list')
    pseudo_palavras = []
    silabas = gs(lista_palavras)
    seed(version=2)
    for palavra in lista_palavras:
        n_pseudo = 2 + randint(0,99) % 4
        pseudo_palavras += gpp(palavra,n_pseudo,silabas)
    with open("files/pseudoPalavras.csv",'w') as arq:
        arq.write("palavra,canonicidade,tonicidade\n")
        for p in pseudo_palavras:
            string = p + ',' + str(canonicidade(p)) + ',' + tonicidade(p) + '\n'
            arq.write(string)  
    df_csv = read_csv('files/pseudoPalavras.csv')
    writer = ExcelWriter('files/pseudoPalavras.xlsx')
    df_csv.to_excel(writer,index=True)
    writer.save()
    with open('templates/exportado.html','w') as html:
        html.write('<h1>Arquivo pronto para download!</h1>')
        html.write('<a download href="/download"> <button class="btn btn-default" type="button">Download</button> </a>')
    myString = 'exportado.html'
    return render_template('index.html',myString=myString)

@app.route('/download')
def return_file():
	return send_file(path, as_attachment=True)

# Roda a aplicação
if __name__ == '__main__':
    app.run(debug=True)