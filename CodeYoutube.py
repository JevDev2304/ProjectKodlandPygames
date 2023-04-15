import pygame
import math
import random
from pygame import mixer
#Inicialize the pygame

pygame.init()


#Create the screen
screen = pygame.display.set_mode((800,600))
#Background
background = pygame.image.load("images/background.png")
#Background Sound
mixer.music.load("sounds/background.wav")
mixer.music.set_volume(0.2)
mixer.music.play(-1)

#Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("images/ufo.png")
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load("images/player.png")
playerX = 370
playerY = 480
playerX_change = 0

#Enemies
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
colisionEnemies= False
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("images/enemy.png"))
    enemyX.append(random.randint(0,730))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(2)
    enemyY_change.append(40)

#Bullet
# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving

bulletImg = pygame.image.load("images/bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 7
bullet_state = "ready"

#Score
score_value=0
font = pygame.font.Font("freesansbold.ttf",32)
textX = 10
testY = 10
#Game over text
over_font = pygame.font.Font("freesansbold.ttf",64)



def player(x,y):
    screen.blit(playerImg,(x,y))





def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x+16,y+10))

def isColission(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2))+(math.pow((enemyY-bulletY),2)))
    if distance < 27:
        return True
    else:
        return False
def show_score(x,y):
    score = font.render("Score : "+ str(score_value),True, (255,255,255))
    screen.blit(score,(x,y))

def game_over_text(x,y):
    over_text = over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(over_text, (x, y))
#Game Loop
running = True
while running:
    # RGB - Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #if keastroke is pressed check wheter its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_Sound = mixer.Sound("sounds/laser.wav")
                    bullet_Sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)
                    print("Holaa")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Keystoke has been released")
                playerX_change = 0



    # Checking for boundaries of spaceship so it doesn't go out of bounds
    #Player movements
    playerX += playerX_change
    if playerX <= 10:
        playerX = 10
    elif playerX >= 730:
        playerX = 730
    #Enemy movements
    for i in range(num_of_enemies):
        #Game Over
        if enemyY[i] > 400:
            for j in range (num_of_enemies):
                enemyY[j]= 4000
            game_over_text(200, 250)
            break
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 10:
            enemyX_change[i] = 2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 730:
            enemyX_change[i] = -2
            enemyY[i] += enemyY_change[i]
        # Colision
        colision = isColission(enemyX[i], enemyY[i], bulletX, bulletY)
        if i > 0:
            colisionEnemies = isColission(enemyX[i], enemyY[i], enemyX[i-1], enemyY[i-1])
        if colision:
            explosion_sound= mixer.Sound("sounds/explosion.wav")
            explosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 730)
            enemyY[i] = random.randint(50, 150)
        if colisionEnemies:
            enemyX[i] = random.randint(0, 730)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i],i)

    #Bullet movement
    if bulletY <= 0 :
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -=bulletY_change


    player(playerX,playerY)
    show_score(textX,testY)
    pygame.display.update()