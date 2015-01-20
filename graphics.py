import pygame
import random
import sys

pygame.init()

font = pygame.font.Font(None, 16)
clock = pygame.time.Clock()

keys = {"right" : pygame.K_RIGHT,
        "left" : pygame.K_LEFT,
        "up" : pygame.K_UP,
        "down" : pygame.K_DOWN,
        "escape" : pygame.K_ESCAPE,
        "spacebar" : pygame.K_SPACE,
        "a" : pygame.K_a,
        "b" : pygame.K_b,
        "c" : pygame.K_c,
        "d" : pygame.K_d,
        "e" : pygame.K_e,
        "f" : pygame.K_f,
        "g" : pygame.K_g,
        "h" : pygame.K_h,
        "i" : pygame.K_i,
        "j" : pygame.K_j,
        "k" : pygame.K_k,
        "l" : pygame.K_l,
        "m" : pygame.K_m,
        "n" : pygame.K_n,
        "o" : pygame.K_o,
        "p" : pygame.K_p,
        "q" : pygame.K_q,
        "r" : pygame.K_r,
        "s" : pygame.K_s,
        "t" : pygame.K_t,
        "u" : pygame.K_u,
        "v" : pygame.K_v,
        "w" : pygame.K_w,
        "x" : pygame.K_x,
        "y" : pygame.K_y,
        "z" : pygame.K_z}

colours = {"red"    : (176,57,25),
           "green"  : (75,176,25),
           "blue"   : (25,95,176),
           "yellow" : (250,237,57),
           "black"  : (0,0,0),
           "white"  : (255,255,255)}

images = ["png","jpg","jpeg","gif","bmp","pcx","tga","lbm","pbm","pgm","ppm","xpm"]

def make_window(x_size, y_size):
    global screen
    screen = pygame.display.set_mode((x_size, y_size))

def load(location):
    if location.split(".")[-1].lower() in images:
        return pygame.image.load(location)

def draw_picture(picture, position):
    screen.blit(picture, position)

def draw_box(colour, size, position):
    if colour in colours:
        pygame.draw.rect(screen, colours[colour], (position, size))
    else:
        pygame.draw.rect(screen, colour, (position,size))

def fill(colour):
    if colour in colours:
        screen.fill(colours[colour])
    else:
        screen.fill(colour)

def write(text, position, colour=(255,255,255)):
    if colour in colours:
        colour = colours[colour]
    screen.blit(font.render(str(text), 1, colour), position)

def keydown(key):
    return pygame.key.get_pressed()[keys[key]]

def rand(lower, upper):
    return random.randint(lower,upper)

def get_fps():
    return clock.get_fps()

def done():
    while True:
        pygame.event.pump()
        
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_ESCAPE:
                    sys.exit()

def stop():
    pygame.quit()
    sys.exit()

def next_frame():
    clock.tick(30)
    pygame.event.pump()
    
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_ESCAPE:
                sys.exit()
    
    pygame.display.flip()
    screen.fill((0,0,0))