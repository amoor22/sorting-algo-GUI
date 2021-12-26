from random import random
import pygame
from time import sleep

pygame.init()

screen_width, screen_height = 600, 500
win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Sorting')

clock = pygame.time.Clock()

# CONSTS
nbars = 30
top_margin = 0.1
width_margin = 0.5
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
sort_algo = {'bubble': 0, 'insertion': 1}

class Bar:
    def __init__(self, height, index) -> None:
        self.width = (screen_width // nbars)
        self.draw_width = self.width - width_margin * self.width
        self.height = height * (screen_height - screen_height * top_margin)
        self.color = RED
        self.index = index
    def draw(self):
        y = screen_height - self.height
        x = self.index * self.width
        pygame.draw.rect(win, self.color, (x + (width_margin * 0.5 * self.width), y, self.draw_width, self.height))
sorted = False
def RedrawGameWindow(bars):
    global sorted
    win.fill(0)
    for i in range(len(bars)):
        bars[i].draw()
    if not sorted:
        if sort_algo['bubble']:
            for i in range(len(bars)):
                sorted = True
                for j in range(len(bars)- i - 1):
                    if bars[j].height > bars[j + 1].height:
                        bars[j], bars[j+1] = bars[j+1], bars[j]
                        bars[j].index = j
                        bars[j+1].index = j+1
                        win.fill(0)
                        for i in range(len(bars)):
                            bars[i].draw()
                        # sleep(.05)
                        clock.tick(5)
                        pygame.display.update()
        elif sort_algo['insertion']:
            for i in range(1, len(bars)):
                current = bars[i]
                for j in range(i - 1, -1, -1):
                    if bars[j].height > current.height:
                        bars[j + 1] = bars[j]
                        bars[j + 1].index = bars[j].index
                        bars[j] = current
                        bars[j].index = current.index
                    win.fill(0)
                    for f in range(len(bars)):
                        bars[f].draw()
                    # sleep(0.05)
                    clock.tick(5)
                    pygame.display.update()
                

    pygame.display.update()

def main():
    running = True
    bars = [Bar(random(), i) for i in range(nbars)]
    while running:
        RedrawGameWindow(bars)
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
# sleep(0.5)
main()