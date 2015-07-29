from pygame import *
from tree import CircularTree
import pygame


def main():
    DISPLAY = (400, 400)
    pygame.init()
    flags = DOUBLEBUF | HWSURFACE
    screen = pygame.display.set_mode(DISPLAY, flags)
    pygame.display.set_caption("planets")
    background = Surface(DISPLAY)
    background.fill(Color("#111111"))
    pixel_size = 2
    i = 0
    while i < 100:
        for event in pygame.event.get():
            if event.type == QUIT:
                raise SystemExit
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                raise SystemExit
        t = CircularTree(200, 100, 20, 3, 0.38, 0.6)
        t.generate()
        t.draw(screen, pixel_size)
        pygame.display.update()
        pygame.image.save(screen, "buffer"+str(i)+".bmp")
        i += 1


main()