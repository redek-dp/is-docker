from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Olá! Este Flask está rodando no Docker.000000000"

if __name__ == '__main__':
    # host='0.0.0.0' é essencial para que o container seja acessível externamente
    # app.run(host='0.0.0.0', port=5000)
    app.run(host='0.0.0.0', port=5000, debug=True)