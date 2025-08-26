import qrcode
import os
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer, SquareModuleDrawer, CircleModuleDrawer

from PIL import Image

class GeradorQRCode:
    def __init__(self):
        self.pasta_saida = "qrcodes"
        self.criar_pasta_saida()
    
    def criar_pasta_saida(self):
        """Cria pasta para salvar os QR codes se não existir"""
        if not os.path.exists(self.pasta_saida):
            os.makedirs(self.pasta_saida)
    
    def gerar_qrcode_basico(self):
        """Gera um QR Code básico"""
        print("\n=== GERADOR DE QR CODE BÁSICO ===")
        
        texto = input("Digite o texto: ").strip()
        if not texto:
            print("❌ Texto não pode estar vazio!")
            return
        
        # Solicita o nome do arquivo
        nome_arquivo = texto
        if not nome_arquivo:
            nome_arquivo = "qrcode"
        
        try:
            # Cria o QR Code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            
            qr.add_data(texto)
            qr.make(fit=True)
            
            # Gera a imagem
            img = qr.make_image(fill_color="black", back_color="white")
            
            # Salva o arquivo
            caminho_arquivo = os.path.join(self.pasta_saida, f"{nome_arquivo}.png")
            img.save(caminho_arquivo)
            
            print(f"✅ QR Code salvo em: {caminho_arquivo}")
            
        except Exception as e:
            print(f"❌ Erro ao gerar QR Code: {e}")
    
    def gerar_qrcode_personalizado(self):
        """Gera um QR Code com opções de personalização"""
        print("\n=== GERADOR DE QR CODE PERSONALIZADO ===")
        
        # Solicita o texto
        texto = input("Digite o texto: ").strip()
        if not texto:
            print("❌ Texto não pode estar vazio!")
            return
        
        # Configurações de correção de erro
        print("\nNível de correção de erro:")
        print("1 - Baixo (~7%)")
        print("2 - Médio (~15%)")
        print("3 - Alto (~25%)")
        print("4 - Muito Alto (~30%)")
        
        nivel_erro = input("Escolha o nível (1-4) [padrão: 2]: ").strip()
        niveis = {
            '1': qrcode.constants.ERROR_CORRECT_L,
            '2': qrcode.constants.ERROR_CORRECT_M,
            '3': qrcode.constants.ERROR_CORRECT_Q,
            '4': qrcode.constants.ERROR_CORRECT_H
        }
        error_correction = niveis.get(nivel_erro, qrcode.constants.ERROR_CORRECT_M)
        
        # Tamanho do QR Code
        try:
            box_size = int(input("Tamanho dos quadrados (1-50) [padrão: 10]: ") or "10")
            box_size = max(1, min(50, box_size))
        except ValueError:
            box_size = 10
        
        # Borda
        try:
            border = int(input("Tamanho da borda (1-20) [padrão: 4]: ") or "4")
            border = max(1, min(20, border))
        except ValueError:
            border = 4
        
        # Cores
        cor_frente = input("Cor dos quadrados (ex: black, #000000) [padrão: black]: ").strip() or "black"
        cor_fundo = input("Cor do fundo (ex: white, #FFFFFF) [padrão: white]: ").strip() or "white"
        
        # Nome do arquivo
        nome_arquivo = texto
        if not nome_arquivo:
            nome_arquivo = "qrcode_personalizado"
        
        try:
            # Cria o QR Code
            qr = qrcode.QRCode(
                version=1,
                error_correction=error_correction,
                box_size=box_size,
                border=border,
            )
            
            qr.add_data(texto)
            qr.make(fit=True)
            
            # Gera a imagem
            img = qr.make_image(fill_color=cor_frente, back_color=cor_fundo)
            
            # Salva o arquivo
            caminho_arquivo = os.path.join(self.pasta_saida, f"{nome_arquivo}.png")
            img.save(caminho_arquivo)
            
            print(f"✅ QR Code personalizado salvo em: {caminho_arquivo}")
            
        except Exception as e:
            print(f"❌ Erro ao gerar QR Code: {e}")
    
    

    def listar_qrcodes(self):
        """Lista todos os QR codes salvos"""
        print(f"\n=== QR CODES SALVOS EM '{self.pasta_saida}' ===")
        
        try:
            arquivos = [f for f in os.listdir(self.pasta_saida) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
            
            if not arquivos:
                print("📁 Nenhum QR Code encontrado.")
                return
            
            print(f"📁 Total de arquivos: {len(arquivos)}")
            for i, arquivo in enumerate(arquivos, 1):
                caminho_completo = os.path.join(self.pasta_saida, arquivo)
                tamanho = os.path.getsize(caminho_completo)
                print(f"{i:2d}. {arquivo} ({tamanho:,} bytes)")
                
        except Exception as e:
            print(f"❌ Erro ao listar arquivos: {e}")
    
    def abrir_pasta_qrcodes(self):
        """Abre a pasta onde os QR codes são salvos"""
        try:
            if os.name == 'nt':  # Windows
                os.startfile(self.pasta_saida)
            elif os.name == 'posix':  # macOS e Linux
                os.system(f'open "{self.pasta_saida}"' if os.uname().sysname == 'Darwin' else f'xdg-open "{self.pasta_saida}"')
            print(f"📂 Pasta '{self.pasta_saida}' aberta.")
        except Exception as e:
            print(f"❌ Erro ao abrir pasta: {e}")
            print(f"📁 Pasta manual: {os.path.abspath(self.pasta_saida)}")
    
    def mostrar_info(self):
        """Mostra informações sobre o programa"""
        print("\n=== INFORMAÇÕES ===")
        print("🔍 Gerador de QR Code em Python")
        print("📦 Biblioteca utilizada: qrcode")
        print(f"📁 Pasta de saída: {os.path.abspath(self.pasta_saida)}")
        print("🎨 Suporte a personalização de cores e estilos")
        print("📱 Compatible com qualquer leitor de QR Code")
        print("\n💡 Dicas:")
        print("• Textos longos podem gerar QR codes maiores")
        print("• Cores claras podem dificultar a leitura")
        print("• Para melhor qualidade, use correção de erro alta")

def mostrar_menu():
    """Exibe o menu principal"""
    print("\n" + "="*50)
    print("🔳  GERADOR DE QR CODE  🔳".center(50))
    print("="*50)
    print("1️⃣  Gerar QR Code Básico")
    print("2️⃣  Gerar QR Code Personalizado")
    print("3️⃣  Listar QR Codes Salvos")
    print("4️⃣  Abrir Pasta de QR Codes")
    print("5️⃣  Informações")
    print("0️⃣  Sair")
    print("="*50)

def main():
    """Função principal do programa"""
    gerador = GeradorQRCode()
    
    print("🔳 Bem-vindo ao Gerador de QR Code! 🔳")
    
    while True:
        try:
            mostrar_menu()
            opcao = input("Escolha uma opção: ").strip()
            
            if opcao == '1':
                gerador.gerar_qrcode_basico()
            elif opcao == '2':
                gerador.gerar_qrcode_personalizado()
            elif opcao == '3':
                gerador.listar_qrcodes()
            elif opcao == '4':
                gerador.abrir_pasta_qrcodes()
            elif opcao == '5':
                gerador.mostrar_info()
            elif opcao == '0':
                print("\n👋 Obrigado por usar o Gerador de QR Code!")
                break
            else:
                print("❌ Opção inválida! Tente novamente.")
            
            # Pausa para o usuário ver o resultado
            input("\n⏸️  Pressione Enter para continuar...")
            
        except KeyboardInterrupt:
            print("\n\n👋 Programa encerrado pelo usuário.")
            break
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")
            input("⏸️  Pressione Enter para continuar...")

if __name__ == "__main__":
    main()