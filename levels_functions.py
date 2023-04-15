from Objects import *

def run_first_level():
    game = Game()
    game.start_game()
    game.create_screen()
    game.load_background("images/background.png", "sounds/music_mario.mp3")
    game.load_title_and_icon("Mario Invaders -> World 1")
    player = Player(pygame.image.load("images/mario_128.png"),370,460,0)
    game.load_player(player )
    list_enemies = Enemies(12)
    list_enemies.fill_list("images/CloudTurtle.png",2.5)
    game.load_enemies(list_enemies)
    bullet = Bullet(pygame.image.load("images/star.png"),0,480,0,14)
    player.add_bullet(bullet)
    score = Score(0, pygame.font.Font("freesansbold.ttf",32),10,10)
    game.load_score(score)
    game.load_over_font()
    game.game_loop(2.5)
    if game.level_pass ==1:
        return True
    else:
        return False



def run_second_level():
    game = Game()
    game.start_game()
    game.create_screen()
    game.load_background("images/desert_background.png", "sounds/Desert.mp3")
    game.load_title_and_icon("Mario Invaders -> World 2")
    player = Player(pygame.image.load("images/mario fire.png"), 370,470, 0)
    game.load_player(player)
    list_enemies = Enemies(14)
    list_enemies.fill_list("images/Goomba.png",0.8)
    game.load_enemies(list_enemies)
    bullet = Bullet(pygame.image.load("images/fire.png"), 0 ,470, 0, 14)
    player.add_bullet(bullet)
    score = Score(0, pygame.font.Font("freesansbold.ttf", 32), 10, 10)
    game.load_score(score)
    game.load_over_font()
    game.game_loop(0.7,0.8)
    if game.level_pass ==1:
        return True
    else:
        return False
def run_third_level():
    game = Game()
    game.start_game()
    game.create_screen()
    game.load_background("images/BowserBackground.png", "sounds/BowserMusic.mp3")
    game.load_title_and_icon("Mario Invaders -> Final World")
    player = Player(pygame.image.load("images/MarioFinalWorld.png"), 370,470, 0)
    game.load_player(player)
    list_enemies = Enemies(16)
    list_enemies.fill_list("images/BowserJunior.png",1.6)
    game.load_enemies(list_enemies)
    bullet = Bullet(pygame.image.load("images/eggYoshi.png"), 0 ,470, 0,12)
    player.add_bullet(bullet)
    score = Score(0, pygame.font.Font("freesansbold.ttf", 32), 10, 10)
    game.load_score(score)
    game.load_over_font()
    game.game_loop(1.6,3,True)





