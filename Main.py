from flask import Flask, render_template
from create import create_ 
from delete import delete
from read import read
from flask import Blueprint
central_page = Flask(__name__)

central_page.register_blueprint(read,url_prefix="/read")
central_page.register_blueprint(create_, url_prefix="/create")
central_page.register_blueprint(delete, url_prefix="/delete")

@central_page.route("/")
def Pagina_principal():
    return render_template('documentacao_api.html')

central_page.run(debug=True)