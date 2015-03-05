import pygame
from pygame.locals import *

#class Screen():
#	def __init__(self, width, height):
#		pygame.init()
#		self.screen = pygame.display.set_mode((width, height))


#class RunProgram():

#	def __init__(self):
#		self.view = Screen(640, 480)

#	def run(self):

#		while True:
#			self.view()



#if __name__ == '__main__':
#    game = RunProgram()
#    game.run()




def main():
	
	"""Tells PyGame there will be a window"""
	pygame.init()

	"""Makes the window using the input size (height, width)"""
	screen = pygame.display.set_mode((640, 480))

	"""This initializes a new Surface in the screen, 
	it is the same size as the screen using get_size
	convert() gives the new surface the properties of the display"""
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((0, 0, 0))





	"""This renders the background onto the screen at location(0,0)
	flip updates the display"""
	screen.blit(background, (0, 0))
	pygame.display.flip()

	"""The while loop keeps the screen open until event.get 
	detects that you press the QUIT button
	the elif clause renders text when you press down the mouse button
	It also keeps rendering and updating the screen with blit and flip
	"""



	while 1:
		for event in pygame.event.get():
			if event.type == QUIT:
				return
			

			elif event.type == pygame.MOUSEBUTTONDOWN:
				print "True"
				#font = pygame.font.Font(None, 36)
				#text = font.render("Working :)", 0, (255, 255, 255))
				#textposition = pygame.mouse.get_pos() 
				pygame.rectangle
				background.blit(text, textposition)
				
			elif event.type == pygame.MOUSEBUTTONUP:
				print "False"
				font = pygame.font.Font(None, 36)
				text = font.render("Working :)", 0, (0, 0, 0))
				background.blit(text, textposition)





			
		
		screen.blit(background, (0,0))
		pygame.display.flip()





if __name__ == '__main__': main()
	
