from pygame import *
from random import randint, random
import pygame
from brunch import Brunch
from math import *

COLORS = [Color("#FFFFFF"), Color('#000000')]


def roll(probabilities):
    all_probs = sum(probabilities)
    res = randint(1, all_probs)
    i = 0
    if res <= probabilities[i]:
        return i
    for i in range(1, len(probabilities)):
        if sum(probabilities[:i]) <= res <= sum(probabilities[:i+1]):
            return i


def get_random_angle():
    anglist = [pi/3 + 0.5*(random()-0.5), 4*pi/9 + 0.5*(random()-0.5), pi/4 + 0.5*(random()-0.5)]
    return anglist[randint(0, 2)]


class CircularTree():
    def __init__(self, size, trunk_height, trunk_width, max_iterations, k, k2):
        self.size = size
        self.body = [[0 for j in range(size)] for i in range(size)]
        self.max_iterations = max_iterations
        self.trunk_height = trunk_height
        self.trunk_width = trunk_width
        self.k = k
        self.k2 = k2

    def generate(self, n=0, start=[], angle=pi/2, length=-1, width1=-1):
        if n <= self.max_iterations:
            if start == []:
                start = [self.size/2, self.size]
            if length == -1:
                length = self.trunk_height
            finish = [int(start[0]+cos(angle)*length), int(start[1]-sin(angle)*length)]
            if width1 == -1:
                width1 = self.trunk_width
            brunch = Brunch(start, finish, int(width1), int(width1*self.k), 10, 5)
            self.body = brunch.push(self.body)
            new_brunches = 0
            sign = randint(0, 1)*2 - 1
            for i in range(len(brunch.points)-1, -1, -1):
                is_parent = roll([int((len(brunch.points)-1-i)), i])
                if new_brunches < 5 and is_parent:
                    self.generate(n+1, [brunch.points[i][0], brunch.points[i][1]],
                                  angle+get_random_angle()*sign, int(length*self.k2), int(width1*self.k))
                    sign = - sign
                    new_brunches += 1

    def draw_pixel(self, screen, pixel_size, x, y):
        rect = pygame.Rect(x*pixel_size, y*pixel_size, pixel_size, pixel_size)
        pygame.draw.rect(screen, COLORS[self.body[x][y]], rect)

    def draw(self, screen, pixel_size):
        for x in range(self.size):
            for y in range(self.size):
                self.draw_pixel(screen, pixel_size, x, y)


def get_old_creepy_oak():
    return Tree