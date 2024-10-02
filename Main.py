from flask import Flask, render_template
from create import create_ 
from delete import delete
from update import update_page
from read import read
from flask import Blueprint
app = Flask(__name__)

app.register_blueprint(read,url_prefix="/read")
app.register_blueprint(create_, url_prefix="/create")
app.register_blueprint(delete, url_prefix="/delete")
app.register_blueprint(update_page, url_prefix="/update")


@app.route("/")
def Pagina_principal():
    return render_template('documentacao_api.html')

app.run(debug=True)