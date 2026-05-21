from tkinter import *
from PIL import Image, ImageTk
import requests
import ctypes
import os
import textwrap
from dotenv import load_dotenv

imagem_ancora = None

#--------------------------------------------------------------------------------------------------------------------------------------------------------
def requisicaoNASA(texto_inicial, texto_explanation, label_imagem):
    global imagem_ancora

    load_dotenv()
    api_key = os.getenv("NASA_API_KEY")
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

    resposta = requests.get(url)
    if resposta.status_code == 403:
        texto_inicial["text"] = "Erro 403: Limite de requisições atingido. Tente novamente mais tarde."
        texto_explanation["text"] = "A API da NASA tem um limite de requisições diárias. Por favor, aguarde e tente novamente amanhã."
        return
    
    assert resposta.status_code == 200, f"Expected status code 200, but got {resposta.status_code}"

    dados= resposta.json()

    if dados.get("media_type") != "image":
        print("O conteúdo do dia não é uma imagem.")
        texto_inicial["text"] = "Hoje a NASA postou um vídeo, não uma imagem."
        texto_explanation["text"] = f"Link do vídeo: {dados['url']}"
        return

    texto_inicial["text"] = f"Title: {dados['title']}"

    texto_curto = textwrap.fill(dados['explanation'], width=60)
    texto_explanation["text"] = f"Explicação:\n{texto_curto}"

    url_imagem = dados['url']
    imagem_resposta = requests.get(url_imagem)

    nome_arquivo = "wallpaper_NASA.jpg"
    with open(nome_arquivo, "wb") as arquivo:
        arquivo.write(imagem_resposta.content)


    img_original = Image.open(nome_arquivo).convert("RGB")
    
    img_original.thumbnail((350, 250)) 
    
    imagem_ancora = ImageTk.PhotoImage(img_original)
    
    label_imagem.config(image=imagem_ancora)

    caminho_completo = os.path.abspath(nome_arquivo)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, caminho_completo, 3)
#--------------------------------------------------------------------------------------------------------------------------------------------------------

def main():
    janela = Tk()
    janela.title("Cosmo Wallpaper Engine")
    janela.geometry("600x500")

    texto_inicial = Label(janela, text="", font=("Arial", 12, "bold"))
    texto_inicial.pack(padx=10, pady=10)

    label_foto = Label(janela, text="Foto do Dia da NASA", font=("Arial", 14))
    label_foto.pack(padx=10, pady=10)

    texto_explanation = Label(janela, text="", justify="left", anchor="w")
    texto_explanation.pack(padx=10, pady=10)

    label_imagem = Label(janela, text="Imagem do Dia", font=("Arial", 12))
    label_imagem.pack(padx=10, pady=10)

    botao = Button(janela, text="Mudar Papel de Parede com a Foto da NASA", command=lambda: requisicaoNASA(texto_inicial, texto_explanation, label_imagem), bg="#1a73e8", fg="white", padx=10, pady=10)
    botao.pack(padx=10, pady=20)

    janela.mainloop()

if __name__ == "__main__":
    main()