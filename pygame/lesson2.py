# Example file showing a circle moving on screen
import pygame


#This controls the state of the game.
# If there is a function called draw, it should be able to draw the frame as follows
# frame = draw(state)
horizotal_speed = 0.2
dt = 0
dy = -1
dx =  -1
radius = 40
cyan_win = -100
green_win = 1100

screen_width = 1000
screen_height = 1000
speed_multiplier = 10

background_color = "purple"
ball_color = "black"

rectangle1_width = 200
rectangle2_width = 200
rectangle_height = 50

top_rect_color = 'red'
bottom_rect_color = 'yellow'


def reset(screen):
    ball_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    rectangle1_left = (screen_width - rectangle1_width) // 2
    rectangle2_left = (screen_width - rectangle2_width) // 2
    return ball_pos, rectangle1_left, rectangle2_left
    
def draw_text(screen, x, y, text_str):
    background = pygame.Surface((screen.get_width(), screen.get_height()))
    background.fill('purple')
    font = pygame.font.Font(None, 64)
    text = font.render(text_str, True, (128, 128, 128))
    textpos = text.get_rect(x=x, y=y)
    background.blit(text, textpos)
    screen.blit(background, (0, 0))

def update_player_pos(dy, ball_pos, dx):
    ball_pos.y += dy * speed_multiplier 
    ball_pos.x += dx*horizotal_speed * speed_multiplier   
    return ball_pos
    
def is_hitting(rectangle, ball):
    center = rectangle.x + rectangle.width/2
    return  abs(center - ball.x) <= 100+radius
    
# pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
ball_pos,rectangle1_left,rectangle2_left = reset(screen)

# This is the loop.
while running:
    
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
    # fill the screen with a color to wipe away anything from last frame
    screen.fill(background_color)
    
    ball_pos = update_player_pos(dy, ball_pos, dx)
    pygame.draw.circle(screen, ball_color, ball_pos , radius)
    
    
    top_rect = pygame.Rect(rectangle1_left, 0, rectangle1_width, rectangle_height)
    bottom_rect = pygame.Rect(rectangle2_left, screen_height - rectangle_height, rectangle2_width, rectangle_height)


    if ball_pos.y == top_rect.bottom and is_hitting(top_rect, ball_pos):
        center = top_rect.x + top_rect.width/2
        dy = 1
        if ball_pos.x > center: 
            dx = 1
        
    if ball_pos.y == bottom_rect.top and is_hitting(bottom_rect, ball_pos):
        dy = -1
        center = bottom_rect.x + bottom_rect.width/2
        if ball_pos.x > center:
            dx=1
        
    if ball_pos.x == radius:
        dx = 1
    if ball_pos.x == screen_width - radius:
        dx = -1
    
    pygame.draw.rect(screen, top_rect_color, top_rect)
    pygame.draw.rect(screen, bottom_rect_color, bottom_rect)
    
    keys = pygame.key.get_pressed()
     
    if keys[pygame.K_a] and top_rect.x > 0:
        rectangle1_left -= 300 * dt 
    if keys[pygame.K_d] and top_rect.x < screen_width - top_rect.width:
        rectangle1_left += 300 * dt
    if keys[pygame.K_j] and bottom_rect.x > 0:  
        rectangle2_left -= 300 * dt 
    if keys[pygame.K_l] and bottom_rect.x < screen_width - bottom_rect.width:  
        rectangle2_left += 300 * dt  
    out_of_bounds = ball_pos.y > screen_width or ball_pos.y < 0
    if keys[pygame.K_r] and out_of_bounds:
        ball_pos,rectangle1_left,rectangle2_left = reset(screen)
    if keys[pygame.K_q] and out_of_bounds:
        running = False
        

    if ball_pos.y <= -1*radius:
        draw_text(screen, screen.get_width()/2-200, screen.get_height()/2-50, f'{bottom_rect_color} won') 
    if ball_pos.y >= screen_height+radius:
        draw_text(screen, screen.get_width()/2-200, screen.get_height()/2-50, f'{top_rect_color} won')
               
                       

    # flip() the display to put your work on screen
    pygame.display.flip()
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()