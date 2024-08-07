import pygame
import time
import random
import datetime
pygame.init()
pygame.mixer.init()

#game variables
w_width=500
w_height=500
window=pygame.display.set_mode((w_width,w_height))
pygame.display.set_caption("Drive0")
icon = pygame.image.load("img_assets/icon.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
font1 = pygame.font.SysFont("helvetica", 50, 1)
font2 = pygame.font.SysFont("helvetica", 50, 1)
font = pygame.font.SysFont("monocoque", 50, 1, 1)
font3 = pygame.font.SysFont(None, 30)
bg_speed=5
score=0
level=1
next_level=20
run=True


#images....
bg_img=pygame.transform.scale(pygame.image.load("img_assets/bg.jpg"),(500, 500))
car_img=pygame.image.load("img_assets/car1.png")
grass=pygame.image.load("img_assets/grass.jpg")
white_line=pygame.image.load("img_assets/white_line.jpg")
yellow_line=pygame.image.load("img_assets/yellow_line.jpg")
trees=pygame.image.load("img_assets/tree.png")
loser=pygame.transform.scale(pygame.image.load("img_assets/down.jpg"),(400,300))
win=pygame.transform.scale(pygame.image.load("img_assets/up.jpg"),(400,300))
ecar=[pygame.image.load("img_assets/car2.png"),pygame.image.load("img_assets/car3.png")]
#sounds
bg_music=pygame.mixer.Sound("sounds/bgm.mp3")
over_sound=pygame.mixer.Sound("sounds/go.mp3")
explo_sound=pygame.mixer.Sound("sounds/ex.mp3")
yay=pygame.mixer.Sound("sounds/yay.mp3")

#displaying text on the screen
def text_display(score, level, next_level):
    score_text=font2.render("Score: "+str(score), 1, "black")
    window.blit(score_text,(0,0))
    level_text=font1.render("Level: "+str(level), 1, "black")
    window.blit(level_text,(w_width-level_text.get_width(), 0))

# Button class
class Button():
    def __init__(self, x, y, width, height, text, action):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action

    def draw(self):
        pygame.draw.rect(window, "white", self.rect)
        pygame.draw.rect(window, "black", self.rect, 3)
        text_surface = font3.render(self.text, True, "black")
        text_rect = text_surface.get_rect(center=self.rect.center)
        window.blit(text_surface, text_rect)

    def perform_action(self):
        self.action()
#start game function
def startgame():
    #cars
    #yours
    class car():
        def __init__(self,x,y):
            self.x=x
            self.y=y
            self.width=26
            self.height=46
            self.vel=2
        def draw(self, window):
            window.blit(car_img, (self.x,self.y))

    maincar=car(250,250)
    #enemys's
    class enemy_car():
        def __init__(self,x,y,img):
            self.x=x
            self.y = y
            self.img = img
            self.width=26
            self.height=46
            self.vel=2
        
        def move(self):
            self.y+=self.vel

        def draw(self,window):
            window.blit(self.img, (self.x,self.y))

    #enemycar list
    enemycar=[]
    for i in range(3):
        x=random.randint(100,400-28)
        y=random.randint(-500, -50)
        img=random.choice(ecar)
        ec = enemy_car(x,y,img)
        enemycar.append(ec)

    #write score in file
    def writer(cscore):
        file=open("score.txt","a")
        now = datetime.datetime.now()
        formatted_time = now.strftime("%Y-%m-%d %H:%M:%S.%f")
        file.writelines(str(cscore)+" "+str(formatted_time)+'\n')
        file.close()
    #get high score
    def greatest():
        greatest=0
        file=open("score.txt","r")
        for line in file:
            js = line.strip().split(" ", 1)
            js=int(js[0])
            number = int(js)
            if number>greatest:
                greatest=number
        file.close()
        return greatest

    #drawing the background
    def drawing_background():
        bg_y=pygame.time.get_ticks()// bg_speed
        window.blit(grass, (0, bg_y % w_height - w_height))
        window.blit(grass, (420, bg_y % w_height - w_height))
        window.blit(white_line, (90, bg_y % w_height - w_height))
        window.blit(white_line, (405, bg_y % w_height - w_height))
        window.blit(yellow_line, (225, (bg_y+0)%w_height - w_height))
        window.blit(yellow_line, (225, (bg_y+100)%w_height - w_height))
        window.blit(yellow_line, (225, (bg_y+200)%w_height - w_height))
        window.blit(yellow_line, (225, (bg_y+300)%w_height - w_height))
        window.blit(yellow_line, (225, (bg_y+400)%w_height - w_height))

        window.blit(grass, (1, bg_y % w_height ))
        window.blit(grass, (420, bg_y % w_height ))
        window.blit(white_line, (90, bg_y % w_height ))
        window.blit(white_line, (405, bg_y % w_height ))
        window.blit(yellow_line, (225, (bg_y+0)%w_height ))
        window.blit(yellow_line, (225, (bg_y+100)%w_height ))
        window.blit(yellow_line, (225, (bg_y+200)%w_height ))
        window.blit(yellow_line, (225, (bg_y+300)%w_height ))
        window.blit(yellow_line, (225, (bg_y+400)%w_height ))
        
    #drawing on windos surface....
    def DrawInGameLoop():
        clock.tick(60)
        window.fill((136, 134, 134))#somewhat grey!
        drawing_background()
        maincar.draw(window)
        for obj in enemycar:
            obj.draw(window)
        text_display(score, level, next_level)
        pygame.display.flip()

    #crash logic
    def crash():
        global next_level,score,bg_speed
        pscore=score
        writer(pscore)
        next_level=50
        score=0
        level=1
        maincar.vel=2
        explo_sound.play()
        for i in range(len(blast)):
            window.blit(blast[i],(maincar.x-25,maincar.y-35))
            clock.tick(50)
            pygame.display.flip()
        
        time.sleep(2)
        hs=greatest()
        if hs > pscore:
            over_sound.play()
            text=font.render("you suck at this!!", 1, "white")
            text4=font.render(f'your: {pscore}  HighScore: {hs}', 1, "white")
            window.blit(loser,(50,100))
            window.blit(text4,(70, 300))
            window.blit(text,(100, 350))
        else:
            yay.play()
            text1=font.render('yay new highscore', 1, "white")
            text2=font.render(f'HighScore:{ pscore}', 1, "white")
            window.blit(win,(50,100))
            window.blit(text2,(100, 250))
            window.blit(text1,(100, 350))
        pygame.display.flip()
        time.sleep(5)
        maincar.x=250
        maincar.y=250
        menuloop()
    #create objects....
    blast=[pygame.transform.scale(pygame.image.load(f"crashed/{i}.png"),(70, 70)) for i in range(28)]
    def musicplay():
        bg_music.play(loops=-1)
    #game loop....
    musicplay()
    def gameloop():
        global run,next_level,score,bg_speed
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            #crash
            if maincar.x<70 or maincar.x > 430-maincar.width:
                bg_music.stop()
                crash()

            #levels
            if score >= next_level:
                next_level= next_level + 20
                if bg_speed > 1:
                    bg_speed-=1
                    maincar.vel+=1
                else:
                    bg_speed=1
            #key events...
            keys = pygame.key.get_pressed()

            if keys[pygame.K_a ] and maincar.x > 0:
                maincar.x -= maincar.vel

            elif keys[pygame.K_d] and maincar.x < w_width - maincar.width:
                maincar.x += maincar.vel

            if keys[pygame.K_w] and maincar.y > 0:
                maincar.y -= maincar.vel

            elif keys[pygame.K_s] and maincar.y < w_width - maincar.height:
                maincar.y += maincar.vel
            #enemy car
            for enec in enemycar:
                enec.move()
                        # check for collision with main car
                if (enec.x < maincar.x + maincar.width and
                    enec.x + enec.width > maincar.x and
                    enec.y < maincar.y + maincar.height and
                    enec.y + enec.height > maincar.y):
                    bg_music.stop()
                    crash()

                # if enemy car goes off the screen, reset its position
                if enec.y > w_height:
                    enec.x = random.randint(100, 400 - 28)
                    enec.y = random.randint(-500, -50)
                    enec.img = random.choice(ecar)
                    enec.vel = 2
                    score+=1
            DrawInGameLoop()
    gameloop()
    pygame.quit()

def quit_game():
    pygame.quit()
def menuloop():
    #buttons
    start_button = Button(200, 200, 100, 100, "Start", startgame)
    quit_button = Button(200, 320, 100, 100, "Quit", quit_game)

    #menu loop
    menu_running = True
    while menu_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if start_button.rect.collidepoint(mouse_pos):
                    start_button.perform_action()
                elif quit_button.rect.collidepoint(mouse_pos):
                    quit_button.perform_action()
        window.blit(bg_img,(0,0))
        start_button.draw()
        quit_button.draw()
        pygame.display.flip()
menuloop()
exit()