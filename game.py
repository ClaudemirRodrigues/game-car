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

pygame.mixer.init()
batida = pygame.mixer.Sound('explosion.wav')
fundo = pygame.image.load('background.png')
carro = pygame.image.load('car.png')
pista1 = pygame.image.load('taxi.png')
pista2 = pygame.image.load('police.png')
pista3 = pygame.image.load('green_car.png')
pista4 = pygame.image.load('ferrari.png')
carros = [pista1, pista2, pista3, pista4]

font = pygame.font.SysFont('arial black', 20)
texto = font.render("PONTOS: ", True, (255, 255, 255), (155, 100, 50))
pos_texto = texto.get_rect()
pos_texto.center = (65, 50)
pontos = -4

janela = pygame.display.set_mode((840, 650))
pygame.display.set_caption("Jogo em Python")

freio = 140
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
    if comandos[pygame.K_UP] and freio > 10:
         freio -= 1
    if comandos[pygame.K_DOWN] and freio < 140:
         freio += 5
    if comandos[pygame.K_RIGHT] and x < 560:
        x += vel
    if comandos[pygame.K_LEFT] and x > 180:
        x -= vel

    # substitui os carros e altera valores randômicos
    if pos_y_pista1 > 750:
        pontos += 1
        indice_pista1 = randint(0, 3)
        fator_vel_pista1 = -(randint(5, 15))
        pos_y_pista1 = -(randint(800, 2000))
        pista1 = carros[indice_pista1]
    if pos_y_pista2 > 750:
        pontos += 1
        indice_pista2 = randint(0, 3)
        fator_vel_pista2 = -(randint(5, 17))
        pos_y_pista2 = -(randint(800, 2000))
        pista2 = carros[indice_pista2]
    if pos_y_pista3 > 750:
        pontos += 1
        indice_pista3 = randint(0, 3)
        fator_vel_pista3 = -(randint(5, 17))
        pos_y_pista3 = -(randint(800, 2000))
        pista2 = carros[indice_pista3]
    if pos_y_pista4 > 750:
        pontos += 1
        indice_pista4 = randint(0, 3)
        fator_vel_pista4 = -(randint(5, 17))
        pos_y_pista4 = -(randint(800, 2000))
        pista4 = carros[indice_pista4]

    # atualiza pontos
    texto = font.render("PONTOS: " + str(pontos), True, (255, 255, 255, 5), (155, 100, 50))

    # lógica de velocidade
    pos_y_pista1 += vel_outros + fator_vel_pista1
    pos_y_pista2 += vel_outros + fator_vel_pista2
    pos_y_pista3 += vel_outros + fator_vel_pista3
    pos_y_pista4 += vel_outros + fator_vel_pista4

    # construção dos elementos de movimento vertival
    janela.blit(fundo, (0, 0))
    pygame.draw.polygon(janela, "red", [(112, 39 + timer), (118, 27 + timer), (131, 27 + timer), (137, 39 + timer),
                                        (131, 34 + timer), (118, 34 + timer)])
    pygame.draw.rect(janela, "yellow", (167, 0 + timer, 8, 52))
    pygame.draw.rect(janela, "yellow", (167, 66 + timer, 8, 34))
    pygame.draw.rect(janela, (220, 220, 220), (286, 0 + timer, 7, 52))
    timer += 10
    if timer == 650:
        timer = 0

    # chama os objetos na janela
    janela.blit(carro, (x, y))
    janela.blit(pista1, (pos_x - 220, pos_y_pista1))  # pista 1
    janela.blit(pista2, (pos_x - 100, pos_y_pista2))  # pista 2
    janela.blit(pista3, (pos_x + 40, pos_y_pista3))
    janela.blit(pista4, (pos_x + 154, pos_y_pista4))  # pista 4
    janela.blit(texto, pos_texto)

    # colisões
    # colisão da quarta pista
    if (pos_y_pista4 > flag) and flag != 0:
        flag = 0
    if (x - 90 >= pos_x) and ((y + 120 > pos_y_pista4) and (y - 120 < pos_y_pista4)):
        pontos -= 1
        print('Batida na 4ª pista!')
        if (flag != pos_y_pista4) and (flag == 0):
            if (pos_y_pista4 + 250 != flag) and (flag == 0):
                flag = pos_y_pista4 + 250
                batida.play(0)

    # colisão da primeira pista
    if (pos_y_pista1 > flag_1) and flag_1 != 0:
        flag_1 = 0
    if (x + 140 < pos_x) and ((y + 120 > pos_y_pista1) and (y - 120 < pos_y_pista1)):
        pontos -= 1
        print('Batida na 1ª pista!')
        if (flag_1 != pos_y_pista1) and (flag_1 == 0):
            if (pos_y_pista1 + 250 != flag_1) and (flag_1 == 0):
                flag_1 = pos_y_pista1 + 250
                batida.play(0)
                
    # colisão da segunda pista
    if (pos_y_pista2 > flag_2) and flag_2 != 0:
        flag_2 = 0
    if (x + 170 > pos_x) and (x + 10 < pos_x) and ((y + 120 > pos_y_pista2) and (y - 120 < pos_y_pista2)):
        pontos -= 1
        print('Batida na 2ª pista!')
        if (flag_2 != pos_y_pista2) and (flag_2 == 0):
            if (pos_y_pista2 + 250 != flag_2) and (flag_2 == 0):
                flag_2 = pos_y_pista2 + 250
                batida.play(0)

    # colisão da terceira pista
    if (pos_y_pista3 > flag_3) and flag_3 != 0:
        flag_3 = 0
    if (x - 120 < pos_x) and (x + 40 > pos_x) and ((y + 120 > pos_y_pista3) and (y - 120 < pos_y_pista3)):
        pontos -= 1
        print('Batida na 3ª pista!')
        if (flag_3 != pos_y_pista3) and (flag_3 == 0):
            if (pos_y_pista3 + 250 != flag_3) and (flag_3 == 0):
                flag_3 = pos_y_pista3 + 250
                batida.play(0)

    pygame.display.update()

pygame.quit()
