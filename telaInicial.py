import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageSequence
import subprocess
import os
import pygame

def exibir_imagem_estatica(canvas, caminho_imagem):
    """
    Exibe uma imagem estática no canvas.

    Args:
      canvas: O canvas onde a imagem será exibida.
      caminho_imagem: O caminho para o arquivo de imagem.
    """
    imagem = Image.open(caminho_imagem)
    imagem_tk = ImageTk.PhotoImage(imagem)
    canvas.create_image(0, 0, image=imagem_tk, anchor="nw")
    canvas.image = imagem_tk  # Mantém uma referência para evitar que a imagem seja coletada pelo garbage collector

def torre_de_hanoi():
    try:
        torreDeHanoi = os.path.join("TorreDeHanoi", "main.py")
        subprocess.Popen(["python", torreDeHanoi])
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível iniciar o jogo Torre de Hanoi.\nErro: {e}")

def tiro_ao_alvo():
    try:
        tiroAoAlvo = os.path.join("TiroAoAlvo", "main.py")
        subprocess.Popen(["python", tiroAoAlvo])
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível iniciar o jogo Tiro ao Alvo.\nErro: {e}")
        
def passa_repassa():
    try:
        passaRepassa = os.path.join("PassaRepassa", "main.py")
        subprocess.Popen(["python", passaRepassa])
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível iniciar o jogo Passa Repassa.\nErro: {e}")

def sair():
    janela.quit()

def selecionar_jogo(indice):
    som_clique.play()
    if indice == 0:
        torre_de_hanoi()
    elif indice == 1:
        tiro_ao_alvo()
    elif indice == 2:
        passa_repassa()
    elif indice == 3:
        sair()

def menuInicial():
    """
    Cria e exibe o menu inicial da aplicação.
    """
    global janela, som_clique
    janela = tk.Tk()
    janela.title("Menu de Jogos")
    janela.geometry("1024x600")

    pygame.init()
    som_clique = pygame.mixer.Sound("sounds/click.mp3")  # Carrega o som de clique

    #  Imagem de Fundo
    canvas = tk.Canvas(janela, width=1024, height=600)
    canvas.pack(fill="both", expand=True)
    caminho_imagem_fundo = "images/tela_inicial.jpg"
    exibir_imagem_estatica(canvas, caminho_imagem_fundo)

    #  Imagem do Título
    caminho_imagem_titulo = "images/super_jogos.png"
    imagem_titulo = Image.open(caminho_imagem_titulo)

    # Redimensiona a imagem do título
    nova_largura = 350
    nova_altura = int(imagem_titulo.height * (nova_largura / imagem_titulo.width))
    imagem_titulo = imagem_titulo.resize((nova_largura, nova_altura), Image.LANCZOS)
    imagem_titulo_tk = ImageTk.PhotoImage(imagem_titulo)

    canvas.create_image(512, 50, image=imagem_titulo_tk, anchor="n")
    canvas.image_titulo = imagem_titulo_tk  # Mantém uma referência para evitar que a imagem seja coletada pelo garbage collector

    jogos = ["Torre de Hanoi", "Tiro ao Alvo", "Passa Repassa","Sair"]
    botoes = []
    largura_botao = 200
    altura_botao = 50

    for i, jogo in enumerate(jogos):
        botao = tk.Button(
            janela,
            text=jogo,
            font=("Arial", 16),
            bg="#808080",
            fg="white",
            activebackground="#A9A9A9",
            activeforeground="white",
            bd=0,
            cursor="hand2",
            command=lambda indice=i: selecionar_jogo(indice)
        )

        # Posiciona o botão na janela com um tamanho fixo
        botao.place(x=412, y=300 + i * 70, width=largura_botao, height=altura_botao)
        botoes.append(botao)  # Adiciona o botão à lista de botões

    def navegar_jogos(event):
        """
        Permite navegar pelos botões usando as teclas de seta e Enter.

        Args:
          event: O evento de teclado.
        """
        nonlocal selecionado
        if event.keysym == "Down":  # Se a tecla pressionada for seta para baixo
            selecionado = (selecionado + 1) % len(botoes)
            atualizar_botoes()
        elif event.keysym == "Up":  # Se a tecla pressionada for seta para cima
            selecionado = (selecionado - 1) % len(botoes)
            atualizar_botoes()
        elif event.keysym == "Return":  # Se a tecla pressionada for Enter
            selecionar_jogo(selecionado)

    def atualizar_botoes():
        for i, botao in enumerate(botoes):
            if i == selecionado:  # Se o botão atual for o selecionado
                botao.config(bg="#A9A9A9")
            else:  # Caso contrário
                botao.config(bg="#808080")

    selecionado = 0
    atualizar_botoes()

    janela.bind("<Key>", navegar_jogos)
    janela.mainloop()

if __name__ == "__main__":
    menuInicial()