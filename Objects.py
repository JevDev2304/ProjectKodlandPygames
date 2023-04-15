import pygame
import random
import math
from pygame import mixer
import time
class Bullet:
    def __init__(self,img,x,y,x_change,y_change,state="ready"):
        self.img =img
        self.x = x
        self.y = y
        self.x_change = x_change
        self.y_change = y_change
        self.state = state
class Score:
    def __init__(self,value,font,x,y):
        self.value = value
        self.font = font
        self.x = x
        self.y= y

class Enemy:
    def __init__(self,Img,X,Y,X_change,Y_change):
        self.Img= Img
        self.x= X
        self.y = Y
        self.x_change = X_change
        self.y_change = Y_change
        self.colisionEnemy = False

class Player:
    def __init__(self,Img,X,Y,X_change):
        self.Img = Img
        self.x = X
        self.y = Y
        self.x_change = X_change
        self.bullet=None
    def add_bullet(self,bullet : Bullet):
        self.bullet= bullet


class Enemies:
    def __init__(self,num):
        self.Num = num
        self.List = []
    def fill_list(self,img,cambio_x=2):
        for enemy in range(0,self.Num):
            self.List.append(Enemy(pygame.image.load(img),random.randint(0, 11)*64,random.randint(1,3)*64,cambio_x,40))





class Game:
    def __init__(self):
        self.Player = None
        self.Enemies = None
        self.screen = None
        self.background = None
        self.icon = None
        self.over_font= None
        self.score = None
        self.level_pass =False
    def start_game(self):
        pygame.init()
    def create_screen(self):
        self.screen= pygame.display.set_mode((800, 600))
    def load_background(self,image,sound):
        self.background = pygame.image.load(image)
        mixer.music.load(sound)
        mixer.music.set_volume(0.6)
        mixer.music.play(-1)
    def load_title_and_icon(self,Title):
        pygame.display.set_caption(Title)
        self.icon = pygame.image.load("images/marioIcon.png")
        pygame.display.set_icon(self.icon)
    def load_over_font(self):
        self.over_font = pygame.font.Font("freesansbold.ttf", 64)
    def load_player(self,player):
        self.player = player
    def load_enemies(self,enemies):
        self.Enemies= enemies
    def load_score(self,score):
        self.score =score
    def show_player(self,player):
        self.screen.blit(player.Img, (player.x, player.y))
    def show_enemy(self,enemy:Enemy):
         self.screen.blit(enemy.Img, (enemy.x, enemy.y))

    def is_colission(self,enemy : Enemy, bullet : Bullet):
        distance = math.sqrt((math.pow(enemy.x - bullet.x, 2)) + (math.pow((enemy.y - bullet.y), 2)))
        if distance < 27:
            return True
        else:
            return False
    def fire_bullet(self):
            self.player.bullet.state = "fire"
            self.screen.blit(self.player.bullet.img, (self.player.bullet.x + 32, self.player.bullet.y + 20))
    def show_score(self):
        self.screen.blit(self.score.font.render("Score : "+ str(self.score.value),True, (255,255,255)),(self.score.x,self.score.y))

    def game_over_text(self,x, y):
        over_text = self.over_font.render("GAME OVER", True, (255, 255, 255))
        self.screen.blit(over_text, (x, y))
    def win_text(self,x,y):
        win_text = self.over_font.render("YOU WIN ", True, (255, 255, 255))
        self.screen.blit(win_text, (x, y))

    def game_loop(self,enemy_xchange=2,player_xchange=5, fin=False):
        running = True
        while running:
            # RGB - Red, Green, Blue
            self.screen.fill((0, 0, 0))
            # Background Image
            self.screen.blit(self.background, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                # if keastroke is pressed check wheter its right or left
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player.x_change= -player_xchange
                    if event.key == pygame.K_RIGHT:
                        self.player.x_change = player_xchange
                    if event.key == pygame.K_SPACE:
                        if self.player.bullet.state == "ready":
                            bullet_Sound = mixer.Sound("sounds/mario-coin.mp3")
                            bullet_Sound.play()
                            self.player.bullet.x = self.player.x
                            self.fire_bullet()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        print("Keystoke has been released")
                        self.player.x_change = 0

            # Checking for boundaries of spaceship so it doesn't go out of bounds
            # Player movements
            self.player.x += self.player.x_change
            if self.player.x <= 64:
                self.player.x= 64
            elif self.player.x>= 704:
                self.player.x = 704
            # Enemy movements

            for enemy in self.Enemies.List:
                if  self.score.value > 99:
                    self.win_text(250, 250)
                    self.level_pass = True

                    if fin == True:
                        game_win_sound = mixer.Sound("sounds/WinMario.mp3")
                        game_win_sound.set_volume(0.5)
                        game_win_sound.play()
                    running = False
                    break
                # Game Over
                if enemy.y > 400 :
                    for j in range(len(self.Enemies.List)):
                        self.Enemies.List[j].y = 4000
                    self.game_over_text(200, 250)
                    game_over_sound = mixer.Sound("sounds/game_over.mp3")
                    game_over_sound.set_volume(0.5)
                    game_over_sound.play()
                    break



                enemy.x += enemy.x_change
                if enemy.x <= 0:
                    enemy.x_change = enemy_xchange
                    enemy.y += enemy.y_change
                elif enemy.x >= 705:
                    enemy.x_change = -enemy_xchange
                    enemy.y += enemy.y_change
                # Colision
                colision = self.is_colission(enemy, self.player.bullet)

                self.show_enemy(enemy)



                if colision:
                    explosion_sound = mixer.Sound("sounds/mario-bros-1-up.mp3")
                    explosion_sound.set_volume(0.5)
                    explosion_sound.play()
                    self.player.bullet.y = 480
                    self.player.bullet.state = "ready"
                    self.score.value += 1
                    enemy.x = random.randint(0, 11)*64
                    enemy.y = random.randint(1, 3)*64


            # Bullet movement
            if self.player.bullet.y <= 0:
                self.player.bullet.y= 480
                self.player.bullet.state = "ready"
            if self.player.bullet.state == "fire":
                self.fire_bullet()
                self.player.bullet.y -= self.player.bullet.y_change
            self.show_player(self.player)
            self.show_score()

            pygame.display.update()

        pygame.time.wait(3000)
        pygame.quit()




