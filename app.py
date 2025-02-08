from models.database import create_tables
from controllers.promocao_controller import PromocaoController
from views.promocao_view import PromocaoView
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash
from config import get_connection
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
jwt = JWTManager(app)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# Modelo de Usuário
users = {}

@app.route('/register', methods=['POST'])
def register():
    email = request.json.get('email')
    password = request.json.get('password')
    if email in users:
        return jsonify({'error': 'Email já registrado'}), 400
    users[email] = generate_password_hash(password)
    return jsonify({'message': 'Usuário registrado com sucesso!'}), 201

@app.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    user_password_hash = users.get(email)
    if not user_password_hash or not check_password_hash(user_password_hash, password):
        return jsonify({'error': 'Credenciais inválidas'}), 401
    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token), 200

@app.route('/promocoes', methods=['GET'])
def listar_promocoes():
    promocoes = PromocaoController.listar_promocoes()
    promocoes_dict = [promocao.to_dict() for promocao in promocoes]
    return jsonify(promocoes_dict)

@app.route('/promocoes', methods=['POST'])
def criar_promocao():
    try:
        dados = request.json
        PromocaoController.criar_promocao(**dados)
        return jsonify({'message': 'Promoção criada com sucesso!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/promocoes/<int:id>', methods=['PUT'])
def editar_promocao(id):
    try:
        dados = request.json
        PromocaoController.editar_promocao(id, **dados)
        return jsonify({'message': 'Promoção editada com sucesso!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/promocoes/<int:id>/status', methods=['PATCH'])
def alterar_status_promocao(id):
    try:
        dados = request.json
        PromocaoController.alterar_status_promocao(id, **dados)
        return jsonify({'message': 'Status da promoção alterado com sucesso!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/regioes', methods=['GET'])
def listar_regioes():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT id, uf, estado FROM regioes")
    regioes = cursor.fetchall()
    cursor.close()
    connection.close()
    regioes_list = [{'id': regiao[0], 'nome': f"{regiao[1]} - {regiao[2]}"} for regiao in regioes]
    return jsonify(regioes_list)

@socketio.on('connect')
def handle_connect():
    print('A client connected')

def main():
    while True:
        print("\n1. Criar Promoção")
        print("2. Listar Promoções")
        print("3. Editar Promoção")
        print("4. Alterar Status da Promoção")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            dados = PromocaoView.solicitar_dados_promocao()
            regioes_ids = PromocaoView.solicitar_regioes()
            PromocaoController.criar_promocao(*dados, regioes_ids)
        elif opcao == "2":
            promocoes = PromocaoController.listar_promocoes()
            PromocaoView.exibir_promocoes(promocoes)
        elif opcao == "3":
            id = input("Digite o ID da Promoção a editar: ")
            dados = PromocaoView.solicitar_dados_promocao_edicao()
            PromocaoController.editar_promocao(id, *dados)
        elif opcao == "4":
            dados = PromocaoView.solicitar_dados_alteracao_status()
            PromocaoController.alterar_status_promocao(*dados)
        elif opcao == "5":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=5000)
else:
    main()
