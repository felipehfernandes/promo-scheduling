from models.database import create_tables
from controllers.promocao_controller import PromocaoController
from views.promocao_view import PromocaoView

def main():
    create_tables()
    while True:
        print("\n1. Criar Promoção")
        print("2. Listar Promoções")
        print("3. Editar Promoção")
        print("4. Excluir Promoção")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            dados = PromocaoView.solicitar_dados_promocao()
            PromocaoController.criar_promocao(*dados)
        elif opcao == "2":
            promocoes = PromocaoController.listar_promocoes()
            PromocaoView.exibir_promocoes(promocoes)
        elif opcao == "3":
            id = int(input("ID da Promoção a editar: "))
            dados = PromocaoView.solicitar_dados_promocao()
            PromocaoController.editar_promocao(id, *dados)
        elif opcao == "4":
            id = int(input("ID da Promoção a excluir: "))
            PromocaoController.excluir_promocao(id)
        elif opcao == "5":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
