import pygame
import random
import math
from PIL import Image

pygame.init()


def newRain(width, rainlength):
    return (random.randint(-50, width), random.randint(-(rainlength), -(rainlength/2)), random.randint(1, 3), 0)


def endpoint(start, length, angle):
    return (start[0] + length * math.cos((angle / 180) * math.pi),
            start[1] + length)


class Main:
    elements = []
    gravity = 70
    rainlength = 150
    angle = 80

    def __init__(self, windows, win_height, win_width):
        self.win = windows
        self.width = win_width
        self.height = win_height
        for _ in range(50):
            self.elements.append(newRain(self.width, self.rainlength))

    def Update(self):
        win.fill((0, 0, 0))
        for _ in range(4):
            self.elements.append(newRain(self.width, self.rainlength))

        for i in range(len(self.elements)):
            x, y, speed, prev_vel = self.elements[i]
            vel = self.gravity / speed
            x += prev_vel * math.cos((self.angle / 180) * math.pi)
            y += prev_vel
            self.elements[i] = (x, y, speed, vel)

        for e in self.elements:
            if e[1] >= self.height + 20:
                self.elements.remove(e)
                continue
            length = self.rainlength / e[2]
            thickness = 3 / e[2]
            gray = int(240 / e[2])
            color = (gray, gray, gray)
            pygame.draw.line(win, color, (e[0], e[1]), endpoint(
                (e[0], e[1]), length, self.angle), int(thickness))

        pygame.display.update()
        string_image = pygame.image.tostring(win, "RGB")
        image = Image.frombytes("RGB", (win_width, win_height), string_image)
        frames.append(image)


win_width = 1200
win_height = 500
limitFPS = 40
frame_count = 120

win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("It's heavy rain now")
main = Main(win, win_height, win_width)
clock = pygame.time.Clock()

frames = []
for _ in range(frame_count):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    main.Update()
    clock.tick(limitFPS)

pygame.quit()
frames[0].save("heavy_rain.gif", format="GIF", append_images=frames[1:],
               save_all=True, duration=int(1000/limitFPS), loop=0)
