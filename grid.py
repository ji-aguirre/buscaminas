
import pygame
import pygame.freetype
import comandos as com
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

partida = com.Juego(10,10,15)

cant_tiles_x = partida.tablero.largo
cant_tiles_y = partida.tablero.alto

TILE_SIZE = 20
MARGIN = 3
WINDOW_SIZE = [(TILE_SIZE+2*MARGIN)*cant_tiles_x,(TILE_SIZE+2*MARGIN)*cant_tiles_y]

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = (WINDOW_SIZE[0] / cant_tiles_x) - MARGIN
HEIGHT = (WINDOW_SIZE[1] / cant_tiles_y)-MARGIN
 
# This sets the margin between each cell

 
# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = partida.tablero
#partida.tablero.mostrar_tablero()

 

# Initialize pygame
pygame.init()

fuente = pygame.freetype.SysFont("Arial",12)
 
# Set the HEIGHT and WIDTH of the screen
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Array Backed Grid")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
	for event in pygame.event.get():  # User did something
		if event.type == pygame.QUIT:  # If user clicked close
			done = True  # Flag that we are done so we exit this loop
		elif event.type == pygame.MOUSEBUTTONDOWN:
			# User clicks the mouse. Get the position
			pos = pygame.mouse.get_pos()
			# Change the x/y screen coordinates to grid coordinates
			column = pos[0] // (WIDTH + MARGIN)
			row = pos[1] // (HEIGHT + MARGIN)
			# Set that location to one
			if partida.jugada(int(row),int(column)):
				print("Partida Terminada")

			#print("Click ", pos, "Grid coordinates: ", row, column)
 
	# Set the screen background
	screen.fill(BLACK)
 
	# Draw the grid
	for row in range(cant_tiles_x):
		for column in range(cant_tiles_y):
			color = WHITE
			if grid[(row,column)] != -1:
			    color = WHITE
			pygame.draw.rect(screen,color,[(MARGIN + WIDTH) * column + MARGIN,(MARGIN + HEIGHT) * row + MARGIN,WIDTH,HEIGHT])
			fuente.render_to(screen, [(MARGIN + WIDTH) * column + MARGIN + (WIDTH/2 -MARGIN),(MARGIN + HEIGHT) * row + MARGIN+(HEIGHT/2 -MARGIN),WIDTH,HEIGHT],str(grid[(row,column)]),(255,0,0))
 
	# Limit to 60 frames per second
	clock.tick(60)
 
	# Go ahead and update the screen with what we've drawn.
	pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()