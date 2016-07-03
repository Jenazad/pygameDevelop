#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame, sys
from pygame.locals import *

RESOLUCION= (200, 600)

class MiJuego():
	def __init__(self):
		self.ventana= None
		self.fondo= None
		self.reloj = None
		self.estado= None
		self.personaje= None
		self.objetos= None

		self.preset()
		self.load()
		self.run()

	def preset(self):
		pygame.init()
		pygame.display.set_mode( RESOLUCION , 0, 0)

	def load(self):
		self.ventana = pygame.display.get_surface()

		superficie = pygame.Surface( RESOLUCION, flags=HWSURFACE )
		superficie.fill((128,128,128,255))
		self.fondo= superficie

		self.reloj = pygame.time.Clock()
		self.estado= True
		self.personaje= Personaje()
		self.objetos= pygame.sprite.OrderedUpdates()
		self.objetos.add(self.personaje)

	def run(self):
		self.ventana.blit(self.fondo, (0,0))
		pygame.display.update()
		while self.estado:
			self.reloj.tick(35)
			self.objetos.clear(self.ventana, self.fondo)
			self.objetos.update()
			self.objetos.draw(self.ventana)
			pygame.display.update()

class Personaje(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image= pygame.Surface((20, 20))
		self.rect= self.image.get_rect()
		self.rect.x= RESOLUCION[0]/2-self.rect.w/2
		self.rect.y= 0
	
	def update(self):
		self.rect.y += 1
		if self.rect.y > RESOLUCION[1]:
			pygame.quit()
			sys.exit()

if __name__=="__main__":
	MiJuego()
