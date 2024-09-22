from flask import Flask, render_template
from create import app as create_page
from delete import app as delete_page
app = Flask(__name__)
app.register_blueprint(create_page, url_prefix="/create")

app.register_blueprint(delete_page, url_prefix='/delete')
@app.route("/")
def Pagina_principal():
    return render_template('documentacao_api.html')
app.run(debug=True)