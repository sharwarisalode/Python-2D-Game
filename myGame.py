#importing libraris
import pygame
from sys import exit

#initalizing
pygame.init()

#making the display window
screen = pygame.display.set_mode((1000,600))

#set header for the game
pygame.display.set_caption("game")

#setting clock
clock=pygame.time.Clock()
#setting text font
text_font = pygame.font.Font('pob.ttf',50)

game_active = True

#importing images and texts
#background tile
background_surface = pygame.image.load('assets/Background/Yellow.png').convert()
#Ground
ground_surface = pygame.image.load('assets/ground.png').convert()
#text
text_surface = text_font.render('GAME',False,'Black')
#player
player_surface = pygame.image.load('assets/tile0000.png').convert_alpha()
player_rect=player_surface.get_rect(midbottom=(80,435))
player_scale = 5  # Adjust the scale factor
player_gravity = 0 #adding gravity
#ghost
enemy1_surface = pygame.image.load('assets/tile000.png').convert_alpha()
enemy1_rect =enemy1_surface.get_rect(midbottom=(800,440))
enemy1_scale = 4.5  # Adjust the scale factor
#game over text
game_over_font = pygame.font.Font('pob.ttf', 40)
game_over_text = game_over_font.render('Game Over', False, 'Red')
#replay text
replay_font = pygame.font.Font('pob.ttf', 25)
replay_text = replay_font.render('Replay', False, 'Blue')
#quit text
quit_text = replay_font.render('Quit', False, 'Blue')


#loop for running window
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 435:
                    player_gravity = -20
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if replay_rect.collidepoint(event.pos):
                    game_active = True
                    enemy1_rect.right = 500
                    player_rect = player_surface.get_rect(midbottom=(80, 435))
                if quit_rect.collidepoint(event.pos):
                    pygame.quit()
                    exit()
    if game_active:
        #fill the whole screeen with the tile
        for x in range(0, 1000, background_surface.get_width()):
            for y in range(0, 600, background_surface.get_height()):
                screen.blit(background_surface, (x, y))

        # Scale the image to the new dimensions
        scaled_ground_surface = pygame.transform.scale(ground_surface, (1000,200))
        screen.blit(scaled_ground_surface, (0, 500)) 

        #adding text in window
        screen.blit(text_surface,(450,50))

        #position the enemy and loop the movement:whenever enemy move out of window start again from the given position
        enemy1_rect.x -= 10
        if enemy1_rect.right <=0:
            enemy1_rect.left =1200 
        #scale and set the position of enemy1  
        scaled_enemy1_surface = pygame.transform.scale(enemy1_surface, (player_rect.width * enemy1_scale, enemy1_rect.height * player_scale))
        screen.blit(scaled_enemy1_surface, enemy1_rect)

    # Scale the player and update player position
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 435:
            player_rect.bottom = 435
        scaled_player_surface = pygame.transform.scale(player_surface, (player_rect.width * player_scale, player_rect.height * player_scale))
        screen.blit(scaled_player_surface, player_rect)

    #collision
        if player_rect.colliderect(enemy1_rect):
            game_active = False
    # game over window       
    else:
        screen.fill('Yellow')
        screen.blit(game_over_text, (380, 200))
        replay_rect = pygame.draw.rect(screen, 'yellow', (300, 300, 150, 50))
        quit_rect = pygame.draw.rect(screen, 'yellow', (500, 300, 150, 50))
        screen.blit(replay_text, (360, 305))
        screen.blit(quit_text, (520, 305))
    #updating screen
    pygame.display.update()        
    clock.tick(60)




