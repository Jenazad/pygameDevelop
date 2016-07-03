import pygame
import random
import sys
import os

path = os.getcwd() + '/'

class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    def update(self):
        self.left,self.top = pygame.mouse.get_pos()

class Boton(pygame.sprite.Sprite):
    def __init__(self,imagen1,imagen2,x,y):
        self.imagen_normal = imagen1
        self.imagen_seleccion = imagen2
        self.imagen_actual = self.imagen_normal
        self.rect = self.imagen_actual.get_rect()
        self.rect.left,self.rect.top=(x,y)
    def update(self,pantalla,cursor):
        if cursor.colliderect(self.rect):
            self.imagen_actual = self.imagen_seleccion
        else: self.imagen_actual = self.imagen_normal
        pantalla.blit(self.imagen_actual,self.rect)

class Player(pygame.sprite.Sprite):

    def __init__(self,imagen):
        self.imagen=imagen
        self.rect = self.imagen.get_rect()
        self.rect.top,self.rect.left=(550,450)

    def mover(self,vx,vy):
        self.rect.move_ip(vx,vy)

    def update(self,superficie):
        superficie.blit(self.imagen,self.rect)

class Playerrandom(pygame.sprite.Sprite):

    def __init__(self,imagen,x,y):
        self.imagen=imagen
        self.rect = self.imagen.get_rect()
        self.rect.top,self.rect.left=(x,y)

    def mover(self,vx,vy):
        self.rect.move_ip(vx,vy)

    def update(self,superficie):
        superficie.blit(self.imagen,self.rect)

class Disparo(pygame.sprite.Sprite):
    def __init__(self,imagen):
        self.imagen = imagen
        self.rect = self.imagen.get_rect()
        self.rect.top,self.rect.left=(950,900)
    def mover(self,x):
        self.rect.move_ip(0,x)

    def update(self,superficie):
        superficie.blit(self.imagen,self.rect)
"""
class Sprites(pygame.sprite.Sprite):
    def __init__(self,imagen,numero):
        self.lista=[]
        for a in range(numero):
            self.imagen=imagen
            self.rect=self.imagen.get_rect()
            self.rect.top=random.randrange(-10,0)
            self.rect.left=random.randrange(5,1000)
            self.lista.append(self.rect)

    def mover (self):
        for imagenes in self.lista:
            imagenes.move_ip(0,2)

    def reagregar(self):
        pass

    def agregarotro(self):
        pass

    def update (self,superficie):
        for imagenes in self.lista:
            superficie.blit(self.imagen,self.rect)
"""
class Recs(pygame.sprite.Sprite):

    def __init__ (self,numeroinicial):
        self.lista=[]
        pygame.sprite.Sprite.__init__(self)
        for x in range(numeroinicial):
            #creo un rec random
            leftrandom = random.randrange(2,880)
            toprandom = random.randrange(-580,-10)
            widthrandom = random.randrange(10,30)
            heightrandom = random.randrange(15,30)
            self.lista.append(pygame.Rect(leftrandom,toprandom,widthrandom,heightrandom))

    def reagregar(self):
        for x in range (len(self.lista)):
            if self.lista[x].top>650:
                leftrandom = random.randrange(2,880)
                toprandom = random.randrange(-580,-10)
                widthrandom = random.randrange(10,30)
                heightrandom = random.randrange(15,30)
                self.lista[x]=(pygame.Rect(leftrandom,toprandom,widthrandom,heightrandom))

    def mover(self,numero):
        for rectangulo in self.lista:
            rectangulo.move_ip(0,numero)

    def pintar(self,superficie):
        for rectangulo in self.lista:
            pygame.draw.rect(superficie,(255,255,255),rectangulo)
#            self.image= pygame.transform.scale(imagen, (20,20))
#   (103,100,58)

def buscar(player,playerrandom,numero):
    if(player.rect.left<playerrandom.rect.left):
        playerrandom.mover(-numero,0)
    else:
        playerrandom.mover(numero,0)
    if(player.rect.top<playerrandom.rect.top):
        playerrandom.mover(0,-numero)
    else:
        playerrandom.mover(0,numero)

def disparar(disparo):
    disparo.mover(-5)

def colision(player,recs):
    for rec in recs.lista:
        if player.rect.colliderect(rec):
            return True
    return False

def colision1(player,playerrandom):
    if player.rect.colliderect(playerrandom.rect):
        return True
    return False

def colision2(disparo,recs):
    for rec in recs.lista:
        if disparo.rect.colliderect(rec):
            rec.width =0
            rec.height=0
            (rec.left,rec.top) = (920,900)
            return True
    return False

def colision3(disparo,playerrandom):
    if disparo.rect.colliderect(playerrandom.rect):
        return True
    return False

def juego(recs1,numero,time,vx1):    

    pygame.init()
    pygame.joystick.init()

    pantalla = pygame.display.set_mode((901,678))
    pygame.display.set_caption("AsteoroiMeow")
    cursor1 = Cursor()
    salir = True
    imagen1 = pygame.image.load(path+"navecita.png")#.conver_alpha
    imagen2 = pygame.image.load(path+"navecita1.png")#.conver_alpha
    imagenfondo = pygame.image.load(path+"fondo.jpg")
    imagenexplosion = pygame.image.load(path+"explosion.png")
    pygame.mixer.music.load(path+"Topgear.mp3")
    rojo1 = pygame.image.load(path+"menu2.jpg")
    rojo2 = pygame.image.load(path+"menu3.jpg")
    imagen3 = pygame.image.load(path+"nuclear.png")
    azul1 = pygame.image.load(path+"exit.png")
    azul2 = pygame.image.load(path+"exit1.png")
    sonido1 = pygame.mixer.Sound(path+"Mariojump.wav")
    sonido2 = pygame.mixer.Sound(path+"explosion.wav")
    sonido3 = pygame.mixer.Sound(path+"Game_Over.wav")
    sonido4 = pygame.mixer.Sound(path+"disparo.wav")
    fuente2 = pygame.font.SysFont("Arial",15,True,False)
    fuente1 = pygame.font.SysFont("Arial",60,True,True)
    info3 = fuente1.render("GAME OVER",0,(240,240,0))
    info4 = fuente1.render("PAUSE",0,(240,240,0))
    r1 = pygame.Rect(900,0,100,678) # X Y , x y dimensiones ya ta
    r2 = pygame.Rect(-50,0,51,678) # ya ta
    r3 = pygame.Rect(0,677,901,150) # ya ta
    r4 = pygame.Rect(0,-50,901,51) # ya ta
    reloj1 = pygame.time.Clock()
    boton1 = Boton(rojo1,rojo2,250,450) #x,y
    boton2 = Boton(azul1,azul2,550,450)
    vidasint = 3
    S=2
    dispara = False
    a = 0
    salir1 = True
    tiempo = 0
    pau = 0
    invu = 0
    disparo1 = Disparo(imagen2)
    player2 = Playerrandom(imagen2,5,5)
    player1 = Player(imagen1)
    player3 = Player(imagen1)
    vx,vy=0,0
    velocidad = 5
    negro = (200,50,130)
    leftsigueapretada,rightsigueapretada,upsigueapretada,downsigueapretada = False,False,False,False
    colisiono = False
    segundosint = 0
    nivelint = 1
    inicio = False
    termino = False
    pygame.mixer.music.play(0)
    while salir != False :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = False
            if colisiono == False:
                if (event.type == pygame.KEYDOWN):
                    if event.key == pygame.K_SPACE:
                        pygame.mixer.music.pause()
                        pantalla.blit(info4,(250,250))
                        pygame.display.update()
                        inicio = True
                        pygame.event.wait() # pausea

                if (event.type == pygame.KEYDOWN):
                    if event.key == pygame.K_SPACE:
                        pygame.mixer.music.pause()
                        pygame.event.wait()

                    if event.key == pygame.K_LEFT:
                        #leftsigueapretada = True
                        vx-=velocidad
                        sonido1.play()
                    if event.key == pygame.K_RIGHT:
                        #rightsigueapretada = True
                        vx+=velocidad
                        sonido1.play()
                    if event.key == pygame.K_UP:
                        #upsigueapretada = True
                        vy-=velocidad
                        sonido1.play()
                    if event.key == pygame.K_DOWN:
                        #downsigueapretada = True
                        vy+=velocidad
                        sonido1.play()
                    if event.key == pygame.K_a:
                        sonido4.play()
                        dispara = True

                if (event.type == pygame.KEYUP):
                    if event.key == pygame.K_LEFT:
                        leftsigueapretada = False
                        if rightsigueapretada:vx += velocidad 
                        else : vx=0
                    if event.key == pygame.K_RIGHT:
                        rightsiguesapretada = False
                        if leftsigueapretada: vx -=velocidad
                        else : vx=0
                    if event.key == pygame.K_UP:
                        upsigueapretada = False
                        if downsigueapretada: vy +=velocidad
                        else : vy=0
                    if event.key == pygame.K_DOWN:
                        downsigueapretada=False
                        if upsigueapretada: vy +=velocidad
                        else : vy=0

        if inicio == True :
            pau = pau +1
#        else:
#            a = a - pau
#            pau = 0

        if dispara == True :
            (disparo1.rect.left,disparo1.rect.top)=(xant1,yant1)
            sonido1.stop()
            dispara = False
        disparar(disparo1)
        disparo1.update(pantalla)



        pygame.mixer.music.unpause()
        (xant1,yant1)=(player1.rect.left,player1.rect.top)
        (xant2,yant2)=(player2.rect.left,player2.rect.top)
        (xant3,yant3)= (950,900)
        (xant,yant)=(450,550)
        (xn,yn)=(5,5)

        if colisiono == False:
            recs1.mover(S)
            player1.mover(vx,vy)

        buscar(player1,player2,vx1)

        if colision1(player1,player2):
            pygame.mixer.music.pause()
            sonido1.stop()
            player1.imagen=imagenexplosion
            player1.update(pantalla)
            sonido2.play(0)
            vidasint=vidasint-1
            pygame.display.update()
            pygame.time.wait(500)
            if (vidasint == 0):
                sonido3.play(0)
                (player1.rect.left,player1.rect.top)=(950,900)
                colisiono = True
                termino = True
#                pygame.display.update()                

            if(vidasint >0):
                player1.update(pantalla)
                (player2.rect.left,player2.rect.top)=(xn,yn)
                (player1.rect.left,player1.rect.top)=(xant,yant)
                pygame.mixer.music.unpause()

            if vidasint < 0 :
                pygame.time.delay(2000)
                salir = False

        if colision(player2,recs1):
            (player2.rect.left,player2.rect.top)=(xant2,yant2)

        if colision2(disparo1,recs1):
            sonido1.stop()
            disparo1.imagen = imagen3
            disparo1.update(pantalla)
            sonido2.play(0)
            pygame.display.update()
            pygame.time.wait(100)
            (disparo1.rect.left,disparo1.rect.top)=(xant3,yant3)

        if colision3(disparo1,player2):
            sonido1.stop()
            disparo1.imagen = imagen3
            disparo1.update(pantalla)
            sonido2.play(0)
            pygame.display.update()
            pygame.time.wait(100)
            (player2.rect.left,player2.rect.top) = (5,5)
            (disparo1.rect.left,disparo1.rect.top)=(xant3,yant3)


        if colision(player1,recs1):
            pygame.mixer.music.pause()
            sonido1.stop()
            player1.imagen=imagenexplosion
            player1.update(pantalla)
            sonido2.play(0)
            vidasint=vidasint-1
            pygame.display.update()
            pygame.time.wait(500)
            if (vidasint == 0):
                sonido3.play(0)
                colisiono = True
                (player1.rect.left,player1.rect.top)=(950,900)
                termino = True
#                pygame.display.update()                

            if(vidasint >0):
                player1.update(pantalla)
                (player2.rect.left,player2.rect.top)=(xn,yn)
                (player1.rect.left,player1.rect.top)=(xant,yant)
                pygame.mixer.music.unpause()
#                if ((segundosint-time) % 15 == 0):
#                    tiempo = tiempo +1
#                for event in pygame.event.get():
#                    if event.type == pygame.MOUSEMOTTION:
#                        (cursor1.left,cursor1.top) = pygame.mouse.get_pos()
#                        (player1.rect.left,player1.rect.top)=(cursor1.left,cursor1.top)
#                if event.type == pygame.MOUSEBUTTONDOWN:
#                   if event.key == pygame.K_ESC:

            if vidasint < 0 :
                pygame.time.delay(2000)
                salir = False


        vidas = str(vidasint)
        nivel = str(nivelint)
        info = fuente2.render("Tienes "+vidas+" vidas",0,(240,56,0))
        info1 = fuente2.render("Nivel: "+nivel,0,(240,56,0))
        pygame.draw.rect(pantalla,negro,r1)
        pygame.draw.rect(pantalla,negro,r2)
        pygame.draw.rect(pantalla,negro,r3)
        pygame.draw.rect(pantalla,negro,r4)
        pantalla.blit(imagenfondo,(1,1))
        recs1.pintar(pantalla)
        disparo1.update(pantalla)
        player2.update(pantalla)
        player1.update(pantalla)

        if player1.rect.colliderect(r1):
            (player1.rect.left,player1.rect.top)=(xant1,yant1)

        if player1.rect.colliderect(r2):
            (player1.rect.left,player1.rect.top)=(xant1,yant1)

        if player1.rect.colliderect(r3):
            (player1.rect.left,player1.rect.top)=(xant1,yant1)

        if player1.rect.colliderect(r4):
            (player1.rect.left,player1.rect.top)=(xant1,yant1) 

        if player2.rect.colliderect(r1):
            (player2.rect.left,player2.rect.top)=(xant2,yant2)

        if player2.rect.colliderect(r2):
            (player2.rect.left,player2.rect.top)=(xant2,yant2)

        if player2.rect.colliderect(r3):
            (player2.rect.left,player2.rect.top)=(xant2,yant2)

        if player2.rect.colliderect(r4):
            (player2.rect.left,player2.rect.top)=(xant2,yant2)            

        if termino == False:
            segundosint = pygame.time.get_ticks()/1000
            a = segundosint - time
            segundos = str(a)
            contador = fuente2.render(segundos,0,(240,56,0))
        else:
            salir = False
#            pygame.display.update()
 
        if ((a) % 15 == 0):
            tiempo = tiempo +1

        if (tiempo >= 85 and tiempo <= 90 and termino == False):
            nivelint = nivelint + 1
            S = S + numero
            if nivelint>1 and nivelint%2 ==1:
                vidasint = vidasint + 1
            tiempo = 0

        disparo1.imagen = imagen2
        player1.imagen = imagen1
        player1.update(pantalla)
        player2.update(pantalla)
        pantalla.blit(contador,(490,5))
        pantalla.blit(info,(150,5))
        pantalla.blit(info1,(70,5))
        pygame.display.update()
        recs1.reagregar()
    while salir1 !=False:
        for event in pygame.event.get():
            if cursor1.colliderect(boton1.rect):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
                    salir = False
                    menu()
            if cursor1.colliderect(boton2.rect):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
                    salir = False
                    sys.exit()
            if event.type == pygame.QUIT:
                salir = False
                sys.exit()

        pantalla.blit(imagenfondo,(0,0))
        vidas = str(vidasint)
        nivel = str(nivelint)
        player3.imagen = imagen1
        player2.imagen = imagen2
        (player3.rect.left,player3.rect.top)=(0,0)
        (player2.rect.left,player2.rect.top)=(0,60)
        info = fuente2.render("Tienes "+vidas+" vidas",0,(240,56,0))
        info1 = fuente2.render("Nivel: "+nivel,0,(240,56,0))
        contador = fuente2.render("Usted soporto la lluvia de meteoros durante: "+segundos+" segundos",0,(240,56,0))
        pantalla.blit(info3,(250,250))
        player3.update(pantalla)
        player2.update(pantalla)
        pantalla.blit(info,(150,5))
        pantalla.blit(info1,(70,5))
        pantalla.blit(contador,(490,5))
        cursor1.update()
        boton1.update(pantalla,cursor1)
        boton2.update(pantalla,cursor1)
        pygame.display.update()
    pygame.quit()




def menu():
    pygame.init()
    pantalla = pygame.display.set_mode((900,720))
    pygame.display.set_caption("Dificultad de Juego")
    cursor1 = Cursor()
    fuente1 = pygame.font.SysFont("Arial",50,True,True)
    info = fuente1.render("~~Niveles~~",0,(140,210,130))
    info1 = fuente1.render("Easy",0,(180,180,130))
    info2 = fuente1.render("Maso Melas",0,(180,180,130))
    info3 = fuente1.render("Arrugo",0,(180,180,130))
    info5 = fuente1.render("Nika-gando",0,(180,180,130))
    info4 = fuente1.render("Volver al Menu",0,(180,180,130))
    easy1 = pygame.image.load(path+"facil.jpg")
    easy2 = pygame.image.load(path+"facil1.jpg")
    medium1 = pygame.image.load(path+"normal.jpg")
    medium2 = pygame.image.load(path+"normal1.jpg")
    hard1 = pygame.image.load(path+"dificil.jpg")
    hard2 = pygame.image.load(path+"dificil1.jpg")
    menu1 = pygame.image.load(path+"menu.jpg")
    menu2 = pygame.image.load(path+"menu1.jpg")
    impo1 = pygame.image.load(path+"impo.jpg")
    impo2 = pygame.image.load(path+"impo1.jpg")
    imagenfondo1 = pygame.image.load(path+"planetas1.jpg")
    pygame.mixer.music.load(path+"X-Zero.mp3")
    boton1 = Boton(easy1,easy2,100,150) #x,y
    boton2 = Boton(medium1,medium2,100,260)
    boton3 = Boton(hard1,hard2,100,370)
    boton4 = Boton(menu1,menu2,100,590)
    boton5 = Boton(impo1,impo2,100,480)
    salir = True
    pygame.mixer.music.play(0)
    while salir != False :
        for event in pygame.event.get():
            if cursor1.colliderect(boton1.rect):
# Facil
                if event.type == pygame.MOUSEBUTTONDOWN:
                        tiempo_inicio = pygame.time.get_ticks()/1000
                        pygame.quit()
                        recs1 = Recs(10)
                        salir = False
                        juego(recs1,2,tiempo_inicio,1)
# Medio
            if cursor1.colliderect(boton2.rect):
                if event.type == pygame.MOUSEBUTTONDOWN:
                        tiempo_inicio = pygame.time.get_ticks()/1000
                        pygame.quit()
                        recs1 = Recs(15)
                        salir = False
                        juego(recs1,2,tiempo_inicio,1)
# Normal
            if cursor1.colliderect(boton3.rect):
                if event.type == pygame.MOUSEBUTTONDOWN:
                        tiempo_inicio = pygame.time.get_ticks()/1000
                        pygame.quit()
                        recs1 = Recs(15)
                        salir = False
                        juego(recs1,3,tiempo_inicio,1)
# Imposible
            if cursor1.colliderect(boton5.rect):
                if event.type == pygame.MOUSEBUTTONDOWN:
                        tiempo_inicio = pygame.time.get_ticks()/1000
                        pygame.quit()
                        recs1 = Recs(40)
                        salir = False
                        juego(recs1,5,tiempo_inicio,2)

            if cursor1.colliderect(boton4.rect):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
                    salir = False
                    main()

            if event.type == pygame.QUIT:
                salir = False
                sys.exit()

        pantalla.blit(imagenfondo1,(0,0))
        pantalla.blit(info,(180,10))        
        pantalla.blit(info1,(310,150))        
        pantalla.blit(info2,(310,260))        
        pantalla.blit(info3,(310,370))        
        pantalla.blit(info5,(310,480))        
        pantalla.blit(info4,(310,590))
        cursor1.update()
        boton1.update(pantalla,cursor1)
        boton2.update(pantalla,cursor1)
        boton3.update(pantalla,cursor1)
        boton4.update(pantalla,cursor1)
        boton5.update(pantalla,cursor1)
        pygame.display.update()
    pygame.quit()

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((900,675))
    pygame.display.set_caption("Menu de Juego")
    cursor1 = Cursor()
    fuente1 = pygame.font.SysFont("Arial",60,True,True)
    info = fuente1.render("~~Asteroido-Meow~~",0,(140,210,130))
    info1 = fuente1.render("Nuevo Juego",0,(180,180,130))
    info2 = fuente1.render("Salir del Juego",0,(180,180,130))
    rojo1 = pygame.image.load(path+"start.png")
    rojo2 = pygame.image.load(path+"start1.png")
    azul1 = pygame.image.load(path+"exit.png")
    azul2 = pygame.image.load(path+"exit1.png")
    imagenfondo1 = pygame.image.load(path+"planetas.jpg")
    pygame.mixer.music.load(path+"Metalslug3finalboss.mp3")
    boton1 = Boton(rojo1,rojo2,100,250) #x,y
    boton2 = Boton(azul1,azul2,100,450)
    salir = True
    pygame.mixer.music.play(0)
    while salir != False :
        for event in pygame.event.get():
#            if event.type == pygame.MOUSEBUTTONDOWN:
            if cursor1.colliderect(boton1.rect):
                if event.type == pygame.MOUSEBUTTONDOWN:
                        pygame.quit()
                        salir = False
                        menu()
            if cursor1.colliderect(boton2.rect):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
                    salir = False
                    sys.exit()
            if event.type == pygame.QUIT:
                salir = False
                sys.exit()

        pantalla.blit(imagenfondo1,(0,0))
        pantalla.blit(info,(180,10))        
        pantalla.blit(info1,(210,250))        
        pantalla.blit(info2,(210,450))
        cursor1.update()
        boton1.update(pantalla,cursor1)
        boton2.update(pantalla,cursor1)
        pygame.display.update()
    pygame.quit()
main()

if __name__ == " __main__" : main()
