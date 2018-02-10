# Author Name: Zhang Ruofan
# AndrewID: ruofanz
# Note that the MVC structure is from the 15112 lesson
import pygame
import math
import random
import cv2
import numpy
cap = cv2.VideoCapture(0)


screenSize = (1280,720)

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(screenSize,0,32)


running = True

#backgroundImage = pygame.image.load("images/background.jpg").convert()
backgroundImage = pygame.transform.scale(pygame.image.load("images/background.jpg"),\
                                  screenSize).convert()


menuSound = pygame.mixer.Sound("sound/menu.ogg")
startSound = pygame.mixer.Sound("sound/start.ogg")
boomSound = pygame.mixer.Sound("sound/boom.ogg")
throwSound = pygame.mixer.Sound("sound/throw.ogg")
splatterSound = pygame.mixer.Sound("sound/splatter.ogg")
overSound = pygame.mixer.Sound("sound/over.ogg")

appleImage = pygame.image.load("images/fruit/apple.png")
apple_1Image = pygame.image.load("images/fruit/apple-1.png")
apple_2Image = pygame.image.load("images/fruit/apple-2.png")
bananaImage = pygame.image.load("images/fruit/banana.png")
banana_1Image = pygame.image.load("images/fruit/banana-1.png")
banana_2Image = pygame.image.load("images/fruit/banana-2.png")
basahaImage = pygame.image.load("images/fruit/basaha.png")
basaha_1Image = pygame.image.load("images/fruit/basaha-1.png")
basaha_2Image = pygame.image.load("images/fruit/basaha-2.png")
peachImage = pygame.image.load("images/fruit/peach.png")
peach_1Image = pygame.image.load("images/fruit/peach-1.png")
peach_2Image = pygame.image.load("images/fruit/peach-2.png")
sandiaImage = pygame.image.load("images/fruit/sandia.png")
sandia_1Image = pygame.image.load("images/fruit/sandia-1.png")
sandia_2Image = pygame.image.load("images/fruit/sandia-2.png")
bombImage = pygame.image.load("images/fruit/boom.png")

gameOverImage = pygame.image.load("images/game-over.png")




# Apple class
class apple(object):
    def __init__(self, x, y, vx, vy, g, rotateAngle):
        self.isValid = True
        self.isOut = False
        self.name = "apple"
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.g = g
        self.rotateAngle = rotateAngle
        self.mainImage = appleImage
        self.slice1Image = apple_1Image
        self.slice2Image = apple_2Image
        self.w , self.h = self.mainImage.get_size()
        self.r = (self.w + self.h)/4*1.2

# Banana class
class banana(object):
    def __init__(self, x, y, vx, vy, g, rotateAngle):
        self.isValid = True
        self.isOut = False
        self.name = "banana"
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.g = g
        self.rotateAngle = rotateAngle
        self.mainImage = bananaImage
        self.slice1Image = banana_1Image
        self.slice2Image = banana_2Image
        self.w , self.h = self.mainImage.get_size()
        self.r = (self.w + self.h)/4*1.2        

# Basaha class
class basaha(object):
    def __init__(self, x, y, vx, vy, g, rotateAngle):
        self.isValid = True
        self.isOut = False
        self.name = "basaha"
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.g = g
        self.rotateAngle = rotateAngle
        self.mainImage = basahaImage
        self.slice1Image = basaha_1Image
        self.slice2Image = basaha_2Image
        self.w , self.h = self.mainImage.get_size()
        self.r = (self.w + self.h)/4*1.2


# Peach class
class peach(object):
    def __init__(self, x, y, vx, vy, g, rotateAngle):
        self.isValid = True
        self.isOut = False
        self.name = "peach"
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.g = g
        self.rotateAngle = rotateAngle
        self.mainImage = peachImage
        self.slice1Image = peach_1Image
        self.slice2Image = peach_2Image
        self.w , self.h = self.mainImage.get_size()
        self.r = (self.w + self.h)/4*1.2

# Sandia class
class sandia(object):
    def __init__(self, x, y, vx, vy, g, rotateAngle):
        self.isValid = True
        self.isOut = False
        self.name = "sandia"
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.g = g
        self.rotateAngle = rotateAngle
        self.mainImage = sandiaImage
        self.slice1Image = sandia_1Image
        self.slice2Image = sandia_2Image
        self.w , self.h = self.mainImage.get_size()
        self.r = (self.w + self.h)/4*1.2

# Bomb class
class bomb(object):
    def __init__(self, x, y, vx, vy, g, rotateAngle):
        self.isValid = True
        self.isOut = False
        self.name = "bomb"
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.g = g
        self.rotateAngle = rotateAngle
        self.mainImage = bombImage
        self.w , self.h = self.mainImage.get_size()
        self.r = (self.w + self.h)/4*1.2        

# Fruit ninja logo
class logo(object):
    def __init__(self):
        self.logoImage = pygame.image.load("images/logo.png")
        self.w , self.h = self.logoImage.get_size()
        self.x = screenSize[0]/2-self.w/2
        self.y = 0
        
# Another Fruit ninja logo
class ninja(object):
    def __init__(self):
        self.ninjaImage = pygame.image.load("images/ninja.png")
        self.w , self.h = self.ninjaImage.get_size()
        self.x = screenSize[0]/2-self.w/2
        self.y = screenSize[1]/4-self.h/2

# New Game mode logo
class newGame(object):
    def __init__(self):
        self.innerImage = pygame.image.load("images/fruit/sandia.png")
        self.outterImage = pygame.image.load("images/new-game.png")
        self.innerW , self.innerH = self.innerImage.get_size()
        self.outterW, self.outterH = self.outterImage.get_size()
        self.innerX = screenSize[0]/4 - self.innerW/2
        self.innerY = screenSize[1]*3/4 - self.innerH/2
        self.outterX = screenSize[0]/4 - self.outterW/2
        self.outterY = screenSize[1]*3/4 - self.outterH/2
        self.innerAngle = 0
        self.outterAngle = 360
        self.r = (self.innerW + self.innerH)/4
        self.fixX = screenSize[0]/4
        self.fixY = screenSize[1]*3/4
        self.fixX1 = screenSize[0]/3
        self.fixY1 = screenSize[1]/2
        
# Instruction mode logo
class dojo(object):
    def __init__(self):
        self.innerImage = pygame.image.load("images/fruit/apple.png")
        self.outterImage = pygame.image.load("images/dojo.png")
        self.innerW , self.innerH = self.innerImage.get_size()
        self.outterW, self.outterH = self.outterImage.get_size()
        self.innerX = screenSize[0]*2/4 - self.innerW/2
        self.innerY = screenSize[1]*3/4 - self.innerH/2
        self.outterX = screenSize[0]*2/4 - self.outterW/2
        self.outterY = screenSize[1]*3/4 - self.outterH/2
        self.innerAngle = 90
        self.outterAngle = 90
        self.r = (self.innerW + self.innerH)/4
        self.fixX = screenSize[0]*2/4
        self.fixY = screenSize[1]*3/4

# Quit Game mode logo
class quitGame(object):
    def __init__(self):
        self.innerImage = pygame.image.load("images/fruit/boom.png")
        self.outterImage = pygame.image.load("images/quit.png")
        self.innerW , self.innerH = self.innerImage.get_size()
        self.outterW, self.outterH = self.outterImage.get_size()
        self.innerX = screenSize[0]*3/4 - self.innerW/2
        self.innerY = screenSize[1]*3/4 - self.innerH/2
        self.outterX = screenSize[0]*3/4 - self.outterW/2
        self.outterY = screenSize[1]*3/4 - self.outterH/2
        self.innerAngle = 180
        self.outterAngle = 180
        self.r = (self.innerW + self.innerH)/4
        self.fixX = screenSize[0]*3/4
        self.fixY = screenSize[1]*3/4
        self.fixX1 = screenSize[0]*2/3
        self.fixY1 = screenSize[1]/2
        self.fixXdojo = screenSize[0]*9.4/10 
        self.fixYdojo = screenSize[1]*8.9/10

# OpenCV mode logo
class openCVlogo(object):
    def __init__(self):
        self.w = 120
        self.h = 120
        self.image = pygame.transform.scale(\
            pygame.image.load("images/openCV.png"),(self.w,self.h))
        self.x = screenSize[0]/2 - self.w/2
        self.y = screenSize[1]/2 - self.h/2
        self.fixX = screenSize[0]/2
        self.fixY = screenSize[1]/2


# The score of the game        
class gameScore(object):
    def __init__(self):
        self.image = pygame.transform.scale(pygame.image.load("images/score.png"),(64,64))
        self.x = screenSize[0]/50
        self.y = screenSize[1]/50
        self.w, self.h = self.image.get_size()
        

# Initialize all the game data  
def init(data):

    data.ret,data.frame_origin = cap.read()
    data.arfa = 10

    data.hand1PosX = 0
    data.hand1PosY = 0

    data.videoCnt = 0
    
    data.xsize = int(len(data.frame_origin)/data.arfa)
    data.ysize = int(len(data.frame_origin[0])/data.arfa)

    data.xPosArray = []
    for i in range(data.xsize):
        data.xPosArray.append(numpy.arange(data.ysize))


    data.yPosArray = numpy.zeros((data.xsize,data.ysize))
    for i in range(data.xsize):
        data.yPosArray[i] = numpy.add(data.yPosArray[i],i)

    data.testPicture = numpy.zeros((data.xsize,data.ysize))


    
    pygame.mixer.Sound.stop(menuSound)    
    pygame.mixer.Sound.play(menuSound)
    data.score = 0
    data.timeLeft = 60
    data.timeCount = 0
    data.x = 0
    data.y = 0
    data.rotateAngle = 0
    data.logo = logo()
    data.ninja = ninja()
    data.newGame = newGame()
    data.gameScore = gameScore()
    data.openCVlogo = openCVlogo()
    data.count = 0
    data.randomIndexLocation = 0
    data.randomIndexFruit = 0
    data.width = screenSize[0]
    data.height = screenSize[1]
    data.fruits = []
    data.bombs = []
    data.bombPosibility = 10
    
    data.knifePointsNumber = 12
    data.knifePoints = []

    data.cutFruitFlag = False
    data.cutFruitCount = 0
    data.cutCruitConnectTimeLeft = 0

    data.comboFlag = False
    data.comboTime = 0
    data.comboTimeLeft = 0
    data.comboCount = 0
    data.speed = 1
    

    data.showComboFlag = False
    data.showComboTimeLeft = 0
    
    data.dojo = dojo()
    data.quitGame = quitGame()
    data.modes = ["menu", "newGame","newGameGameOver","dojo", "help"]
    data.mode = data.modes[0]

# Init continuously cutting fruit.
def initCutFruit(data):
    data.cutFruitFlag = False
    data.cutFruitCount = 0
    data.cutCruitConnectTimeLeft = 0    

# Init all things about combo
def initCombo(data):
    data.comboFlag = False
    data.comboTime = 0
    data.comboTimeLeft = 0
    data.comboCount = 0
    data.showComboFlag = False
    data.showComboTimeLeft = 0
    data.speed = 1
    data.bombPosibility = 10

# MVC structure
class Struct(object): pass
data = Struct()
init(data)


# Create the fruits' coming location
def createLocation(data):
    data.randomIndexLocation = random.randint(0,1)

# Create one fruit
def createFruit(data):

    data.randomIndexFruit = random.randint(0,4)

    if(data.randomIndexLocation == 0):
        
        x = random.randint(data.width*2/10,data.width*8/10)
        y = data.height
        vx = 0*data.speed
        vy = int(-data.height/15/3)*data.speed
        g = (data.height/300/12)*(data.speed**2)
        rotateAngle = random.randint(0,360)
        if(data.randomIndexFruit == 0):
            newApple = apple(x,y,vx,vy,g,rotateAngle)
            data.fruits.append(newApple)
        if(data.randomIndexFruit == 1):
            newBanana = banana(x,y,vx,vy,g,rotateAngle)
            data.fruits.append(newBanana)
        if(data.randomIndexFruit == 2):
            newBasaha = basaha(x,y,vx,vy,g,rotateAngle)
            data.fruits.append(newBasaha)
        if(data.randomIndexFruit == 3):
            newPeach = peach(x,y,vx,vy,g,rotateAngle)
            data.fruits.append(newPeach)
        if(data.randomIndexFruit == 4):
            newSandia = sandia(x,y,vx,vy,g,rotateAngle)
            data.fruits.append(newSandia)
    if(data.randomIndexLocation == 1):
        x = 0
        y = random.randint(data.height/3,data.height*1/2)
        vx = int(data.width/30/3)*data.speed
        vy = int(-data.height/60/3)*data.speed
        g = (data.height/300/24)*(data.speed**2)
        rotateAngle = random.randint(0,360)
        if(data.randomIndexFruit == 0):
            newApple = apple(x,y,vx,vy,g,rotateAngle)
            data.fruits.append(newApple)
        if(data.randomIndexFruit == 1):
            newBanana = banana(x,y,vx,vy,g,rotateAngle)
            data.fruits.append(newBanana)
        if(data.randomIndexFruit == 2):
            newBasaha = basaha(x,y,vx,vy,g,rotateAngle)
            data.fruits.append(newBasaha)
        if(data.randomIndexFruit == 3):
            newPeach = peach(x,y,vx,vy,g,rotateAngle)
            data.fruits.append(newPeach)
        if(data.randomIndexFruit == 4):
            newSandia = sandia(x,y,vx,vy,g,rotateAngle)
            data.fruits.append(newSandia)
    pygame.mixer.Sound.play(throwSound)

# Create one bomb
def createBomb(data):
    createOrNot = True
    temp = random.randint(0,100)
    if(temp < data.bombPosibility):
        createOrNot = True
    else:
        createOrNot = False
        
    if(createOrNot == True):
        x = random.randint(data.width*2/10,data.width*8/10)
        y = data.height
        vx = 0*data.speed
        vy = int(-data.height/15/3)*data.speed
        g = (data.height/300/12)*(data.speed**2)
        rotateAngle = random.randint(0,360)
        newBomb = bomb(x,y,vx,vy,g,rotateAngle)
        data.bombs.append(newBomb)
        pygame.mixer.Sound.play(throwSound)    

# Redraw all the pictures
def reDrawAll():


    if(data.mode == "menu"):
        screen.blit(backgroundImage,(0,0))
        screen.blit(data.logo.logoImage,(data.logo.x,data.logo.y))
        screen.blit(data.ninja.ninjaImage,(data.ninja.x,data.ninja.y))

    #newGame   
        data.newGame.innerW, data.newGame.innerH= \
            pygame.transform.rotate(data.newGame.innerImage,data.newGame.innerAngle).get_size()
        data.newGame.innerX = screenSize[0]/4 - data.newGame.innerW/2
        data.newGame.innerY = screenSize[1]*3/4 - data.newGame.innerH/2
        screen.blit(pygame.transform.rotate(data.newGame.innerImage,data.newGame.innerAngle), \
                    (data.newGame.innerX, data.newGame.innerY))

        data.newGame.outterW, data.newGame.outterH= \
            pygame.transform.rotate(data.newGame.outterImage,data.newGame.outterAngle).get_size()
        data.newGame.outterX = screenSize[0]/4 - data.newGame.outterW/2
        data.newGame.outterY = screenSize[1]*3/4 - data.newGame.outterH/2
        screen.blit(pygame.transform.rotate(data.newGame.outterImage,data.newGame.outterAngle), \
                    (data.newGame.outterX, data.newGame.outterY))

    #dojo
        data.dojo.innerW, data.dojo.innerH= \
            pygame.transform.rotate(data.dojo.innerImage,data.dojo.innerAngle).get_size()
        data.dojo.innerX = screenSize[0]*2/4 - data.dojo.innerW/2
        data.dojo.innerY = screenSize[1]*3/4 - data.dojo.innerH/2
        screen.blit(pygame.transform.rotate(data.dojo.innerImage,data.dojo.innerAngle), \
                    (data.dojo.innerX, data.dojo.innerY))

        data.dojo.outterW, data.dojo.outterH= \
            pygame.transform.rotate(data.dojo.outterImage,data.dojo.outterAngle).get_size()
        data.dojo.outterX = screenSize[0]*2/4 - data.dojo.outterW/2
        data.dojo.outterY = screenSize[1]*3/4 - data.dojo.outterH/2
        screen.blit(pygame.transform.rotate(data.dojo.outterImage,data.dojo.outterAngle), \
                    (data.dojo.outterX, data.dojo.outterY))

    #quitGame
        data.quitGame.innerW, data.quitGame.innerH= \
            pygame.transform.rotate(data.quitGame.innerImage,data.quitGame.innerAngle).get_size()
        data.quitGame.innerX = screenSize[0]*3/4 - data.quitGame.innerW/2
        data.quitGame.innerY = screenSize[1]*3/4 - data.quitGame.innerH/2
        screen.blit(pygame.transform.rotate(data.quitGame.innerImage,data.quitGame.innerAngle), \
                    (data.quitGame.innerX, data.quitGame.innerY))

        data.quitGame.outterW, data.quitGame.outterH= \
            pygame.transform.rotate(data.quitGame.outterImage,data.quitGame.outterAngle).get_size()
        data.quitGame.outterX = screenSize[0]*3/4 - data.quitGame.outterW/2
        data.quitGame.outterY = screenSize[1]*3/4 - data.quitGame.outterH/2
        screen.blit(pygame.transform.rotate(data.quitGame.outterImage,data.quitGame.outterAngle), \
                    (data.quitGame.outterX, data.quitGame.outterY))
    #openCVlogo
        screen.blit(data.openCVlogo.image,(data.openCVlogo.x,data.openCVlogo.y))
        


    if(data.mode == "newGame"):
        screen.blit(backgroundImage,(0,0))

    #quitGame
        data.quitGame.innerW, data.quitGame.innerH= \
            pygame.transform.rotate(data.quitGame.innerImage,data.quitGame.innerAngle).get_size()
        data.quitGame.innerX = data.quitGame.fixXdojo - data.quitGame.innerW/2
        data.quitGame.innerY = data.quitGame.fixYdojo - data.quitGame.innerH/2
        screen.blit(pygame.transform.rotate(data.quitGame.innerImage,data.quitGame.innerAngle), \
                    (data.quitGame.innerX, data.quitGame.innerY))

        data.quitGame.outterW, data.quitGame.outterH= \
            pygame.transform.rotate(data.quitGame.outterImage,data.quitGame.outterAngle).get_size()
        data.quitGame.outterX = data.quitGame.fixXdojo - data.quitGame.outterW/2
        data.quitGame.outterY = data.quitGame.fixYdojo - data.quitGame.outterH/2
        screen.blit(pygame.transform.rotate(data.quitGame.outterImage,data.quitGame.outterAngle), \
                    (data.quitGame.outterX, data.quitGame.outterY))

        if(data.showComboFlag == True):
            data.showComboTimeLeft -= 1
            if(data.showComboTimeLeft <= 0):
                data.showComboFlag = False
            myFont = pygame.font.SysFont("arial",64)
            text_surface = myFont.render("Combo" +\
                                         " : " + " + " + str(data.comboCount * 5),True,(255,255,255))
            w,h = text_surface.get_size()
            x = screenSize[0]/2 - w/2
            y = screenSize[1]/2 - h/2
            screen.blit(text_surface,(x,y))            

        for i in data.fruits:
            if(i.isValid == True):
                w,h = pygame.transform.rotate(i.mainImage, i.rotateAngle).get_size()
                screen.blit(pygame.transform.rotate(i.mainImage, i.rotateAngle),\
                            (i.x-w/2, i.y-h/2))
            else:
                if(i.name == "basaha"):
                    w,h = pygame.transform.rotate(i.slice1Image, i.rotateAngle).get_size()
                    screen.blit(pygame.transform.rotate(i.slice1Image, i.rotateAngle),\
                                (i.x-w/2, i.y-h/2))
                    w,h = pygame.transform.rotate(i.slice2Image, i.rotateAngle).get_size()
                    screen.blit(pygame.transform.rotate(i.slice2Image, i.rotateAngle),\
                                (i.x, i.y))
                elif(i.name == "apple"):
                    w,h = pygame.transform.rotate(i.slice1Image, i.rotateAngle).get_size()
                    screen.blit(pygame.transform.rotate(i.slice1Image, i.rotateAngle),\
                                (i.x-w/2, i.y+h/2))
                    w,h = pygame.transform.rotate(i.slice2Image, i.rotateAngle).get_size()
                    screen.blit(pygame.transform.rotate(i.slice2Image, i.rotateAngle),\
                                (i.x, i.y))
                elif(i.name == "banana"):
                    w,h = pygame.transform.rotate(i.slice1Image, i.rotateAngle).get_size()
                    screen.blit(pygame.transform.rotate(i.slice1Image, i.rotateAngle),\
                                (i.x-w/2, i.y))
                    w,h = pygame.transform.rotate(i.slice2Image, i.rotateAngle).get_size()
                    screen.blit(pygame.transform.rotate(i.slice2Image, i.rotateAngle),\
                                (i.x, i.y))
                elif(i.name == "peach"):
                    w,h = pygame.transform.rotate(i.slice1Image, i.rotateAngle).get_size()
                    screen.blit(pygame.transform.rotate(i.slice1Image, i.rotateAngle),\
                                (i.x-w/2, i.y+h/2))
                    w,h = pygame.transform.rotate(i.slice2Image, i.rotateAngle).get_size()
                    screen.blit(pygame.transform.rotate(i.slice2Image, i.rotateAngle),\
                                (i.x, i.y))
                elif(i.name == "sandia"):
                    w,h = pygame.transform.rotate(i.slice1Image, i.rotateAngle).get_size()
                    screen.blit(pygame.transform.rotate(i.slice1Image, i.rotateAngle),\
                                (i.x-w/2, i.y))
                    w,h = pygame.transform.rotate(i.slice2Image, i.rotateAngle).get_size()
                    screen.blit(pygame.transform.rotate(i.slice2Image, i.rotateAngle),\
                                (i.x, i.y))                    
                    
        for i in data.bombs:
            w,h = pygame.transform.rotate(i.mainImage, i.rotateAngle).get_size()
            screen.blit(pygame.transform.rotate(i.mainImage, i.rotateAngle),\
                        (i.x-w/2, i.y-h/2))            
        



        screen.blit(data.gameScore.image, (data.gameScore.x, data.gameScore.y))

        myFont = pygame.font.SysFont("arial",64)
        text_surface = myFont.render("Score: " + str(data.score),True,(255,255,255))
        x = data.gameScore.x + data.gameScore.w*1.2
        y = data.gameScore.y
        screen.blit(text_surface,(x,y))

        myFont = pygame.font.SysFont("arial",64)
        text_surface = myFont.render("Speed: " + str(data.speed),True,(255,255,255))
        x = data.gameScore.x + data.gameScore.w*5.7
        y = data.gameScore.y
        screen.blit(text_surface,(x,y))

        myFont = pygame.font.SysFont("arial",64)
        text_surface = myFont.render("Bomb Posibility: " \
                + str(int((1-(1-(data.bombPosibility/100))**2)*100)/100)\
                                     ,True,(255,255,255))
        x = data.gameScore.x + data.gameScore.w*10.7
        y = data.gameScore.y
        screen.blit(text_surface,(x,y)) 

        myFont = pygame.font.SysFont("arial",64)
        text_surface = myFont.render("Time Left: "+str(data.timeLeft),True,(255,255,255))
        x = data.gameScore.x
        y = data.height - data.gameScore.y - 64
        screen.blit(text_surface,(x,y))

    if(data.mode == "openCV"):
        screen.blit(backgroundImage,(0,0))

    #quitGame
        data.quitGame.innerW, data.quitGame.innerH= \
            pygame.transform.rotate(data.quitGame.innerImage,data.quitGame.innerAngle).get_size()
        data.quitGame.innerX = data.quitGame.fixXdojo - data.quitGame.innerW/2
        data.quitGame.innerY = data.quitGame.fixYdojo - data.quitGame.innerH/2
        screen.blit(pygame.transform.rotate(data.quitGame.innerImage,data.quitGame.innerAngle), \
                    (data.quitGame.innerX, data.quitGame.innerY))

        data.quitGame.outterW, data.quitGame.outterH= \
            pygame.transform.rotate(data.quitGame.outterImage,data.quitGame.outterAngle).get_size()
        data.quitGame.outterX = data.quitGame.fixXdojo - data.quitGame.outterW/2
        data.quitGame.outterY = data.quitGame.fixYdojo - data.quitGame.outterH/2
        screen.blit(pygame.transform.rotate(data.quitGame.outterImage,data.quitGame.outterAngle), \
                    (data.quitGame.outterX, data.quitGame.outterY))

        if(data.showComboFlag == True):
            data.showComboTimeLeft -= 1
            if(data.showComboTimeLeft <= 0):
                data.showComboFlag = False
            myFont = pygame.font.SysFont("arial",64)
            text_surface = myFont.render("Combo" +\
                    " : " + " + " + str(data.comboCount * 5),True,(255,255,255))
            w,h = text_surface.get_size()
            x = screenSize[0]/2 - w/2
            y = screenSize[1]/2 - h/2
            screen.blit(text_surface,(x,y))            

        for i in data.fruits:
            if(i.isValid == True):
                w,h = pygame.transform.rotate(i.mainImage, i.rotateAngle).get_size()
                screen.blit(pygame.transform.rotate(i.mainImage, i.rotateAngle),\
                            (i.x-w/2, i.y-h/2))
            else:
                if(i.name == "basaha"):
                    w,h = pygame.transform.rotate(i.slice1Image, i.rotateAngle).get_size()
                    screen.blit(pygame.transform.rotate(i.slice1Image, i.rotateAngle),\
                                (i.x-w/2, i.y-h/2))
                    w,h = pygame.transform.rotate(i.slice2Image, i.rotateAngle).get_size()
                    screen.blit(pygame.transform.rotate(i.slice2Image, i.rotateAngle),\
                                (i.x, i.y))
                elif(i.name == "apple"):
                    w,h = pygame.transform.rotate(i.slice1Image, i.rotateAngle).get_size()
                    screen.blit(pygame.transform.rotate(i.slice1Image, i.rotateAngle),\
                                (i.x-w/2, i.y+h/2))
                    w,h = pygame.transform.rotate(i.slice2Image, i.rotateAngle).get_size()
                    screen.blit(pygame.transform.rotate(i.slice2Image, i.rotateAngle),\
                                (i.x, i.y))
                elif(i.name == "banana"):
                    w,h = pygame.transform.rotate(i.slice1Image, i.rotateAngle).get_size()
                    screen.blit(pygame.transform.rotate(i.slice1Image, i.rotateAngle),\
                                (i.x-w/2, i.y))
                    w,h = pygame.transform.rotate(i.slice2Image, i.rotateAngle).get_size()
                    screen.blit(pygame.transform.rotate(i.slice2Image, i.rotateAngle),\
                                (i.x, i.y))
                elif(i.name == "peach"):
                    w,h = pygame.transform.rotate(i.slice1Image, i.rotateAngle).get_size()
                    screen.blit(pygame.transform.rotate(i.slice1Image, i.rotateAngle),\
                                (i.x-w/2, i.y+h/2))
                    w,h = pygame.transform.rotate(i.slice2Image, i.rotateAngle).get_size()
                    screen.blit(pygame.transform.rotate(i.slice2Image, i.rotateAngle),\
                                (i.x, i.y))
                elif(i.name == "sandia"):
                    w,h = pygame.transform.rotate(i.slice1Image, i.rotateAngle).get_size()
                    screen.blit(pygame.transform.rotate(i.slice1Image, i.rotateAngle),\
                                (i.x-w/2, i.y))
                    w,h = pygame.transform.rotate(i.slice2Image, i.rotateAngle).get_size()
                    screen.blit(pygame.transform.rotate(i.slice2Image, i.rotateAngle),\
                                (i.x, i.y)) 
        for i in data.bombs:
            w,h = pygame.transform.rotate(i.mainImage, i.rotateAngle).get_size()
            screen.blit(pygame.transform.rotate(i.mainImage, i.rotateAngle),\
                        (i.x-w/2, i.y-h/2))            
        
            


        screen.blit(data.gameScore.image, (data.gameScore.x, data.gameScore.y))

        myFont = pygame.font.SysFont("arial",64)
        text_surface = myFont.render("Score: " + str(data.score),True,(255,255,255))
        x = data.gameScore.x + data.gameScore.w*1.2
        y = data.gameScore.y
        screen.blit(text_surface,(x,y))

        myFont = pygame.font.SysFont("arial",64)
        text_surface = myFont.render("Speed: " + str(data.speed),True,(255,255,255))
        x = data.gameScore.x + data.gameScore.w*5.7
        y = data.gameScore.y
        screen.blit(text_surface,(x,y))

        myFont = pygame.font.SysFont("arial",64)
        text_surface = myFont.render("Bomb Posibility: " \
                    + str(int((1-(1-(data.bombPosibility/100))**2)*100)/100),\
                                     True,(255,255,255))
        x = data.gameScore.x + data.gameScore.w*10.7
        y = data.gameScore.y
        screen.blit(text_surface,(x,y)) 

        myFont = pygame.font.SysFont("arial",64)
        text_surface = myFont.render("Time Left: "+str(data.timeLeft),True,(255,255,255))
        x = data.gameScore.x
        y = data.height - data.gameScore.y - 64
        screen.blit(text_surface,(x,y))


    if(data.mode == "newGameGameOver"):
        screen.blit(backgroundImage,(0,0))        

    #newGame   
        data.newGame.innerW, data.newGame.innerH= \
            pygame.transform.rotate(data.newGame.innerImage,data.newGame.innerAngle).get_size()
        data.newGame.innerX = screenSize[0]/3 - data.newGame.innerW/2
        data.newGame.innerY = screenSize[1]/2 - data.newGame.innerH/2
        screen.blit(pygame.transform.rotate(data.newGame.innerImage,data.newGame.innerAngle), \
                    (data.newGame.innerX, data.newGame.innerY))

        data.newGame.outterW, data.newGame.outterH= \
            pygame.transform.rotate(data.newGame.outterImage,data.newGame.outterAngle).get_size()
        data.newGame.outterX = screenSize[0]/3 - data.newGame.outterW/2
        data.newGame.outterY = screenSize[1]/2 - data.newGame.outterH/2
        screen.blit(pygame.transform.rotate(data.newGame.outterImage,data.newGame.outterAngle), \
                    (data.newGame.outterX, data.newGame.outterY))

    #quitGame
        data.quitGame.innerW, data.quitGame.innerH= \
            pygame.transform.rotate(data.quitGame.innerImage,data.quitGame.innerAngle).get_size()
        data.quitGame.innerX = screenSize[0]*2/3 - data.quitGame.innerW/2
        data.quitGame.innerY = screenSize[1]/2 - data.quitGame.innerH/2
        screen.blit(pygame.transform.rotate(data.quitGame.innerImage,data.quitGame.innerAngle), \
                    (data.quitGame.innerX, data.quitGame.innerY))

        data.quitGame.outterW, data.quitGame.outterH= \
            pygame.transform.rotate(data.quitGame.outterImage,data.quitGame.outterAngle).get_size()
        data.quitGame.outterX = screenSize[0]*2/3 - data.quitGame.outterW/2
        data.quitGame.outterY = screenSize[1]/2 - data.quitGame.outterH/2
        screen.blit(pygame.transform.rotate(data.quitGame.outterImage,data.quitGame.outterAngle), \
                    (data.quitGame.outterX, data.quitGame.outterY))
    #score
        myFont = pygame.font.SysFont("arial",64)
        text_surface = myFont.render("Score: " + str(data.score),True,(255,255,255))
        w,h = text_surface.get_size()
        x = screenSize[0]/2 - w/2
        y = screenSize[1]*3/4 - h/2
        screen.blit(text_surface,(x,y))        
    #gameOverImage
        w,h = gameOverImage.get_size()
        x = screenSize[0]/2 - w/2
        y = screenSize[1]/4 - h/2
        screen.blit(gameOverImage,(x,y))

    if(data.mode == "openCVGameOver"):
        screen.blit(backgroundImage,(0,0))        


    #quitGame
        data.quitGame.innerW, data.quitGame.innerH= \
            pygame.transform.rotate(data.quitGame.innerImage,data.quitGame.innerAngle).get_size()
        data.quitGame.innerX = screenSize[0]*1/2 - data.quitGame.innerW/2
        data.quitGame.innerY = screenSize[1]/2 - data.quitGame.innerH/2
        screen.blit(pygame.transform.rotate(data.quitGame.innerImage,data.quitGame.innerAngle), \
                    (data.quitGame.innerX, data.quitGame.innerY))

        data.quitGame.outterW, data.quitGame.outterH= \
            pygame.transform.rotate(data.quitGame.outterImage,data.quitGame.outterAngle).get_size()
        data.quitGame.outterX = screenSize[0]*1/2 - data.quitGame.outterW/2
        data.quitGame.outterY = screenSize[1]/2 - data.quitGame.outterH/2
        screen.blit(pygame.transform.rotate(data.quitGame.outterImage,data.quitGame.outterAngle), \
                    (data.quitGame.outterX, data.quitGame.outterY))
    #score
        myFont = pygame.font.SysFont("arial",64)
        text_surface = myFont.render("Score: " + str(data.score),True,(255,255,255))
        w,h = text_surface.get_size()
        x = screenSize[0]/2 - w/2
        y = screenSize[1]*3/4 - h/2
        screen.blit(text_surface,(x,y))        
    #gameOverImage
        w,h = gameOverImage.get_size()
        x = screenSize[0]/2 - w/2
        y = screenSize[1]/4 - h/2
        screen.blit(gameOverImage,(x,y))

        
    #cursor
    for i in range(len(data.knifePoints)-1):
        x1 = data.knifePoints[i][0]
        y1 = data.knifePoints[i][1]
        x2 = data.knifePoints[i+1][0]
        y2 = data.knifePoints[i+1][1]
        pygame.draw.line(screen, (255, 255, 255),(x1,y1), (x2,y2), 5)
        
    if(data.mode == "dojo"):
        screen.blit(backgroundImage,(0,0))
    #introduction
        myFont = pygame.font.SysFont("arial",64)
        text_surface = myFont.render("Cut fruits to gain score.",True,(255,255,255))
        w,h = text_surface.get_size()
        x = screenSize[0]/2 - w/2
        y = screenSize[1]/10 - h/2
        screen.blit(text_surface,(x,y))

        myFont = pygame.font.SysFont("arial",64)
        text_surface = myFont.render("Cut at least 3 fruits to gain Combo.",True,(255,255,255))
        w,h = text_surface.get_size()
        x = screenSize[0]/2 - w/2
        y = screenSize[1]*2/10 - h/2
        screen.blit(text_surface,(x,y))

        myFont = pygame.font.SysFont("arial",64)
        text_surface = myFont.render("Avoid cutting bombs.",True,(255,255,255))
        w,h = text_surface.get_size()
        x = screenSize[0]/2 - w/2
        y = screenSize[1]*3/10 - h/2
        screen.blit(text_surface,(x,y))

        myFont = pygame.font.SysFont("arial",64)
        text_surface = myFont.render("Bomb will eliminate Combo and score will -10."\
                                     ,True,(255,255,255))
        w,h = text_surface.get_size()
        x = screenSize[0]/2 - w/2
        y = screenSize[1]*4/10 - h/2
        screen.blit(text_surface,(x,y))

        myFont = pygame.font.SysFont("arial",64)
        text_surface = myFont.render("When the Combos get larger, the speed increases."\
                                     ,True,(255,255,255))
        w,h = text_surface.get_size()
        x = screenSize[0]/2 - w/2
        y = screenSize[1]*5/10 - h/2
        screen.blit(text_surface,(x,y))

        myFont = pygame.font.SysFont("arial",64)
        text_surface = myFont.render("Use red gloves to play openCV mode."\
                                     ,True,(255,255,255))
        w,h = text_surface.get_size()
        x = screenSize[0]/2 - w/2
        y = screenSize[1]*6/10 - h/2
        screen.blit(text_surface,(x,y))        

    #quitGame
        data.quitGame.innerW, data.quitGame.innerH= \
            pygame.transform.rotate(data.quitGame.innerImage,data.quitGame.innerAngle).get_size()
        data.quitGame.innerX = data.quitGame.fixXdojo - data.quitGame.innerW/2
        data.quitGame.innerY = data.quitGame.fixYdojo - data.quitGame.innerH/2
        screen.blit(pygame.transform.rotate(data.quitGame.innerImage,data.quitGame.innerAngle), \
                    (data.quitGame.innerX, data.quitGame.innerY))

        data.quitGame.outterW, data.quitGame.outterH= \
            pygame.transform.rotate(data.quitGame.outterImage,data.quitGame.outterAngle).get_size()
        data.quitGame.outterX = data.quitGame.fixXdojo - data.quitGame.outterW/2
        data.quitGame.outterY = data.quitGame.fixYdojo - data.quitGame.outterH/2
        screen.blit(pygame.transform.rotate(data.quitGame.outterImage,data.quitGame.outterAngle), \
                    (data.quitGame.outterX, data.quitGame.outterY))
        
    #cursor
    for i in range(len(data.knifePoints)-1):
        x1 = data.knifePoints[i][0]
        y1 = data.knifePoints[i][1]
        x2 = data.knifePoints[i+1][0]
        y2 = data.knifePoints[i+1][1]
        pygame.draw.line(screen, (255, 255, 255),(x1,y1), (x2,y2), 5)        


    pygame.display.update()

    

# The main loop
while running:
    time = clock.tick(60) #similar to timerDelay

    data.speed = 1 + data.comboCount * 0.08
    data.bombPosibility = 10 + data.comboCount*5

    if(data.mode == "menu"):
        data.rotateAngle += 1

        #newGame
        data.newGame.innerAngle += 1
        if(data.newGame.innerAngle == 360):
            data.newGame.innerAngle = 0
        data.newGame.outterAngle -= 1
        if(data.newGame.outterAngle == 0):
            data.newGame.outterAngle = 360

        #dojo
        data.dojo.innerAngle += 1
        if(data.dojo.innerAngle == 360):
            data.dojo.innerAngle = 0
        data.dojo.outterAngle -= 1
        if(data.dojo.outterAngle == 0):
            data.dojo.outterAngle = 360
            
            
        #quitGame
        data.quitGame.innerAngle += 1
        if(data.quitGame.innerAngle == 360):
            data.quitGame.innerAngle = 0
        data.quitGame.outterAngle -= 1
        if(data.quitGame.outterAngle == 0):
            data.quitGame.outterAngle = 360


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                data.x, data.y = event.pos
                #newGame
                dx = data.x - data.newGame.fixX
                dy = data.y - data.newGame.fixY
                dr = math.sqrt(dx**2+dy**2)
                if(dr < data.newGame.r):
                    data.mode = data.modes[1]
                    pygame.mixer.Sound.play(startSound)

                dx = data.x - data.quitGame.fixX
                dy = data.y - data.quitGame.fixY
                dr = math.sqrt(dx**2+dy**2)
                if(dr < data.quitGame.r):
                    running = False

                dx = data.x - data.dojo.fixX
                dy = data.y - data.dojo.fixY
                dr = math.sqrt(dx**2+dy**2)
                if(dr < data.dojo.r):
                    data.mode = "dojo"
                    pygame.mixer.Sound.stop(menuSound)

                dx = data.x - data.openCVlogo.fixX
                dy = data.y - data.openCVlogo.fixY
                if(abs(dx)<data.openCVlogo.w/2 and abs(dy) < data.openCVlogo.h/2):
                    data.mode = "openCV"
                    pygame.mixer.Sound.stop(menuSound)
                    pygame.mixer.Sound.play(startSound)
                
        if(len(data.knifePoints) < data.knifePointsNumber):
            data.knifePoints.append((data.x, data.y))
        else:
            data.knifePoints.append((data.x, data.y))
            data.knifePoints.pop(0) 




    if(data.mode == "openCV"):
        menuSound.stop()

        data.videoCnt += 1
        
        if(data.videoCnt >= 3):
            data.videoCnt = 0
            data.ret,data.frame_origin = cap.read()    
            data.frame=cv2.resize(data.frame_origin,\
                                  (data.ysize,data.xsize),interpolation=cv2.INTER_CUBIC)
            red = data.frame[:,:,2]
            green = data.frame[:,:,1]
            blue = data.frame[:,:,0]
            

            retval1, threshold1=cv2.threshold(red, 90, 255, cv2.THRESH_BINARY)
            retval2, threshold2=cv2.threshold(green, 50, 255, cv2.THRESH_BINARY)
            retval3, threshold3=cv2.threshold(blue, 50, 255, cv2.THRESH_BINARY)

            t1 = numpy.subtract(threshold1,threshold2)
            t1 = numpy.subtract(t1,threshold3)
            retval1, threshold1 = cv2.threshold(t1, 254,255, cv2.THRESH_BINARY)
            t1 = cv2.GaussianBlur(t1, (5,5), 0)


            number = numpy.sum(t1)/255
            if(number != 0):
                x1 = numpy.multiply(t1,data.xPosArray)
                X = int(numpy.sum(x1)/(number)/255)
                y1 = numpy.multiply(t1,data.yPosArray)
                Y = int(numpy.sum(y1)/(number)/255)
                data.hand1PosX = screenSize[0]*(1-X/data.ysize)
                data.hand1PosY = screenSize[1]*Y/data.xsize
                
#            cv2.imshow('threshold1',t1)
#            testPicture = numpy.zeros((xsize,ysize))       
#            testPicture[Y][X] = 255
#            cv2.imshow('testPicture',testPicture)
#            cv2.imshow('red',red)
            cv2.imshow('frame-origin',data.frame_origin)            
        

        
        data.quitGame.innerAngle += 1
        if(data.quitGame.innerAngle == 360):
            data.quitGame.innerAngle = 0
        data.quitGame.outterAngle -= 1
        if(data.quitGame.outterAngle == 0):
            data.quitGame.outterAngle = 360


        if(data.cutFruitFlag == True):
            data.cutFruitConnectTimeLeft -= 1
            if(data.cutFruitConnectTimeLeft <= 0):
                data.cutFruitFlag = False
                if(data.cutFruitCount >= 3):
                    data.comboFlag = True
                    data.comboTimeLeft = 300
                    if(data.comboCount < 6):
                        data.comboCount += 1
                    data.score += data.comboCount*5
                    data.showComboFlag = True
                    data.showComboTimeLeft = 90
                    #print("combo!  ",data.cutFruitCount)
                data.cutFruitCount = 0


        if(data.comboFlag == True):
            data.comboTimeLeft -= 1
            if(data.comboTimeLeft <= 0):
                initCombo(data)
                #print("combo not anymore")

                
        
        data.rotateAngle += 1
        data.count += 1
        data.timeCount += 1
        if(data.timeCount == 60):
            data.timeCount = 0
            data.timeLeft -= 1
        if(data.timeLeft < 0 ):
            data.mode = "openCVGameOver"
            pygame.mixer.Sound.play(overSound)

            
        for i in range(len(data.fruits)):
            data.fruits[i].x += data.fruits[i].vx
            data.fruits[i].y += data.fruits[i].vy
            data.fruits[i].vy += data.fruits[i].g
            data.fruits[i].rotateAngle += 2

        for i in range(len(data.bombs)):
            data.bombs[i].x += data.bombs[i].vx
            data.bombs[i].y += data.bombs[i].vy
            data.bombs[i].vy += data.bombs[i].g
            data.bombs[i].rotateAngle += 2

        outFruitNumber = []
        for i in range(len(data.fruits)):
            x = data.fruits[i].x
            y = data.fruits[i].y
            width = screenSize[0]
            height = screenSize[1]
            if(x<0 or x>width or y<0 or y>height or data.fruits[i].isOut):
                #data.fruits.pop(i)
                outFruitNumber.append(i)
        tempCount = 0
        for i in outFruitNumber:
            data.fruits.pop(i-tempCount)
            tempCount += 1

        outBombNumber = []
        for i in range(len(data.bombs)):
            x = data.bombs[i].x
            y = data.bombs[i].y
            width = screenSize[0]
            height = screenSize[1]
            if(x<0 or x>width or y<0 or y>height):
                data.bombs[i].isOut = True
            if(data.bombs[i].isOut):
                #data.fruits.pop(i)
                outBombNumber.append(i)
        tempCount = 0
        for i in outBombNumber:
            data.bombs.pop(i-tempCount)
            tempCount += 1

                
        if(data.count == 120):
            createLocation(data)
            createFruit(data)
        if(data.count == 124):
            createFruit(data)
        if(data.count == 128):
            createFruit(data)
        if(data.count == 132):
            createFruit(data)
        if(data.count == 136):
            createFruit(data)
            createBomb(data)
        if(data.count == 140):
            createFruit(data)
            createBomb(data)
            data.count = 0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                data.x, data.y = event.pos

                
        #cutFruit
        for i in data.fruits:
            if(i.isValid == True):
                dx = data.hand1PosX - i.x
                dy = data.hand1PosY - i.y
                dr = math.sqrt(dx**2 + dy**2)
                if(dr < i.r):
                    data.score += 1
                    i.rotateAngle = 0
                    i.isValid = False
                    i.g *= 2
                    i.vx*= 0.5
                    data.cutFruitFlag = True
                    data.cutFruitConnectTimeLeft = 10
                    data.cutFruitCount += 1
                    pygame.mixer.Sound.play(splatterSound)
        #cutBomb            
        for i in data.bombs:
            dx = data.hand1PosX - i.x
            dy = data.hand1PosY - i.y
            dr = math.sqrt(dx**2 + dy**2)
            if(dr < i.r):
                data.score -= 10
                initCombo(data)
                initCutFruit(data)
                if(data.score < 0):
                    data.score = 0
                i.rotateAngle = 0
                i.isOut = True
                i.g *= 2
                i.vx*= 0.5
                for i in data.fruits:
                    i.isOut = True
                pygame.mixer.Sound.play(boomSound)                    
        #quitGame
        dx = data.hand1PosX - data.quitGame.fixXdojo
        dy = data.hand1PosY - data.quitGame.fixYdojo
        dr = math.sqrt(dx**2+dy**2)
        if(dr < data.quitGame.r):
            init(data)
                        
                
        if(len(data.knifePoints) < data.knifePointsNumber):
            data.knifePoints.append((data.hand1PosX, data.hand1PosY))
        else:
            
            data.knifePoints.append((data.hand1PosX, data.hand1PosY))
            data.knifePoints.pop(0)





            

    if(data.mode == "newGame"):
        menuSound.stop()
        data.quitGame.innerAngle += 1
        if(data.quitGame.innerAngle == 360):
            data.quitGame.innerAngle = 0
        data.quitGame.outterAngle -= 1
        if(data.quitGame.outterAngle == 0):
            data.quitGame.outterAngle = 360


        if(data.cutFruitFlag == True):
            data.cutFruitConnectTimeLeft -= 1
            if(data.cutFruitConnectTimeLeft <= 0):
                data.cutFruitFlag = False
                if(data.cutFruitCount >= 3):
                    data.comboFlag = True
                    data.comboTimeLeft = 300
                    if(data.comboCount < 6):
                        data.comboCount += 1
                    data.score += data.comboCount*5
                    data.showComboFlag = True
                    data.showComboTimeLeft = 90
                    #print("combo!  ",data.cutFruitCount)
                data.cutFruitCount = 0


        if(data.comboFlag == True):
            data.comboTimeLeft -= 1
            if(data.comboTimeLeft <= 0):
                initCombo(data)
                #print("combo not anymore")

                
        
        data.rotateAngle += 1
        data.count += 1
        data.timeCount += 1
        if(data.timeCount == 60):
            data.timeCount = 0
            data.timeLeft -= 1
        if(data.timeLeft < 0 ):
            data.mode = "newGameGameOver"
            pygame.mixer.Sound.play(overSound)

            
        for i in range(len(data.fruits)):
            data.fruits[i].x += data.fruits[i].vx
            data.fruits[i].y += data.fruits[i].vy
            data.fruits[i].vy += data.fruits[i].g
            data.fruits[i].rotateAngle += 2

        for i in range(len(data.bombs)):
            data.bombs[i].x += data.bombs[i].vx
            data.bombs[i].y += data.bombs[i].vy
            data.bombs[i].vy += data.bombs[i].g
            data.bombs[i].rotateAngle += 2

        outFruitNumber = []
        for i in range(len(data.fruits)):
            x = data.fruits[i].x
            y = data.fruits[i].y
            width = screenSize[0]
            height = screenSize[1]
            if(x<0 or x>width or y<0 or y>height or data.fruits[i].isOut):
                #data.fruits.pop(i)
                outFruitNumber.append(i)
        tempCount = 0
        for i in outFruitNumber:
            data.fruits.pop(i-tempCount)
            tempCount += 1

        outBombNumber = []
        for i in range(len(data.bombs)):
            x = data.bombs[i].x
            y = data.bombs[i].y
            width = screenSize[0]
            height = screenSize[1]
            if(x<0 or x>width or y<0 or y>height):
                data.bombs[i].isOut = True
            if(data.bombs[i].isOut):
                #data.fruits.pop(i)
                outBombNumber.append(i)
        tempCount = 0
        for i in outBombNumber:
            data.bombs.pop(i-tempCount)
            tempCount += 1

                
        if(data.count == 120):
            createLocation(data)
            createFruit(data)
        if(data.count == 124):
            createFruit(data)
        if(data.count == 128):
            createFruit(data)
        if(data.count == 132):
            createFruit(data)
        if(data.count == 136):
            createFruit(data)
            createBomb(data)
        if(data.count == 140):
            createFruit(data)
            createBomb(data)
            data.count = 0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                data.x, data.y = event.pos
                #cutFruit
                for i in data.fruits:
                    if(i.isValid == True):
                        dx = data.x - i.x
                        dy = data.y - i.y
                        dr = math.sqrt(dx**2 + dy**2)
                        if(dr < i.r):
                            data.score += 1
                            i.rotateAngle = 0
                            i.isValid = False
                            i.g *= 2
                            i.vx*= 0.5
                            data.cutFruitFlag = True
                            data.cutFruitConnectTimeLeft = 10
                            data.cutFruitCount += 1
                            pygame.mixer.Sound.play(splatterSound)
                #cutBomb            
                for i in data.bombs:
                    dx = data.x - i.x
                    dy = data.y - i.y
                    dr = math.sqrt(dx**2 + dy**2)
                    if(dr < i.r):
                        data.score -= 10
                        initCombo(data)
                        initCutFruit(data)
                        if(data.score < 0):
                            data.score = 0
                        i.rotateAngle = 0
                        i.isOut = True
                        i.g *= 2
                        i.vx*= 0.5
                        for i in data.fruits:
                            i.isOut = True
                        pygame.mixer.Sound.play(boomSound)                    
                #quitGame
                dx = data.x - data.quitGame.fixXdojo
                dy = data.y - data.quitGame.fixYdojo
                dr = math.sqrt(dx**2+dy**2)
                if(dr < data.quitGame.r):
                    init(data)
                        
                
        if(len(data.knifePoints) < data.knifePointsNumber):
            data.knifePoints.append((data.x, data.y))
        else:
            
            data.knifePoints.append((data.x, data.y))
            data.knifePoints.pop(0)


            
    if(data.mode == "newGameGameOver"):
        
        data.newGame.innerAngle += 1
        if(data.newGame.innerAngle == 360):
            data.newGame.innerAngle = 0
        data.newGame.outterAngle -= 1
        if(data.newGame.outterAngle == 0):
            data.newGame.outterAngle = 360

        data.quitGame.innerAngle += 1
        if(data.quitGame.innerAngle == 360):
            data.quitGame.innerAngle = 0
        data.quitGame.outterAngle -= 1
        if(data.quitGame.outterAngle == 0):
            data.quitGame.outterAngle = 360



        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                data.x, data.y = event.pos
                dx = data.x - data.newGame.fixX1
                dy = data.y - data.newGame.fixY1
                dr = math.sqrt(dx**2+dy**2)
                if(dr < data.newGame.r):
                    init(data)
                    data.mode = "newGame"
                    pygame.mixer.Sound.play(startSound)

                dx = data.x - data.quitGame.fixX1
                dy = data.y - data.quitGame.fixY1
                dr = math.sqrt(dx**2+dy**2)
                if(dr < data.quitGame.r):
                    init(data)

                
        if(len(data.knifePoints) < data.knifePointsNumber):
            data.knifePoints.append((data.x, data.y))
        else:
            data.knifePoints.append((data.x, data.y))
            data.knifePoints.pop(0)

    if(data.mode == "openCVGameOver"):

        data.videoCnt += 1
        
        if(data.videoCnt >= 3):
            data.videoCnt = 0
            data.ret,data.frame_origin = cap.read()    
            data.frame=cv2.resize(data.frame_origin,\
                                  (data.ysize,data.xsize),interpolation=cv2.INTER_CUBIC)
            red = data.frame[:,:,2]
            green = data.frame[:,:,1]
            blue = data.frame[:,:,0]
            

            retval1, threshold1=cv2.threshold(red, 90, 255, cv2.THRESH_BINARY)
            retval2, threshold2=cv2.threshold(green, 50, 255, cv2.THRESH_BINARY)
            retval3, threshold3=cv2.threshold(blue, 50, 255, cv2.THRESH_BINARY)

            t1 = numpy.subtract(threshold1,threshold2)
            t1 = numpy.subtract(t1,threshold3)
            retval1, threshold1 = cv2.threshold(t1, 254,255, cv2.THRESH_BINARY)
            t1 = cv2.GaussianBlur(t1, (5,5), 0)


            number = numpy.sum(t1)/255
            if(number != 0):
                x1 = numpy.multiply(t1,data.xPosArray)
                X = int(numpy.sum(x1)/(number)/255)
                y1 = numpy.multiply(t1,data.yPosArray)
                Y = int(numpy.sum(y1)/(number)/255)
                data.hand1PosX = screenSize[0]*(1-X/data.ysize)
                data.hand1PosY = screenSize[1]*Y/data.xsize
                
#            cv2.imshow('threshold1',t1)
#            testPicture = numpy.zeros((xsize,ysize))       
#            testPicture[Y][X] = 255
#            cv2.imshow('testPicture',testPicture)
#            cv2.imshow('red',red)
            cv2.imshow('frame-origin',data.frame_origin)                

        data.quitGame.innerAngle += 1
        if(data.quitGame.innerAngle == 360):
            data.quitGame.innerAngle = 0
        data.quitGame.outterAngle -= 1
        if(data.quitGame.outterAngle == 0):
            data.quitGame.outterAngle = 360


        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                data.x, data.y = event.pos

        dx = data.hand1PosX - screenSize[0]/2
        dy = data.hand1PosY - screenSize[1]/2
        dr = math.sqrt(dx**2+dy**2)
        if(dr < data.quitGame.r):
            init(data)

                
        if(len(data.knifePoints) < data.knifePointsNumber):
            data.knifePoints.append((data.hand1PosX, data.hand1PosY))
        else:
            data.knifePoints.append((data.hand1PosX, data.hand1PosY))
            data.knifePoints.pop(0)

            

    if(data.mode == "dojo"):
        
        data.quitGame.innerAngle += 1
        if(data.quitGame.innerAngle == 360):
            data.quitGame.innerAngle = 0
        data.quitGame.outterAngle -= 1
        if(data.quitGame.outterAngle == 0):
            data.quitGame.outterAngle = 360

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                data.x, data.y = event.pos

                dx = data.x - data.quitGame.fixXdojo
                dy = data.y - data.quitGame.fixYdojo
                dr = math.sqrt(dx**2+dy**2)
                if(dr < data.quitGame.r):
                    init(data)

        if(len(data.knifePoints) < data.knifePointsNumber):
            data.knifePoints.append((data.x, data.y))
        else:
            data.knifePoints.append((data.x, data.y))
            data.knifePoints.pop(0)

        
    reDrawAll()
    
    

    
pygame.quit()

