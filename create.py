from flask import Flask,Blueprint

home = Blueprint("/create",__name__)

@home.route("/")
def create()
