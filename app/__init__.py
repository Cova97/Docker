from flask import Flask

app = Flask(__name__)

# Importar rutas al final para evitar circular imports
from app.routes import *