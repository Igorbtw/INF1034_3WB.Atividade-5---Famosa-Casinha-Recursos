from pygame import*
import sys

init()

invincible_png = image.load('invincible.png')

invincible_png = transform.scale(invincible_png, (200, 200))

invincible_font = font.Font("invinciblefont.TTF, 50")

texto = invincible_font.render("casa do invencível", True, (0, 0, 0))

mixer.music.load()

window = display.set_mode((1280, 720))

# Variáveis da nuvem (EXTRA)

nuvem_x = 800

nuvem_y = 100

velocidade_nuvem = 3

#loop principal 

relogio = time.Clock()

window.fill((60, 182, 254))

while True:
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()

    # Movimento da nuvem

    nuvem_x += velocidade_nuvem

    if nuvem_x > 1300: 

        nuvem_x = -150 

# Grama 

    draw.rect(window, (100, 150, 50), (0, 550, 1200, 170))



    # Sol

    draw.circle(window, (255, 255, 0), (150, 150), 50)

    draw.line(window, (255, 255, 0), (150, 80), (150, 50), 5)

    draw.line(window, (255, 255, 0), (150, 220), (150, 250), 5)

    draw.line(window, (255, 255, 0), (80, 150), (50, 150), 5)

    draw.line(window, (255, 255, 0), (220, 150), (250, 150), 5)

    draw.line(window, (255, 255, 0), (100, 100), (75, 75), 5)

    draw.line(window, (255, 255, 0), (200, 200), (225, 225), 5)

    draw.line(window, (255, 255, 0), (100, 200), (75, 225), 5)

    draw.line(window, (255, 255, 0), (200, 100), (225, 75), 5)



    # Casa 

    draw.rect(window, (105, 105, 105), (450, 350, 200, 200))

    draw.polygon(window, (210, 105, 30), [(450, 350), (550, 200), (650, 350)]) 

    draw.rect(window, (139, 69, 19), (560, 430, 60, 120)) 

    draw.circle(window, (0, 0, 0), (610, 490), 5) 

    draw.rect(window, (0, 0, 128), (480, 430, 60, 60)) 


    # Árvore

    draw.rect(window, (101, 67, 33), (830, 450, 40, 100)) 

    draw.circle(window, (34, 139, 34), (850, 400), 70) 



    # Nuvem Animada

    draw.circle(window, (255, 255, 255), (nuvem_x, nuvem_y), 30)

    draw.circle(window, (255, 255, 255), (nuvem_x + 30, nuvem_y - 15), 40)

    draw.circle(window, (255, 255, 255), (nuvem_x + 70, nuvem_y), 35)

    draw.circle(window, (255, 255, 255), (nuvem_x + 40, nuvem_y + 15), 30)



  

    # invincible

    window.blit(invincible_png, (50, 310)) 
   

    # texto

    window.blit(texto, (400, 50))



    display.update()

    relogio.tick(60) 
