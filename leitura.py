from pyzbar.pyzbar import decode
from PIL import Image

# Função para processar QR Codes de uma imagem
def processar_qrcodes(imagem_path):
    """
    Lê um QR Code de uma imagem e retorna os dados em uma lista.
    """
    if not imagem_path:
        raise ValueError("Você precisa passar o caminho da imagem para processar_qrcodes")

    try:
        img = Image.open(imagem_path)
        decoded_objects = decode(img)
        resultados = [obj.data.decode('utf-8') for obj in decoded_objects]
        return resultados
    except Exception as e:
        print(f"Erro ao processar QR Code '{imagem_path}': {e}")
        return []