from produtos import adicionar_produto, ler_produtos
from geracaoQrcode import gerar_qrcode

def main():
    nome_produto = input("Digite o nome do produto: ")

    # Adiciona ou atualiza o produto no JSON
    adicionar_produto(nome_produto)

    # Gera QR Code automaticamente na pasta 'qrcodes'
    gerar_qrcode(nome_produto)

    # Lista todos os produtos cadastrados
    produtos = ler_produtos()
    print("\nProdutos cadastrados:")
    for p in produtos:
        print(f"{p['nome']} - Quantidade: {p['quantidade']}")

if __name__ == "__main__":
    main()