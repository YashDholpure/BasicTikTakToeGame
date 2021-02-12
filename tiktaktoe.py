# psuedo code
"""1:make main window
   2:make 9 tiles
   3:make 1 pointer made of 4 surfaces
   4:game ends when event is quit
   5:need to check that 3 consecutive tiles whether diagonally,horizontally or
   vertically hold the same symbols
   """
import tkinter
import tkinter.messagebox
import pygame
from pygame.locals import (K_UP,K_DOWN,K_LEFT,K_RIGHT,K_RETURN,KEYDOWN)
Height=420
Width=440
pygame.init()
screen=pygame.display.set_mode((Width,Height))
running=True
class Tiles(pygame.sprite.Sprite):
    def __init__(self,initialcordinateX,initialcordinateY,index):
        super().__init__()
        self.surf=pygame.image.load("tile.png").convert()         #tile.png dimensions height=110 width=120
        self.symbol=None
        self.rect=self.surf.get_rect()
        self.rect.move_ip(initialcordinateX,initialcordinateY)
        self.index=index
        self.haveimage=False
        self.havex="Yo"
class Pointer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.cordinates=None
        self.surf=pygame.image.load("topNbottombar.png").convert()    #topNbottombar.png dimensions height=10 width=120
        #self.topbar=pygame.image.load("topNbottombar.png").convert()
        #self.bottombar=pygame.image.load("topNbottombar.png").convert()
        #self.leftbar=pygame.image.load("sidebars.png").convert()
        #self.rightbar=pygame.image.load("sidebars.png").convert()
        self.index=1
        
        #self.toprect=self.topbar.get_rect()
        #self.bottomrect=self.bottombar.get_rect()
        #self.leftrect=self.leftbar.get_rect()
        #self.rightrect=self.rightbar.get_rect()
        self.rect=self.surf.get_rect()
        self.rect.move_ip(20,10)
        #self.toprect.move_ip(10,0)
        #self.bottomrect.move_ip(10,130)
        #self.leftrect.move_ip(0,0)
        #self.rightrect.move_ip(130,10)
        
        
    def move(self,keys):
        if keys[K_UP]:
            self.rect.move_ip(0,-130)
        if keys[K_DOWN]:
            self.rect.move_ip(0,130)
        if keys[K_RIGHT]:
            self.rect.move_ip(140,0)
        if keys[K_LEFT]:
            self.rect.move_ip(-140,0)
            
        if self.rect.left<20:
            self.rect.left=20
        if self.rect.right>420:
            self.rect.right=420
        if self.rect.bottom>250:
            self.rect.bottom=280
        if self.rect.top<10:
            self.rect.top=10
class O(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.surf=pygame.image.load("o.png").convert()
class X(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.surf=pygame.image.load("x.png").convert()
	
clock=pygame.time.Clock()
pointer=Pointer()
tile1=Tiles(20,20,1)
tile2=Tiles(160,20,2)
tile3=Tiles(300,20,3)
tile4=Tiles(20,150,4)
tile5=Tiles(160,150,5)
tile6=Tiles(300,150,6)
tile7=Tiles(20,280,7)
tile8=Tiles(160,280,8)
tile9=Tiles(300,280,9)
tiles=(tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile9)
pointer_index_cordinates={'1':'<rect(20, 10, 120, 10)>','2':'<rect(160, 10, 120, 10)>','3':'<rect(300, 10, 120, 10)>','4':'<rect(20, 140, 120, 10)>','5':'<rect(160, 140, 120, 10)>','6':'<rect(300, 140, 120, 10)>','7':'<rect(20, 270, 120, 10)>','8':'<rect(160, 270, 120, 10)>','9':'<rect(300, 270, 120, 10)>'}
#pointerimages=[pointer.leftbar,pointer.rightbar,pointer.bottombar,pointer.topbar]
#pointerrects=[pointer.leftrect,pointer.rightrect,pointer.bottomrect,pointer.toprect]
o=O()
x=X()
xturn=True
oturn=False
#pointerrect=((0,0),(130,0),(10,-130),(10,0))


while running:
	for index,xy in pointer_index_cordinates.items():
		pointerrect=str(pointer.rect)
		if pointerrect==xy:
			pointer.index=int(index)#FF0000#0F0B0B
	pressed_key=pygame.key.get_pressed()
	pointer.move(pressed_key)
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			running=False
		if event.type==KEYDOWN:
			if event.key==K_RETURN:
				for tile in tiles:
					if tile.index==pointer.index:
						if not tile.haveimage:

							if xturn:
								tile.surf.blit(x.surf,(0,0))
								tile.havex=True
								xturn=False
								tile.haveimage=True
								if tile1.havex==True and tile2.havex==True and tile3.havex==True:
									tkinter.messagebox.showinfo("X win!!")
								elif tile4.havex==True and tile5.havex==True and tile6.havex==True:
									tkinter.messagebox.showinfo("X win!!")
								elif tile7.havex==True and tile8.havex==True and tile9.havex==True:
									tkinter.messagebox.showinfo("X win!!")
								elif tile1.havex==True and tile4.havex==True and tile7.havex==True:
									tkinter.messagebox.showinfo("X win!!")
								elif tile2.havex==True and tile5.havex==True and tile8.havex==True:
									tkinter.messagebox.showinfo("X win!!")
								elif tile3.havex==True and tile6.havex==True and tile9.havex==True:
									tkinter.messagebox.showinfo("X win!!")
								elif tile1.havex==True and tile5.havex==True and tile9.havex==True:
									tkinter.messagebox.showinfo("X win!!")
								elif tile3.havex==True and tile5.havex==True and tile7.havex==True:
									tkinter.messagebox.showinfo("X win!!")


							else:
								tile.surf.blit(o.surf,(0,0))
								tile.havex=False
								xturn=True
								tile.haveimage=True
								if tile1.havex==False and tile2.havex==False and tile3.havex==False:
									tkinter.messagebox.showinfo("O win!!")
								elif tile4.havex==False and tile5.havex==False and tile6.havex==False:
									tkinter.messagebox.showinfo("O win!!")
								elif tile7.havex==False and tile8.havex==False and tile9.havex==False:
									tkinter.messagebox.showinfo("O win!!")
								elif tile1.havex==False and tile4.havex==False and tile7.havex==False:
									tkinter.messagebox.showinfo("O win!!")
								elif tile2.havex==False and tile5.havex==False and tile8.havex==False:
									tkinter.messagebox.showinfo("O win!!")
								elif tile3.havex==False and tile6.havex==False and tile9.havex==False:
									tkinter.messagebox.showinfo("O win!!")
								elif tile1.havex==False and tile5.havex==False and tile9.havex==False:
									tkinter.messagebox.showinfo("O win!!")
								elif tile3.havex==False and tile5.havex==False and tile7.havex==False:
									tkinter.messagebox.showinfo("O win!!")




						
	screen.blit(pointer.surf,pointer.rect)
	screen.blit(tile1.surf,tile1.rect)
	screen.blit(tile2.surf, tile2.rect)
	screen.blit(tile3.surf,tile3.rect)
	screen.blit(tile4.surf,tile4.rect)
	screen.blit(tile5.surf,tile5.rect)
	screen.blit(tile6.surf,tile6.rect)
	screen.blit(tile7.surf,tile7.rect)
	screen.blit(tile8.surf,tile8.rect)
	screen.blit(tile9.surf,tile9.rect)
	pygame.display.flip()
	screen.fill((255,255,255))
	clock.tick(5)
pygame.quit()


        
    
        
        
    

