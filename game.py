import pygame
from random import randint
import pygame.mixer

pygame.init()
x = 430  # max 550, min 110
y = 350
pos_x = 400
pos_y_pista1 = 800
pos_y_pista2 = 1200
pos_y_pista3 = 1600
pos_y_pista4 = 1800
vel = 10
vel_outros = 20
timer = 0
fator_vel_pista1 = 0
fator_vel_pista2 = 0
fator_vel_pista3 = 0
fator_vel_pista4 = 0
indice_pista1 = 0
indice_pista2 = 0
indice_pista3 = 0
indice_pista4 = 0
flag = 0
flag_1 = 0
flag_2 = 0
flag_3 = 0
flag_pos = 0

fator_mult = 0

pygame.mixer.init()
batida = [pygame.mixer.Sound('batida_1.wav'), pygame.mixer.Sound('batida_2.wav'), pygame.mixer.Sound('batida_3.wav'),
          pygame.mixer.Sound('batida_4.wav'), pygame.mixer.Sound('batida_5.wav')]
indice_batida = 0
freada = pygame.mixer.Sound('freada_1.wav')
virar = pygame.mixer.Sound('virar.wav')
motor = pygame.mixer.Sound('motor.ogg')
acelerar = pygame.mixer.Sound('acelerar.wav')
motor.play(-1)
trilha = pygame.mixer.Sound('trilha.ogg')
trilha.play(-1)

fundo = pygame.image.load('background.png')
carro = pygame.image.load('car.png')
pista1 = pygame.image.load('taxi.png')
pista2 = pygame.image.load('police.png')
pista3 = pygame.image.load('green_car.png')
pista4 = pygame.image.load('ferrari.png')
carros = [pista1, pista2, pista3, pista4]

font = pygame.font.SysFont('arial black', 20)
texto_xp = font.render("XP: ", True, (255, 255, 255), (155, 100, 50))
texto_pontos = font.render("TOTAL: ", True, (255, 255, 255), (155, 100, 50))

pos_texto = texto_xp.get_rect()
pos_texto.center = (410, 10)
xp = -4

janela = pygame.display.set_mode((840, 650))
pygame.display.set_caption("Jogo em Python")

freio = 170
janela_aberta = True

while janela_aberta:
    pygame.time.delay(freio)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    # comandos e freio
    if freio > 25:
        freio -= 1
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP] and freio > 8:
         freio -= 1
    if comandos[pygame.K_DOWN] and freio < 140:
         freio += 5
         virar.play()
    if comandos[pygame.K_RIGHT] and x < 560:
        x += vel
    if comandos[pygame.K_LEFT] and x > 180:
        x -= vel

    # substitui os carros e altera valores randômicos de velocidade, qual carro e em qual pista vai aparecer
    if pos_y_pista1 > 750:
        xp += 1
        indice_pista1 = randint(0, 3)
        fator_vel_pista1 = -(randint(5, 15))
        pos_y_pista1 = -(randint(800, 2000))
        pista1 = carros[indice_pista1]
    if pos_y_pista2 > 750:
        xp += 1
        indice_pista2 = randint(0, 3)
        fator_vel_pista2 = -(randint(5, 17))
        pos_y_pista2 = -(randint(800, 2000))
        pista2 = carros[indice_pista2]
    if pos_y_pista3 > 750:
        xp += 1
        indice_pista3 = randint(0, 3)
        fator_vel_pista3 = -(randint(5, 17))
        pos_y_pista3 = -(randint(800, 2000))
        pista3 = carros[indice_pista3]  # Achei o bug sem querer!
    if pos_y_pista4 > 750:
        xp += 1
        indice_pista4 = randint(0, 3)
        fator_vel_pista4 = -(randint(5, 17))
        pos_y_pista4 = -(randint(800, 2000))
        pista4 = carros[indice_pista4]

    # atualiza pontos
    texto_xp = font.render("XP: " + str(xp), True, (255, 255, 255, 5), (155, 100, 50))

    # lógica de velocidade
    pos_y_pista1 += vel_outros + fator_vel_pista1
    pos_y_pista2 += vel_outros + fator_vel_pista2
    pos_y_pista3 += vel_outros + fator_vel_pista3
    pos_y_pista4 += vel_outros + fator_vel_pista4

    # laços para construção dos elementos vetoriais de movimento vertical
    fator_mult = -1100
    janela.blit(fundo, (0, 0))
    for c in range(0, 30):
        mureta = pygame.draw.polygon(janela, (150, 150, 150),
                                     [(112, 39 + fator_mult + timer), (118, 27 + fator_mult + timer),
                                      (131, 27 + fator_mult + timer), (137, 39 + fator_mult + timer),
                                      (131, 34 + fator_mult + timer), (118, 34 + fator_mult + timer)])

        pygame.draw.rect(janela, (255, 215, 0), (167, fator_mult + timer, 8, 52))  # retangulo maior
        pygame.draw.rect(janela, (255, 215, 0), (167, 66 + fator_mult + timer, 8, 34))  # retangulo menor
        pygame.draw.rect(janela, (220, 220, 220), (286, fator_mult + timer, 7, 52))  # retangulo cinza

        pygame.draw.rect(janela, (255, 215, 0), (415, fator_mult + timer, 8, 52))  # retangulo maior
        pygame.draw.rect(janela, (255, 215, 0), (415, 66 + fator_mult + timer, 8, 34))  # retangulo menor
        pygame.draw.rect(janela, (220, 220, 220), (548, fator_mult + timer, 7, 52))  # retangulo cinza

        pygame.draw.rect(janela, (255, 215, 0), (668, fator_mult + timer, 8, 52))  # retangulo maior
        pygame.draw.rect(janela, (255, 215, 0), (668, 66 + fator_mult + timer, 8, 34))  # retangulo menor
        fator_mult += 114
        c += 1

    timer += 20
    if timer > 1150:
        timer = 0

    # chama os objetos na janela
    janela.blit(carro, (x, y))
    janela.blit(pista1, (pos_x - 220, pos_y_pista1))  # pista 1
    janela.blit(pista2, (pos_x - 100, pos_y_pista2))  # pista 2
    janela.blit(pista3, (pos_x + 40, pos_y_pista3))
    janela.blit(pista4, (pos_x + 154, pos_y_pista4))  # pista 4
    janela.blit(texto_xp, pos_texto)

    # colisões
    # colisão da quarta pista
    if (pos_y_pista4 > flag) and flag != 0:
        flag = 0
    if (x - 90 > pos_x) and ((y + 120 > pos_y_pista4) and (y - 120 < pos_y_pista4)):
        xp -= 1
        freio += 3
        print('Batida na 4ª pista!')
        if (flag != pos_y_pista4) and (flag == 0):
            if (pos_y_pista4 + 250 != flag) and (flag == 0):
                flag = pos_y_pista4 + 250
                indice_batida = randint(0, 4)
                batida[indice_batida].play(0)

    # colisão da primeira pista
    if (pos_y_pista1 > flag_1) and flag_1 != 0:
        flag_1 = 0
    if (x + 140 < pos_x) and ((y + 120 > pos_y_pista1) and (y - 120 < pos_y_pista1)):
        xp -= 1
        freio += 3
        print('Batida na 1ª pista!')
        if (flag_1 != pos_y_pista1) and (flag_1 == 0):
            if (pos_y_pista1 + 250 != flag_1) and (flag_1 == 0):
                flag_1 = pos_y_pista1 + 250
                indice_batida = randint(0, 4)
                batida[indice_batida].play(0)

    # colisão da segunda pista
    if (pos_y_pista2 > flag_2) and flag_2 != 0:
        flag_2 = 0
    if (x + 170 > pos_x) and (x + 10 < pos_x) and ((y + 120 > pos_y_pista2) and (y - 120 < pos_y_pista2)):
        xp -= 1
        freio += 3
        print('Batida na 2ª pista!')
        if (flag_2 != pos_y_pista2) and (flag_2 == 0):
            if (pos_y_pista2 + 250 != flag_2) and (flag_2 == 0):
                flag_2 = pos_y_pista2 + 250
                indice_batida = randint(0, 4)
                batida[indice_batida].play(0)

    # colisão da terceira pista
    if (pos_y_pista3 > flag_3) and flag_3 != 0:
        flag_3 = 0
    if (x - 120 < pos_x) and (x + 40 > pos_x) and ((y + 120 > pos_y_pista3) and (y - 120 < pos_y_pista3)):
        xp -= 1
        freio += 3
        print('Batida na 3ª pista!')
        if (flag_3 != pos_y_pista3) and (flag_3 == 0):
            if (pos_y_pista3 + 250 != flag_3) and (flag_3 == 0):
                flag_3 = pos_y_pista3 + 250
                indice_batida = randint(0, 4)
                batida[indice_batida].play(0)

    # if xp < 0:
    #     break

    pygame.display.update()

pygame.quit()
