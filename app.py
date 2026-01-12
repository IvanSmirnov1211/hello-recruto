from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name', 'Recruto')
    message = request.args.get('message', 'Давай дружить')
    return f"Hello {name}! {message}!"

if __name__ == '__main__':
    # Слушаем все интерфейсы, порт 8080 (не требует прав администратора)
    app.run(host='0.0.0.0', port=8080, debug=False)