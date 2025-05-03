# Example file showing a circle moving on screen
import pygame


horizotal_speed = 0.2
dt = 0
x = 500
dy = -1
dx =  -1
radius = 40

def draw_text(screen, x, y, text_str):
    background = pygame.Surface((screen.get_width(), screen.get_height()))
    background.fill('purple')
    font = pygame.font.Font(None, 64)
    text = font.render(text_str, True, (128, 128, 128))
    textpos = text.get_rect(x=x, y=y)
    background.blit(text, textpos)
    screen.blit(background, (0, 0))

def update_player_pos(dy,ball_pos,dx):
    ball_pos.y += dy*10 
    ball_pos.x += dx*horizotal_speed*10   
    return ball_pos
    
    
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1000,1000))
clock = pygame.time.Clock()
running = True

ball_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
rectangle1_left = 400
rectangle2_left = 400
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    ball_pos = update_player_pos(dy,ball_pos,dx)
    pygame.draw.circle(screen, "red",ball_pos , radius)
    
    def is_hitting(rectangle,ball):
        center = rectangle.x + rectangle.width/2
        return abs(center - ball.x) <= 100
    
    
    rectangle1 = pygame.Rect(rectangle1_left,0, 200, 50)
    rectangle2 = pygame.Rect(rectangle2_left,950, 200, 50)
    
    if ball_pos.y == 50 and is_hitting(rectangle1, ball_pos):
        center = rectangle1.x + rectangle1.width/2
        dy = 1
        if ball_pos.x > center:
            dx = 1
        else:
            dx = -1
    if ball_pos.y == 950 and is_hitting(rectangle2, ball_pos):
        dy = -1
        center = rectangle2.x + rectangle2.width/2
        if ball_pos.x > center:
            dx=1
        else:
            dx = -1
    if ball_pos.x == 40:
        dx = 1
    if ball_pos.x == 960:
        dx = -1
    
    
   
    
    

    pygame.draw.rect(screen,'green', rectangle1)
    pygame.draw.rect(screen,'cyan', rectangle2)
    
    keys = pygame.key.get_pressed()
     
    if keys[pygame.K_a] and rectangle1.x > 0:
        rectangle1_left -= 300 * dt 
    if keys[pygame.K_d] and rectangle1.x < 1000-rectangle1.width:
        rectangle1_left += 300 * dt
    if keys[pygame.K_j] and rectangle2.x > 0:  
        rectangle2_left -= 300 * dt 
    if keys[pygame.K_l] and rectangle2.x < 1000-rectangle2.width:  
        rectangle2_left += 300 * dt      
    
    if ball_pos.y <= -100:
        draw_text(screen, screen.get_width()/2-200, screen.get_height()/2-50, 'cyan won')       
    if ball_pos.y >= 1100:
        draw_text(screen, screen.get_width()/2-200, screen.get_height()/2-50, 'green won')
               
                       

    # flip() the display to put your work on screen
    pygame.display.flip()
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
x = x-50
pygame.quit()