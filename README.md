# QR_prod

Leitor e gerador de QR Code integrado com JSON.

## Instalação

1. **Clone o repositório**  
   ```bash
   git clone <url-do-repositorio>
   cd QR_prod
   ```

2. **Crie um ambiente virtual (opcional, recomendado)**  
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Instale as dependências**  
   ```bash
   pip install -r requirements.txt
   ```

## Como usar

1. **Execute o programa**  
   ```bash
   python main.py
   ```

2. **Menu principal**  
   - Ler QR Code
   - Gerar QR Code
   - Limpar JSON
   - Limpar QRs
   - Sair

3. **Funções**
   - **Ler QR Code:** Leia códigos QR e salve os dados no arquivo JSON.
   - **Gerar QR Code:** Crie QR Codes básicos ou personalizados.
   - **Limpar JSON:** Apaga todos os dados do arquivo JSON.
   - **Limpar QRs:** Remove todos os arquivos de QR gerados.

## Observações

- Os QR Codes gerados ficam na pasta `qrcodes`.
- O arquivo de dados é `dados.json`.
- Personalize cores e estilos ao gerar QR Codes.

---
Feito com Python, Pillow