# test_database.py
import unittest
from unittest.mock import MagicMock, patch, call
from models.database import create_tables

class TestCreateTables(unittest.TestCase):
    @patch("models.database.get_connection")
    def test_create_tables_execution(self, mock_get_connection):
        """
        Testa se a função create_tables executa todas as queries esperadas,
        realiza o commit e fecha a conexão corretamente.
        """
        # Cria mocks para conexão e cursor
        fake_cursor = MagicMock()
        fake_connection = MagicMock()
        fake_connection.cursor.return_value = fake_cursor
        mock_get_connection.return_value = fake_connection

        # Executa a função que cria as tabelas
        create_tables()

        # Verifica se o cursor foi obtido
        fake_connection.cursor.assert_called_once()

        # Verifica se o commit foi chamado
        fake_connection.commit.assert_called_once()

        # Verifica se o cursor e a conexão foram fechados
        fake_cursor.close.assert_called_once()
        fake_connection.close.assert_called_once()

        # Obtém as queries executadas via execute
        execute_calls = fake_cursor.execute.call_args_list
        queries = [args[0] for args, _ in execute_calls]

        # Valida a criação da tabela de agendamentos
        self.assertTrue(any("CREATE TABLE IF NOT EXISTS agendamentos" in query for query in queries),
                        "Query de criação da tabela 'agendamentos' não foi executada.")

        # Valida a criação da tabela de status
        self.assertTrue(any("CREATE TABLE IF NOT EXISTS status" in query for query in queries),
                        "Query de criação da tabela 'status' não foi executada.")

        # Valida a inserção do status padrão
        self.assertTrue(any("INSERT OR IGNORE INTO status" in query for query in queries),
                        "Query de inserção do status padrão não foi executada.")

        # Valida a criação da tabela de histórico de alterações
        self.assertTrue(any("CREATE TABLE IF NOT EXISTS historico_alteracoes" in query for query in queries),
                        "Query de criação da tabela 'historico_alteracoes' não foi executada.")

        # Valida a criação da tabela de regiões
        self.assertTrue(any("CREATE TABLE IF NOT EXISTS regioes" in query for query in queries),
                        "Query de criação da tabela 'regioes' não foi executada.")

        # Valida a inserção dos estados (regiões) via executemany
        fake_cursor.executemany.assert_called_once()
        executemany_args = fake_cursor.executemany.call_args[0]
        self.assertIn("INSERT OR IGNORE INTO regioes", executemany_args[0],
                      "Query de inserção das regiões não foi executada corretamente.")

        # Valida a criação da tabela associativa entre promoções e regiões
        self.assertTrue(any("CREATE TABLE IF NOT EXISTS promocoes_regioes" in query for query in queries),
                        "Query de criação da tabela 'promocoes_regioes' não foi executada.")

if __name__ == '__main__':
    unittest.main()
