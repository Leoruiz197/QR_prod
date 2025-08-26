import qrcode

def gerar_qr():
    nome_produto = input("Digite o nome do produto: ")

    qr = qrcode.QRCode(
        version =1, 
        error_correction = qrcode.constants.ERROR_CORRECT_H,
        box_size = 10, 
        border = 4
    )

    qr.add_data(nome_produto.title())
    qr.make(fit = True)

    img = qr.make_image(fill_color="black", back_color="white")

    img.save(f"./qrcodes/{nome_produto.lower()}.png")
    print("QRcode gerado com sucesso")

if __name__ == "__main__":
    gerar_qr()