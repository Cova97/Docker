from app import app

@app.route('/')
def hello():
    return "¡Funciona en Docker! 🐳"