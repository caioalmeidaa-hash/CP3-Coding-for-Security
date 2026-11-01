from flask import Flask,request,render_template_string
app=Flask(__name__);alertas=[]
HTML="""<h1>Alertas</h1><form method=post><input name=descricao required><button>Salvar</button></form><ul>{% for a in alertas %}<li>{{a}}</li>{% endfor %}</ul>"""
@app.route('/',methods=['GET','POST'])
def inicio():
    if request.method=='POST':
        d=request.form.get('descricao','')
        if d:alertas.append(d[:500])
    return render_template_string(HTML,alertas=alertas)
if __name__=='__main__':app.run(port=5003,debug=False)
