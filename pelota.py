import sys, pygame

# Inicializamos
pygame.init()

# Resolución de 800x600
width = 1066
height = 600
size = width, height
screen = pygame.display.set_mode(size)

# Título de la ventana
pygame.display.set_caption("Juego ejemplo con Pygame por Borja")

# Empezamos el juego

# Necesitamos ciertas cosas

speed = [1,1] # Velocidad en modo lista (x,y)
speed2 = [-1,-1]
white = 255, 255, 255 # Color blanco del fondo

collision = pygame.mixer.Sound('coin.wav')
collision2 = pygame.mixer.Sound('clap.wav')
pygame.mixer.music.load("ost.wav")
pygame.mixer.music.play(-1)

pygame.font.init()
font = pygame.font.Font(None, 32)

textX = 0
textY = 0

ball = pygame.image.load("ball.png") # Cargamos nuestra imagen
ballrect = ball.get_rect()
ball2 = pygame.image.load("ball2.png")
ballrect2 = ball2.get_rect()

points = 0

bar = pygame.image.load("bar.png") # Cargamos la barra
barrect = bar.get_rect()
barrect.move_ip(533, 260) # Movemos la barra a la mitad

background = pygame.image.load("fondo.jpg").convert()

run=True
while run:
	#Texto de puntuacion
	score = font.render("Score :" + str(points), 0, (white))

	# Esperamos a que se mueva un poco la bola (ms)
	pygame.time.delay(2)
	# Captura de eventos
	for event in pygame.event.get():
		# Si el jugador quiere salir, salimos
		if event.type == pygame.QUIT: run = False

	# Veamos la barra
	keys = pygame.key.get_pressed()
	if keys[pygame.K_UP]:
		if barrect.top > 0:
			barrect=barrect.move(0,-1)
	if keys[pygame.K_DOWN]:
		if barrect.bottom < height:
			barrect=barrect.move(0,1)



	# Colisión de la pelota con la barra
	if barrect.colliderect(ballrect):
		if barrect.top < 100 or barrect.bottom > 500:
			speed[0] = -speed[0]+1
			points -= 1
			pygame.mixer.Sound.play(collision2)
		else:
			speed[0] = -speed[0]-1
			pygame.mixer.Sound.play(collision)
			points += 1





	# Movemos la pelota
	ballrect = ballrect.move(speed)
	# Movemos la segundapelota
	ballrect2 = ballrect2.move(speed2)
	
	# Nos aseguramos que la pelota no se sale de la ventana
	if ballrect.left < 0 or ballrect.right > width:
		speed[0] = -speed[0] # Simulamos el rebote
	if ballrect.top < 0 or ballrect.bottom > height:
		speed[1] = -speed[1] # Simulamos el rebote

	# Nos aseguramos que la segunda pelota no se sale de la ventana
	if ballrect2.left < 0 or ballrect2.right > width:
		speed2[0] = -speed2[0]  # Simulamos el rebote
	if ballrect2.top < 0 or ballrect2.bottom > height:
		speed2[1] = -speed2[1]  # Simulamos el rebote

		# Colisión de la segunda pelota con la barra
		if barrect.colliderect(ballrect2):
			if barrect.top < 100 or barrect.bottom > 500:
				speed2[0] = -speed2[0] + 1
				points -= 1
				pygame.mixer.Sound.play(collision2)
			else:
				speed2[0] = -speed2[0] - 1
				pygame.mixer.Sound.play(collision)
				points += 1

	# Comprobamos la puntuación para saca la segunda pelota
	if points > 5:
		screen.blit(ball2, ballrect2)

	# Ahora el fondo
	screen.blit(background, [0,0])
	screen.blit(ball, ballrect)
	screen.blit(bar, barrect)
	screen.blit(score, (0, 0))
	pygame.display.flip()


	
#Salimos
pygame.quit()

