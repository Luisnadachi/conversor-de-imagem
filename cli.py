from PIL import Image
from cykooz.heif.pil import register_heif_opener
import os

lista_imagem = os.listdir("images")

for imagens in lista_imagem:

    register_heif_opener()
    imagemOriginal = Image.open(f"images/{imagens}")

    imagemOriginal.save(f'converteds/{imagens.replace("avif", "png")}')