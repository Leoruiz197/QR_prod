import segno
import os
import re

def gerar_qrcode(nome_produto, pasta="qrcodes"):
    os.makedirs(pasta, exist_ok=True)  # Cria a pasta se não existir
    
    # Remove caracteres inválidos do nome do arquivo
    nome_arquivo = re.sub(r'[\\/*?:"<>|]', "_", nome_produto)
    
    # QR Code só com o nome do produto
    qr = segno.make(nome_produto)
    
    caminho = os.path.join(pasta, f"{nome_arquivo}.png")
    qr.save(caminho, scale=10)  # Scale = tamanho do QR Code
    print(f"✅ QR Code gerado para '{nome_produto}' em: {caminho}")


if __name__ == "__main__":
    produto = input("Digite o nome do produto: ")
    gerar_qrcode(produto)