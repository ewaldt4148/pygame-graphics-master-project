# Computer Programming 1
# Unit 11 - Graphics
#
# A candy game set up 


# Imports
import pygame
import random

# Initialize game engine
pygame.mixer.pre_init()
pygame.init()

# Images
candy = pygame.image.load('candy.jpg')
candy_cane = pygame.image.load('candy_cane.jpg')
mint = pygame.image.load('mint.png')
candy_piece = pygame.image.load('candy_piece.png')
tide = pygame.image.load('tide_pod.png')
basket = pygame.image.load('Basket.png')
bunny = pygame.image.load('bunny.png')
flower = pygame.image.load('flower.png')
flower_1 = pygame.image.load('flower_1.png')
flowers = [flower, flower_1]
falling_candy = [ mint, candy_piece, tide]
#Window
SIZE = (800, 600)
TITLE = "Candy Game"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)
pause = pygame.Surface([600, 800])
pause.fill([0, 0, 0])
# Timer
clock = pygame.time.Clock()
refresh_rate = 60

#Fonts
MY_FONT = pygame.font.Font(None, 50)
INST = pygame.font.Font(None, 25)
# Colors
GREEN = (0, 175, 0)
WHITE = (255, 255, 255)
BLUE = (75, 200, 255)
YELLOW = (255, 255, 175)
GRAY = (128,128,128)
SKY = (169,169,169)
GRASS = (51, 153, 51)
RAIN = (0, 255, 255)
PINK = (255, 4, 244)
BLACK = (0, 0, 0)

colors = [ PINK, YELLOW, BLUE, WHITE]
# Make clouds

def draw_cloud(loc, color):
    x = loc[0]
    y = loc[1]
    
    pygame.draw.ellipse(screen, color, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, color, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, color, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, color, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, color, [x + 20, y + 20, 60, 40])
    
num_clouds = 20
clouds = []
for i in range(num_clouds):
    x = random.randrange(0, 1600)
    y = random.randrange(-50, 200)
    loc = [x, y]
    clouds.append(loc)
far_clouds = []

for i in range(num_clouds):
    x = random.randrange(0, 1600)
    y = random.randrange(-50, 300)
    loc = [x, y]
    far_clouds.append(loc)
    
rain = []
for i in range(1000):
    x = random.randrange(-400, 800)
    y = random.randrange(0, 600)
    r = random.randrange(10, 11)
    s = [x, y, r, r]
    
    rain.append(s)

def rains(rain):
    pygame.draw.ellipse(screen, random.choice(colors), s)

def f_candy():
    screen.blit(mint, a)
def c_candy():
    screen.blit(candy_cane, a)
def z_candy():
    screen.blit(candy_piece, a)
def draw_bask(xpos):
    screen.blit(bunny, ( xpos, 350))
    screen.blit(basket, ( xpos, 400))
    
sweet = []
for i in range(20):
    x = random.randrange(-400, 800)
    y = random.randrange(-50, 800)
    c = random.choice(falling_candy)
    a = [x, y,c]
    
    sweet.append(a)
flower_timer = 0
frames = 0
ticks = 0

# Sound Effects
pygame.mixer.music.load("music.ogg")


sparkles = False
pa = False
mints = False
start = True
speed = 0
xpos = 250
# Game loop

pygame.mixer.music.play(-1)

done = False    

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                sparkles = not sparkles
            elif event.key == pygame.K_m:
                mints = not mints
            elif event.key == pygame.K_SPACE:
                start = not start
            elif event.key == pygame.K_LEFT :
                speed = -5
            elif event.key == pygame.K_RIGHT:
                speed = 5
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    speed = 0
            elif event.key == pygame.K_RETURN:
                pa = not pa

    # Game logic
    ticks += 1
    if ticks % 30 == 0:
        frames += 1
        if frames > 1:
            frames = 0 




             
    # Drawing code
    ''' sky '''
    screen.blit(candy, (0, 0))
    pause.set_alpha(100)
 


    ''' grass '''
    pygame.draw.rect(screen, GRASS, [0, 400, 800, 200])

    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, WHITE, [[x+5, y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]])
    pygame.draw.line(screen, WHITE, [0, 390], [800, 390], 5)
    pygame.draw.line(screen, WHITE, [0, 410], [800, 410], 5)  

    'flowers'
    y = 350
    for x in range(-100, 800, 100):
            screen.blit(flowers[frames], ( x, y))
   


    draw_bask(xpos)     
    if not pa:
        if(xpos + speed) <= 0:
            speed = 0
        elif(xpos + speed) >= 600:
            speed = 0 
        else:
            xpos += speed
        
    if pa:
        for c in far_clouds:
            draw_cloud(c, WHITE)
            c[0] += 0
    else:
        for c in far_clouds:
            draw_cloud(c, WHITE)
            c[0] -= 1

            if c[0] < -100:
                c[0] = random.randrange(800, 1600)
                c[1] = random.randrange(-50, 200)

    if sparkles:
        for s in rain:
            rains(rain)
            s[0] += random.randrange(-10,10)
            s[1] += 2
        
            if s[1] > 600 :
                s[0] = random.randrange(-500, 800)
                s[1] = random.randrange(-50, 0 )
    if mints:      
        for s in sweet:
            screen.blit(s[2], (s[0], s[1]))
            s[0] -= 0
            s[1] += 1
            

            if s[1] > 400 or s[0] < -50:
                s[1] = random.randrange(-600, 0)
                s[0] = random.randrange(-10, 900)

    if pa:
        for c in clouds:
            draw_cloud(c, PINK)
            c[0] += 0
    else:
        for c in clouds:
            draw_cloud(c, PINK)
            c[0] += 2

            if c[0] > 800:
               c[0] = random.randrange(-1600, -100)
               c[1] = random.randrange(-50, 200)

    '''start'''
    if start:
        pygame.draw.rect(screen, BLACK, [0, 0, 800, 600])
        header = MY_FONT.render('Welcome to Candy Catcher ', True, PINK)
        inst = INST.render('press the SPACE bar to continue ', True, WHITE)
        screen.blit(header, [170, 150])
        screen.blit(inst, [250, 300])

    if pa:
        screen.blit(pause, [0,0])


        
    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
