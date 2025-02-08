# test_app.py
import unittest
import json
from unittest.mock import patch, MagicMock
from app import app, users, socketio

class AppTestCase(unittest.TestCase):
    def setUp(self):
        # Configura o ambiente de teste
        app.testing = True
        self.client = app.test_client()
        users.clear()  # Limpa os usuários registrados antes de cada teste

    # Testes para o endpoint /register
    def test_register_success(self):
        # Cadastro de novo usuário com sucesso
        response = self.client.post('/register', json={'email': 'teste@example.com', 'password': 'senha123'})
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data.get('message'), 'Usuário registrado com sucesso!')
        self.assertIn('teste@example.com', users)

    def test_register_duplicate(self):
        # Cadastro duplicado deve retornar erro
        self.client.post('/register', json={'email': 'teste@example.com', 'password': 'senha123'})
        response = self.client.post('/register', json={'email': 'teste@example.com', 'password': 'senha123'})
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertEqual(data.get('error'), 'Email já registrado')

    # Testes para o endpoint /login
    def test_login_success(self):
        # Usuário cadastrado e login com credenciais corretas
        self.client.post('/register', json={'email': 'teste@example.com', 'password': 'senha123'})
        response = self.client.post('/login', json={'email': 'teste@example.com', 'password': 'senha123'})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('access_token', data)

    def test_login_invalid_email(self):
        # Tentativa de login com email inexistente
        response = self.client.post('/login', json={'email': 'inexistente@example.com', 'password': 'senha123'})
        self.assertEqual(response.status_code, 401)
        data = response.get_json()
        self.assertEqual(data.get('error'), 'Credenciais inválidas')

    def test_login_invalid_password(self):
        # Tentativa de login com senha incorreta
        self.client.post('/register', json={'email': 'teste@example.com', 'password': 'senha123'})
        response = self.client.post('/login', json={'email': 'teste@example.com', 'password': 'senhaErrada'})
        self.assertEqual(response.status_code, 401)
        data = response.get_json()
        self.assertEqual(data.get('error'), 'Credenciais inválidas')

    # Testes para o endpoint GET /promocoes
    @patch('app.PromocaoController.listar_promocoes')
    def test_listar_promocoes(self, mock_listar):
        # Cria um objeto de promoção falso com método to_dict
        fake_promocao = MagicMock()
        fake_promocao.to_dict.return_value = {'id': 1, 'name': 'Promoção Teste'}
        mock_listar.return_value = [fake_promocao]

        response = self.client.get('/promocoes')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['id'], 1)
        self.assertEqual(data[0]['name'], 'Promoção Teste')

    # Testes para o endpoint POST /promocoes
    @patch('app.PromocaoController.criar_promocao')
    def test_criar_promocao_success(self, mock_criar):
        # Simula criação de promoção com sucesso
        mock_criar.return_value = None
        payload = {"campo_exemplo": "valor"}
        response = self.client.post('/promocoes', json=payload)
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data.get('message'), 'Promoção criada com sucesso!')

    @patch('app.PromocaoController.criar_promocao')
    def test_criar_promocao_failure(self, mock_criar):
        # Simula exceção na criação de promoção
        mock_criar.side_effect = Exception("Erro ao criar promoção")
        payload = {"campo_exemplo": "valor"}
        response = self.client.post('/promocoes', json=payload)
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertEqual(data.get('error'), 'Erro ao criar promoção')

    # Testes para o endpoint PUT /promocoes/<id>
    @patch('app.PromocaoController.editar_promocao')
    def test_editar_promocao_success(self, mock_editar):
        # Simula edição de promoção com sucesso
        mock_editar.return_value = None
        payload = {"campo_exemplo": "novo_valor"}
        response = self.client.put('/promocoes/1', json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data.get('message'), 'Promoção editada com sucesso!')

    @patch('app.PromocaoController.editar_promocao')
    def test_editar_promocao_failure(self, mock_editar):
        # Simula exceção na edição de promoção
        mock_editar.side_effect = Exception("Erro ao editar promoção")
        payload = {"campo_exemplo": "novo_valor"}
        response = self.client.put('/promocoes/1', json=payload)
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertEqual(data.get('error'), 'Erro ao editar promoção')

    # Testes para o endpoint PATCH /promocoes/<id>/status
    @patch('app.PromocaoController.alterar_status_promocao')
    def test_alterar_status_promocao_success(self, mock_alterar):
        # Simula alteração de status com sucesso
        mock_alterar.return_value = None
        payload = {"status": "ativo"}
        response = self.client.patch('/promocoes/1/status', json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data.get('message'), 'Status da promoção alterado com sucesso!')

    @patch('app.PromocaoController.alterar_status_promocao')
    def test_alterar_status_promocao_failure(self, mock_alterar):
        # Simula exceção na alteração de status
        mock_alterar.side_effect = Exception("Erro ao alterar status")
        payload = {"status": "inativo"}
        response = self.client.patch('/promocoes/1/status', json=payload)
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertEqual(data.get('error'), 'Erro ao alterar status')

    # Teste para o endpoint GET /regioes
    @patch('app.get_connection')
    def test_listar_regioes(self, mock_get_connection):
        # Cria uma conexão e cursor falsos com dados simulados
        fake_cursor = MagicMock()
        fake_cursor.fetchall.return_value = [
            (1, 'SP', 'São Paulo'),
            (2, 'RJ', 'Rio de Janeiro')
        ]
        fake_connection = MagicMock()
        fake_connection.cursor.return_value = fake_cursor
        mock_get_connection.return_value = fake_connection

        response = self.client.get('/regioes')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['id'], 1)
        self.assertEqual(data[0]['nome'], 'SP - São Paulo')
        self.assertEqual(data[1]['id'], 2)
        self.assertEqual(data[1]['nome'], 'RJ - Rio de Janeiro')

    # Teste para a conexão via SocketIO
    def test_socketio_connect(self):
        # Cria um cliente de teste do SocketIO e verifica se a conexão foi estabelecida
        test_client = socketio.test_client(app)
        self.assertTrue(test_client.is_connected())
        test_client.disconnect()

if __name__ == '__main__':
    unittest.main()
