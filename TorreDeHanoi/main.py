import time
import pygame
from pygame.locals import *
from sys import exit
from classes.Anilha import Anilha
from classes.Hastes import Haste
from collections import deque

# Presets da janela:
pygame.init()
tela = pygame.display.set_mode((1400, 790))
pygame.display.set_caption("Torre Hanoi")
clock = pygame.time.Clock()


# Função que define a fonte
def text(size=36, bold=False):
    font_path = r"TorreDeHanoi\fonte\arial.ttf"
    fonte_style = pygame.font.Font(font_path, size)
    if bold:
        fonte_style.set_bold(True)
    return fonte_style


# Definindo a variavél fonte
fonte = text(size=26, bold=True)


# Texto para o vencedor
def Vencedor(tela, clock):
    texto_Vencedor = fonte.render("Parabéns! Você conseguiu!", True, (0, 255, 0))
    posicao_Vencedor = (tela.get_width() // 2 - texto_Vencedor.get_width() // 2, tela.get_height() // 5.5)
    texto_VencedorMin = fonte.render("Parabéns! Você usou o menor número de movimentos possíveis!", True, (0, 250, 0))
    posicao_VencedorMin = (tela.get_width() // 2 - texto_VencedorMin.get_width() // 2, tela.get_height() // 5.5)

    while True:
        if movimentos == movimentos_min:
            tela.blit(texto_VencedorMin, posicao_VencedorMin)
        else:
            tela.blit(texto_Vencedor, posicao_Vencedor)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.update()
        clock.tick(60)


# Função que cria a tela de inicio
def tela_inicio(tela, clock):
    fonte = text()
    texto_instrucao = fonte.render("Pressione ESPAÇO para iniciar", True, (0, 0, 0))
    posicao_instrucao = (tela.get_width() // 2 - texto_instrucao.get_width() // 2, tela.get_height() // 2)

    # Carregamento do logo
    logo_path = r"TorreDeHanoi\images\Torre_Hanoi_Text_Logo.png"
    logo = pygame.image.load(logo_path).convert_alpha()
    posicao_titulo = (tela.get_width() // 2 - logo.get_width() // 2, tela.get_height() // 4)

    while True:
        tela.fill((255, 255, 255))  # Limpa a tela com a cor de fundo
        tela.blit(texto_instrucao, posicao_instrucao)
        tela.blit(logo, posicao_titulo)
        pygame.display.update()  # Atualize a tela

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return

        clock.tick(60)


def selecionar_num_anilhas(tela, clock):
    fonte = text()
    quantidade = 2
    while True:
        tela.fill((255, 255, 255))  # Limpa a tela com a cor de fundo
        texto_instrucao = fonte.render("Use as setas para escolher a quantidade de anilhas (2-10)", True, (0, 0, 0))
        texto_quantidade = fonte.render(f"Quantidade: {quantidade}", True, (0, 0, 0))
        posicao_instrucao = (tela.get_width() // 2 - texto_instrucao.get_width() // 2, tela.get_height() // 3)
        posicao_quantidade = (tela.get_width() // 2 - texto_quantidade.get_width() // 2, tela.get_height() // 2)

        tela.blit(texto_instrucao, posicao_instrucao)
        tela.blit(texto_quantidade, posicao_quantidade)
        pygame.display.update()  # Atualize a tela

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and quantidade < 10:
                    quantidade += 1
                elif event.key == pygame.K_DOWN and quantidade > 2:
                    quantidade -= 1
                elif event.key == pygame.K_RETURN:
                    return quantidade

        clock.tick(60)


def reiniciar_jogo():
    global anilha_stack, movimentos, anilhaSelecionada, Quant, movimentos_min
    Quant = 0
    #movimentos_min = 0
    movimentos = 0
    anilhaSelecionada = 0

    tela_inicio(tela, clock)

    # Redefinir as hastes
    for haste in hastes:
        haste.deque.clear()

    # Selecionar o número de anilhas novamente
    Quant = selecionar_num_anilhas(tela, clock)
    anilha_stack.clear()

    # Definir o número minimo de movimentos necessários novamente
    movimentos_min = 2 ** Quant - 1

    for i in range(Quant):
        anilha_stack.append(Anilhas[i])

    # Redefinir as posições das anilhas e adicioná-las à haste 1
    for i, anilha in enumerate(anilha_stack):
        anilha.set_pos(300, 760 - i * 17)
        haste1.deque.append(anilha)

# Chamando a função da tela de inicio
tela_inicio(tela, clock)

# Carregando os elementos:
# Criando a base:
superficie_base = pygame.image.load(r"TorreDeHanoi/images/base.jpg").convert()
superficie_base = pygame.transform.scale(superficie_base, (1380, 30))

# Criando as hastes:
haste1 = Haste(pygame.image.load(r"TorreDeHanoi/images/madeira.jpg").convert(), 300, 760)
haste2 = Haste(pygame.image.load(r"TorreDeHanoi/images/madeira.jpg").convert(), 700, 760)
haste3 = Haste(pygame.image.load(r"TorreDeHanoi/images/madeira.jpg").convert(), 1100, 760)

# Agrupando as hastes em uma tupla:
hastes = (haste1, haste2, haste3)

# Criando as anilhas:
anilha0 = Anilha(0, pygame.image.load(r"TorreDeHanoi/images/retanguloAzul.jpg").convert())
anilha1 = Anilha(1, pygame.image.load(r"TorreDeHanoi/images/retanguloAzulCiano.jpg").convert())
anilha2 = Anilha(2, pygame.image.load(r"TorreDeHanoi/images/retanguloAmarelo.jpg").convert())
anilha3 = Anilha(3, pygame.image.load(r"TorreDeHanoi/images/retanguloVermelho.jpg").convert())
anilha4 = Anilha(4, pygame.image.load(r"TorreDeHanoi/images/retanguloVerde.jpg").convert())
anilha5 = Anilha(5, pygame.image.load(r"TorreDeHanoi/images/retanguloRosa.jpg").convert())
anilha6 = Anilha(6, pygame.image.load(r"TorreDeHanoi/images/retanguloRoxo.jpg").convert())
anilha7 = Anilha(7, pygame.image.load(r"TorreDeHanoi/images/retangulocinza.jpg").convert())
anilha8 = Anilha(8, pygame.image.load(r"TorreDeHanoi/images/retanguloLaranja.jpg").convert())
anilha9 = Anilha(9, pygame.image.load(r"TorreDeHanoi/images/retanguloBege.jpg").convert())
Anilhas = [anilha9, anilha8, anilha7, anilha6, anilha5, anilha4, anilha3, anilha2, anilha1, anilha0]
# Stack das anilhas:
Quant = selecionar_num_anilhas(tela, clock)

# Stack das anilhas:
anilha_stack = deque()
for i in range(Quant):
    anilha_stack.append(Anilhas[i])

# anilhas = deque([
#    anilha0,
#    anilha1,
#    anilha2,
#    anilha3,
#    anilha4,
#    anilha5,
#    anilha6,
#    anilha7,
#    anilha8,
#    anilha9
# ])

# Definindo as posições das anilhas e adicionando-as à haste 1:
for i, anilha in enumerate(anilha_stack):
    anilha.set_pos(300, 760 - i * 17)
    # print(anilha.size)
    haste1.deque.append(anilha)

# Definindo o plano de fundo:
background = pygame.Surface((1400, 800))
background.fill("Azure")

# Definindo a variável que caberá a anilha de cima:
anilhaSelecionada = 0

movimentos_min = 2**Quant-1
movimentos = 0

# Criando o loop principal:
while True:
    # -------- Adicionando/Atualizando os elementos dinâmicos à tela:
    tela.blit(background, (0, 5))
    tela.blit(superficie_base, (10, 760))
    # Adicionando as hastes:
    for haste in hastes:
        tela.blit(haste.get_img(), haste.get_pos())

    # Adicionando as anilhas:
    for anilha in anilha_stack:
        tela.blit(anilha.get_img(), anilha.get_pos())

    # Desenhando o contador de movimentos e o número mínimos de movimentos
    texto_movimentos_min = fonte.render(f"Movimentos Minimos: {movimentos_min}", True, (0, 0, 0))
    tela.blit(texto_movimentos_min, (1080, 10))

    texto_movimentos = fonte.render(f"Movimentos: {movimentos}", True, (0, 0, 0))
    tela.blit(texto_movimentos, (10, 10))

    # Capturando a posição do mouse:
    mouse_pos = pygame.mouse.get_pos()

    # Capturando os eventos:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif len(haste2.deque) == Quant or len(haste3.deque) == Quant:
            Vencedor(tela, clock)
            print("Parabéns! Você conseguiu!")
            reiniciar_jogo()  # Chama a função para reiniciar o jogo

        elif event.type == pygame.MOUSEBUTTONUP:
            # Primeiro verifica se o clique foi em uma anilha
            for haste in hastes:
                if haste.deque and haste.deque[-1].get_pos().collidepoint(mouse_pos):
                    anilha = haste.deque[-1]
                    if anilhaSelecionada == 0:
                        # Seleciona a anilha do topo da haste clicada
                        anilhaSelecionada = haste.deque.pop()
                        anilhaSelecionada.set_pos(mouse_pos[0] - anilhaSelecionada.get_img().get_width() // 2, 200)
                    else:
                        # Verifica se a anilha pode ser colocada na haste clicada
                        if len(haste.deque) == 0 or anilhaSelecionada.size < haste.deque[-1].size:
                            haste.deque.append(anilhaSelecionada)
                            anilhaSelecionada.set_pos(haste.get_pos()[0] + 15, 779 - 17 * len(haste.deque))
                            anilhaSelecionada = 0
                            movimentos += 1
                    break
            else:
                # Caso nenhuma anilha tenha sido clicada, verifica se o clique foi em uma haste
                for haste in hastes:
                    if haste.get_pos().collidepoint(mouse_pos):
                        if anilhaSelecionada == 0:
                            try:
                                anilhaSelecionada = haste.deque.pop()
                                anilhaSelecionada.set_pos(mouse_pos[0] - anilhaSelecionada.get_img().get_width() // 2,
                                                          200)
                            except IndexError:
                                pass
                        else:
                            if len(haste.deque) == 0 or anilhaSelecionada.size < haste.deque[-1].size:
                                haste.deque.append(anilhaSelecionada)
                                anilhaSelecionada.set_pos(haste.get_pos()[0] + 15, 779 - 17 * len(haste.deque))
                                anilhaSelecionada = 0
                                movimentos += 1
                        break

    # Atualizando a tela:
    pygame.display.update()
    clock.tick(60)
