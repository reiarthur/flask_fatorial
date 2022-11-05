from flask import Flask
from flask import jsonify

app = Flask(__name__)
@app.route('/<numero>')
def fatorial_numero(numero):
    numero = int(numero)
    resultado = 1
    count = 1
    while count <= numero:
        resultado *= count
        count += 1
    return jsonify({'fatorial':resultado,
                    'numero':numero})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)