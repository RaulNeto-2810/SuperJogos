import random
import pygame
import time

pygame.init()
largura = 900
altura = 700
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Tiro ao Alvo")

dificuldades = {"fácil": 80, "médio": 60, "difícil": 40}

dificuldade_atual = "fácil"
alvo_raio = dificuldades[dificuldade_atual]

alvo = (0, 255, 255)
alvox = largura // 2
alvoy = altura // 2

funcionando = True
score = 0
recorde = 0
tempo_inicial = time.time()
tempo_maximo = 10


def desenharalvo():
    pygame.draw.circle(tela, alvo, (alvox, alvoy), alvo_raio)


def novo_alvo():
    global alvox, alvoy
    alvox = random.randint(alvo_raio, largura - alvo_raio)
    alvoy = random.randint(alvo_raio, altura - alvo_raio)


def atualizar_dificuldade():
    global dificuldade_atual, alvo_raio
    if score >= 80 and dificuldade_atual == "fácil":
        dificuldade_atual = "médio"
        alvo_raio = dificuldades[dificuldade_atual]
    elif score >= 240 and dificuldade_atual == "médio":
        dificuldade_atual = "difícil"
        alvo_raio = dificuldades[dificuldade_atual]


def verificar_click_alvo():
    global score, dificuldade_atual, alvo_raio
    mouse_pos = pygame.mouse.get_pos()
    distancia = ((alvox - mouse_pos[0])**2 + (alvoy - mouse_pos[1])**2)**0.5
    if distancia <= alvo_raio:
        score += 10
        novo_alvo()
        atualizar_dificuldade()
    else:
        if dificuldade_atual == "fácil":
            score = 0
        elif dificuldade_atual == "médio":
            score -= 50
            if score < 0:
                score = 0
            if score < 80:
                dificuldade_atual = "fácil"
                alvo_raio = dificuldades[dificuldade_atual]
        elif dificuldade_atual == "difícil":
            score -= 20
            if score < 0:
                score = 0
            if score < 240:
                dificuldade_atual = "médio"
                alvo_raio = dificuldades[dificuldade_atual]


def desenhar_botao(texto, x, y, largura, altura, cor, cor_texto):
    pygame.draw.rect(tela, cor, (x, y, largura, altura))
    fonte = pygame.font.Font(None, 36)
    texto_renderizado = fonte.render(texto, True, cor_texto)
    tela.blit(texto_renderizado,
              (x + (largura - texto_renderizado.get_width()) // 2, y +
               (altura - texto_renderizado.get_height()) // 2))


def verificar_click_botao(x, y, largura, altura):
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    if mouse_pos[0] >= x and mouse_pos[0] <= x + largura and mouse_pos[
            1] >= y and mouse_pos[1] <= y + altura:
        if mouse_click[0] == 1:
            return True
    return False


def resetar_jogo():
    global score, dificuldade_atual, alvo_raio, tempo_inicial, funcionando
    score = 0
    dificuldade_atual = "fácil"
    alvo_raio = dificuldades[dificuldade_atual]
    tempo_inicial = time.time()
    novo_alvo()
    funcionando = True


def sair_jogo():
    pygame.quit()
    exit()


while True:
    tempo_atual = time.time()
    tempo_decorrido = tempo_atual - tempo_inicial
    tempo_restante = max(tempo_maximo - tempo_decorrido, 0)

    if tempo_restante == 0 and funcionando:
        funcionando = False

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if funcionando:
                verificar_click_alvo()
            else:
                if verificar_click_botao(350, 450, 200, 50):
                    resetar_jogo()
                if verificar_click_botao(350, 520, 200, 50):
                    sair_jogo()

    tela.fill((0, 0, 0))

    if funcionando:
        desenharalvo()

        fonte = pygame.font.Font(None, 36)
        texto_pontuacao = fonte.render(f"Pontuação: {score}", True,
                                       (255, 255, 255))
        tela.blit(texto_pontuacao, (10, 10))

        texto_dificuldade = fonte.render(f"Dificuldade: {dificuldade_atual}",
                                         True, (255, 255, 255))
        tela.blit(texto_dificuldade, (10, 50))

        texto_tempo = fonte.render(f"Tempo Restante: {int(tempo_restante)}s",
                                   True, (255, 255, 255))
        tela.blit(texto_tempo, (10, 90))

        texto_recorde = fonte.render(
            f"Recorde da última jogada: {recorde} pontos", True,
            (255, 255, 255))
        tela.blit(texto_recorde, (10, 130))
    else:
        fonte = pygame.font.Font(None, 36)
        texto_final = fonte.render(f"A sua pontuação foi de {score} pontos",
                                   True, (255, 255, 255))
        texto_final2 = fonte.render(f"Na dificuldade {dificuldade_atual}",
                                    True, (255, 255, 255))
        texto_recorde = fonte.render(
            f"Recorde da última jogada: {recorde} pontos", True,
            (255, 255, 255))
        tela.blit(texto_final, (200, 200))
        tela.blit(texto_final2, (250, 300))
        tela.blit(texto_recorde, (250, 350))

        desenhar_botao("Reiniciar", 350, 450, 200, 50, (0, 255, 0),
                       (255, 255, 255))
        desenhar_botao("Sair", 350, 520, 200, 50, (0, 255, 0), (255, 255, 255))

    pygame.display.flip()

    if not funcionando and score > recorde:
        recorde = score

pygame.quit()
