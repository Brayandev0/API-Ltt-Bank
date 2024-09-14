from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def Pagina_principal():
    return render_template('pagina_principal.html')

app.run(debug=True)