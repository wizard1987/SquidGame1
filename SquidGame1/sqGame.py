import pygame, sys, random
from random import randrange


pygame.init()
screen = pygame.display.set_mode((1024,768))
clock = pygame.time.Clock()
game_font = pygame.font.Font('04B_19.ttf',40)
small_font = pygame.font.Font('04B_19.ttf',10)

bg_surface = pygame.image.load('bk5.png').convert()
bird_movement = 0.0
man_status = 0 # 0 stand 1 run
move_speed = 1.0
move_timer = 10

otherman_status = 0
score = 0

bird_run1 = pygame.image.load('man/man_1.png').convert_alpha()
bird_run2 = pygame.image.load('man/man_2.png').convert_alpha()
bird_run3 = pygame.image.load('man/man_3.png').convert_alpha()
bird_run4 = pygame.image.load('man/man_4.png').convert_alpha()
bird_run5 = pygame.image.load('man/man_5.png').convert_alpha()
bird_run6 = pygame.image.load('man/man_6.png').convert_alpha()
bird_run7 = pygame.image.load('man/man_7.png').convert_alpha()



pipe_surface1 = pygame.image.load('man/man_1.png').convert_alpha()
pipe_surface2 = pygame.image.load('man/man_2.png').convert_alpha()
pipe_surface3 = pygame.image.load('man/man_3.png').convert_alpha()
pipe_surface4 = pygame.image.load('man/man_4.png').convert_alpha()
pipe_surface5 = pygame.image.load('man/man_5.png').convert_alpha()
pipe_surface6 = pygame.image.load('man/man_6.png').convert_alpha()
pipe_surface7 = pygame.image.load('man/man_7.png').convert_alpha()
pipe_frames = [bird_run1,bird_run2,bird_run3,bird_run4,bird_run5,bird_run6,bird_run7]
pipe_index = 0
PIPEFLAP = pygame.USEREVENT + 4
pygame.time.set_timer(PIPEFLAP,20)


pipe_list = []

bigman_run0 = pygame.image.load('girl/girl_0.png').convert_alpha()
bigman_run1 = pygame.image.load('girl/girl_1.png').convert_alpha()
bigman_run2 = pygame.image.load('girl/girl_2.png').convert_alpha()
bigman_run3 = pygame.image.load('girl/girl_3.png').convert_alpha()
bigman_run4 = pygame.image.load('girl/girl_4.png').convert_alpha()
bigman_run5 = pygame.image.load('girl/girl_5.png').convert_alpha()
bigman_run6 = pygame.image.load('girl/girl_6.png').convert_alpha()



bird_frames = [bird_run1,bird_run2,bird_run3,bird_run4,bird_run5,bird_run6,bird_run7]
bird_index = 0
bird_surface = bird_frames[0]
bird_rect = bird_surface.get_rect(center = (100,700))
BIRDFLAP = pygame.USEREVENT + 1
pos_x = 100
pos_y = 700
pygame.time.set_timer(BIRDFLAP,20)
light_status = 0


bigman_frames = [bigman_run6,bigman_run5,bigman_run4,bigman_run3,bigman_run2,
bigman_run1,bigman_run0,bigman_run0,bigman_run0,bigman_run1,
bigman_run2,bigman_run3,bigman_run4,bigman_run5,bigman_run6]
bigman_index = 0
bigman_surface = bigman_frames[0]
bigman_rect = bigman_surface.get_rect(center = (850,100))
BIGMANFLAP = pygame.USEREVENT + 2
pygame.time.set_timer(BIGMANFLAP,200)

gameover_status = 0

score_sound_countdown = 100

def bigman_animation():
	new_bird = bigman_frames[bigman_index]
	new_bird_rect = new_bird.get_rect(center = (bigman_rect.centerx,bigman_rect.centery))
	return new_bird,new_bird_rect

def bird_animation():
	new_bird = bird_frames[bird_index]
	new_bird_rect = new_bird.get_rect(center = (bird_rect.centerx,bird_rect.centery))
	return new_bird,new_bird_rect

def pipe_animation():
	new_pipe = pipe_frames[pipe_index]
	return new_pipe

def pipe_stand():
	new_pipe = pipe_frames[0]
	return new_pipe

def bird_stand():
	new_bird = bird_frames[0]
	new_bird_rect = new_bird.get_rect(center = (bird_rect.centerx,bird_rect.centery))
	return new_bird,new_bird_rect


def redlight_display(game_state):
    if (light_status ==1):
        score_surface = game_font.render("RED LIGHT",True,(255,0,0))
    else:
        score_surface = game_font.render("GREEN LIGHT",True,(0,255,0)) 

    score_rect = score_surface.get_rect(center = (150,50))
    screen.blit(score_surface,score_rect)


def gameover_display(gameover_status):
    if (gameover_status ==1 ):
        gameover_surface = game_font.render("GAME OVER",True,(255,0,0))
        gameover_rect = gameover_surface.get_rect(center = (1024/2,768/2))
        screen.blit(gameover_surface,gameover_rect)

        gameover_surface = game_font.render("Press Space to restart",True,(255,0,0))
        gameover_rect = gameover_surface.get_rect(center = (1024/2,768/2+50))
        screen.blit(gameover_surface,gameover_rect)

    if (gameover_status ==2 ):
        gameover_surface = game_font.render("YOU WIN",True,(255,0,0))
        gameover_rect = gameover_surface.get_rect(center = (1024/2,768/2))
        screen.blit(gameover_surface,gameover_rect)

        gameover_surface = game_font.render("Press Space to restart",True,(255,0,0))
        gameover_rect = gameover_surface.get_rect(center = (1024/2,768/2+50))
        screen.blit(gameover_surface,gameover_rect)





def move_pipes(pipes):
    for pipe in pipes:
        if otherman_status ==1 :
            pipe.centerx += 2
            pipe.centery -= 1

        if pipe.centery < -10:
            pipes.remove(pipe)
    return pipes
            


def create_pipe():
    if gameover_status ==0 :
        bottom_pipe = pipe_frames[0].get_rect(center = (randrange(1024)-600,800+randrange(500)))
        return bottom_pipe


flap_sound = pygame.mixer.Sound('coin.wav')
death_sound = pygame.mixer.Sound('bomb2.wav')
song_sound = pygame.mixer.Sound('song.wav')


SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,1200)


gameover_status =0 
pygame.display.set_caption('Squid Game')


while True:

    if ((bigman_index>=5) & (bigman_index<=10)):
        light_status = 1
        otherman_status = 0
    else :
        light_status = 0  
        otherman_status = 1 

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                man_status = 1
                flap_sound.play()
            if event.key == pygame.K_a:
                man_status = 0
                flap_sound.play()
            if (event.key == pygame.K_SPACE) &( gameover_status !=0 ):
                man_status = 0
                gameover_status = 0 
                pipe_list = [] 
                bird_rect.centerx = 100
                bird_rect.centery = 700
                pos_x = 100
                pos_y = 700



        elif event.type == SPAWNPIPE:
            if ((otherman_status == 1) & (gameover_status == 0)):
                for num in range(0,10): 
                    pipe_list.append(create_pipe())
                print("pile count = ",len(pipe_list))


        elif event.type == PIPEFLAP:
            if pipe_index < 6 :
                pipe_index = pipe_index + 1
            else:
                pipe_index = 0

            if otherman_status==1 :
                pipe_surface = pipe_animation()
            else:
                pipe_surface = pipe_stand()
            


        elif event.type == BIRDFLAP:
            if bird_index < 6 :
                bird_index = bird_index + 1
            else:
                bird_index = 0
            if man_status==1 :
                bird_surface,bird_rect = bird_animation()
            else:
                bird_surface,bird_rect = bird_stand()



        elif event.type == BIGMANFLAP:
            if gameover_status == 0 :
                if bigman_index < 14 :
                    bigman_index = bigman_index + 1
                else:
                    bigman_index = 0
                    song_sound.play()

            bigman_surface,bigman_rect = bigman_animation()



    if gameover_status == 0:

        screen.blit(bg_surface,(0,0))
        text_surface = game_font.render("Press (D) to Go, (A) Stop",True,(0,0,0))
        text_rect = text_surface.get_rect(center = (1024/2,768-50))
        screen.blit(text_surface,text_rect)


        screen.blit(bird_surface, bird_rect)


        screen.blit(bigman_surface, bigman_rect)
         # Pipes
        pipe_list = move_pipes(pipe_list)
        ##pipe_list = remove_pipes(pipe_list)

        for pipe in pipe_list:
            screen.blit(pipe_surface,pipe)

        if (man_status == 1):
            pos_x = pos_x + move_speed
            pos_y = pos_y - move_speed/2
            bird_rect.centerx = pos_x
            bird_rect.centery = pos_y

        if ((man_status ==1)and (light_status==1)) :
            gameover_status = 1
            death_sound.play()
            gameover_display(gameover_status)

        if (pos_y < 250):
            gameover_status = 2
            death_sound.play()
            gameover_display(gameover_status)

        redlight_display('main_game')
    else:
        gameover_display(gameover_status)


    pygame.display.update()
    clock.tick(120)
