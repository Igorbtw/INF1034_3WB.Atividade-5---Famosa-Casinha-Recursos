from pygame import*
import sys

init()

invincible_png = image.load('invincible.png')
invincible_png = transform.scale(invincible_png, (200, 200))

invincible_font = font.Font("invinciblefont.TTF, 50")

mixer.music.load()

window = display.set_mode((1280, 720))

window.fill((60, 182, 254))

while True:
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()

    #Desenhar um quadrado
    draw.rect(window, (255, 0, 0), (200, 300, 100, 50), 0)
    draw.circle(window, (255, 255, 0), (500, 600), 200)
    draw.polygon(window, (0, 255, 0), ((200, 300), (250, 150), (300, 300)))
    draw.line(window, (255, 0, 255), (100, 100), (200, 200), 3)

     #Desenhar imagens
    window.blit(invincible_png, (0, 0))

     #desenhar texto
    invincible_text = invincible_font.render('he has to be invincible')
     
    display.update()


