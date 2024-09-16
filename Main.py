from flask import Flask, render_template
from create import app as create_page
app = Flask(__name__)
app.register_blueprint(create_page, url_prefix="/create/")
@app.route("/")
def Pagina_principal():
    return render_template('pagina_principal.html')

app.run(debug=True)