from pygame import*
import sys

init()


#fundo do dia para noite

raio_x = 140
timer = 0
running = True
clock = time.Clock()


invincible_png = image.load('invincible.png')

invincible_png = transform.scale(invincible_png, (200, 200))

invincible_font = font.Font("invinciblefont.TTF", 50)

texto = invincible_font.render("casa do invencível", True, (0, 0, 0))

mixer.music.load("dav4d.mp3")

mixer.music.play(-1)

window = display.set_mode((1280, 720))

among = mixer.Sound("amongus.mp3")
baby1 = mixer.Sound("baby1.mp3")
error = mixer.Sound("error.mp3")
triste = mixer.Sound("triste.mp3")


# Variáveis da nuvem (EXTRA)

nuvem_x = 800

nuvem_y = 100

velocidade_nuvem = 3

#loop principal 

relogio = time.Clock()

# window.fill removido daqui para rodar dentro do while


#programa para fazer o programa fechar com o X do windows

modo_fundo = False

uuu=255
iii=188
ooo=99
background_color = (uuu, iii, ooo)


aaa = (uuu-(600//5.75))
bbb = (iii+(600//25))
ccc = (ooo+(600//3.95))


while running:
    dt = clock.tick(60) / 1000 # dt precisa estar dentro do loop
    
    for ev in event.get():
        if ev.type == QUIT:
            running = False
            sys.exit()
        
        if ev.type == KEYDOWN:
            if ev.key == K_SPACE:
                modo_fundo = not modo_fundo

        # Lógica dos sons (botão do meio)
        if ev.type == MOUSEBUTTONDOWN:
            if ev.button == 2:
                if modo_fundo == True:
                    triste.play()
                else:
                    if raio_x > 0 and raio_x < 430:
                        baby1.play()
                    elif raio_x >= 430 and raio_x < 860:
                        among.play()
                    elif raio_x >= 860:
                        error.play()

    # Lógica das cores (movida para dentro do loop para atualizar sempre)
    if modo_fundo:
        background_color = (245, 178, 64)
    else:
        if raio_x < 600:
            # max e min garantem que a cor não quebre o pygame (0 a 255)
            r = max(0, min(255, uuu - (raio_x // 5.75)))
            g = max(0, min(255, iii + (raio_x // 25)))
            b = max(0, min(255, ooo + (raio_x // 3.95)))
            background_color = (r, g, b)
        else:
            r = max(0, min(255, aaa - ((raio_x - 600) // 5)))
            g = max(0, min(255, bbb - ((raio_x - 600) // 4.3)))
            b = max(0, min(255, ccc - ((raio_x - 600) // 4.5)))
            background_color = (r, g, b)


    # Teclas e Movimento
    keys = key.get_pressed()
    mouse_keys = mouse.get_pressed()

    if raio_x < 1350:
        if keys[K_d] or mouse_keys[0]: # D ou Clique Esquerdo
            raio_x = raio_x + 300 * dt
    if raio_x > 10:
        if keys[K_a] or mouse_keys[2]: # A ou Clique Direito
            raio_x = raio_x - 300 * dt

    # Movimento da nuvem
    nuvem_x += velocidade_nuvem
    if nuvem_x > 1300: 
        nuvem_x = -150 

    # --- DESENHOS ---

    # Fundo (usando a cor dinâmica)
    window.fill(background_color)

    # Grama 
    draw.rect(window, (100, 150, 50), (0, 550, 1280, 170))

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
    draw.rect(window, (245, 245, 220), (450, 350, 200, 200))
    draw.polygon(window, (60, 60, 60), [(450, 350), (550, 200), (650, 350)])
    draw.rect(window, (139, 69, 19), (560, 430, 60, 120)) 
    draw.circle(window, (0, 0, 0), (610, 490), 5) 
    draw.rect(window, (0, 0, 128), (480, 430, 60, 60)) 

    # Árvore
    draw.rect(window, (101, 67, 33), (830, 450, 40, 100)) 
    draw.circle(window, (34, 139, 34), (850, 400), 70) 

    # Nuvem Animada
    draw.circle(window, (255, 255, 255), (int(nuvem_x), nuvem_y), 30)
    draw.circle(window, (255, 255, 255), (int(nuvem_x) + 30, nuvem_y - 15), 40)
    draw.circle(window, (255, 255, 255), (int(nuvem_x) + 70, nuvem_y), 35)
    draw.circle(window, (255, 255, 255), (int(nuvem_x) + 40, nuvem_y + 15), 30)

    # invincible
    window.blit(invincible_png, (50, 310)) 

    # texto
    window.blit(texto, (400, 50))

    display.update()

