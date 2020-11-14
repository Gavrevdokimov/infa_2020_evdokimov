#
#
# # ЛЕТАЮЩИЙ ШАРИК
#
# import tkinter as tk
# from random import randint
#
# height = 500
# width = 700
#
#
# class BALL:
#     def __init__(self):
#         self.R = randint(20, 50)
#         self.x = randint(self.R, width - self.R)
#         self.y = randint(self.R, height - self.R)
#         self.dx, self.dy = randint(1, 5), randint(1, 3)
#         self.ball_id = canvas.create_oval(self.x - self.R, self.y - self.R, self.x + self.R, self.y + self.R, fill="green")
#
#     def move(self):
#         self.x += self.dx
#         self.y += self.dy
#         if self.x + self.R > width or self.x - self.R <= 0:
#             self.dx = -self.dx
#         if self.y + self.R > height or self.y - self.R <= 0:
#             self.dy = -self.dy
#
#     def show(self):
#         canvas.move(self.ball_id, self.dx, self.dy)
#
#
# def canvas_click_handler(event):
#     print("x=", event.x, "y=", event.y)
#
#
# def tick():
#     for ball in balls:
#         ball.move()
#         ball.show()
#     root.after(10, tick)
#
#
# def main():
#     global root, canvas, balls
#
#     root = tk.Tk()
#     root.geometry(str(width) + "x" + str(height))
#     canvas = tk.Canvas(root)
#     canvas.pack(anchor = "nw", fill = tk.BOTH)
#     canvas.bind("<Button-1>", canvas_click_handler)
#     balls = [BALL() for i in range(5)]
#     tick()
#     root.mainloop()
#
# main()
#


import pygame
from pygame.draw import *

pygame.init()

WINDOW = (400, 400)
FPS = 30

screen = pygame.display.set_mode(WINDOW)

# rect(screen, (255, 0, 255), (100, 100, 200, 200))
# rect(screen, (0, 0, 255), (100, 100, 200, 200), 5)
# rect(screen, (0, 0, 255), (100, 100, 200, 200), 5)
# polygon(screen, (255, 255, 0), [(100,100), (200,50), (300,100), (100,100)])
# polygon(screen, (0, 0, 255), [(100,100), (200,50), (300,100), (100,100)], 5)

rect(screen, (128, 128, 128), (0, 0, 400, 400))

circle(screen, (255, 255, 0), (200, 200), 150)

circle(screen, (255, 0, 0), (130, 175), 30)
circle(screen, (0, 0, 0), (130, 175), 12)
circle(screen, (0, 0, 0), (130, 175), 30, 2)

circle(screen, (255, 0, 0), (270, 175), 25)
circle(screen, (0, 0, 0), (270, 175), 12)
circle(screen, (0, 0, 0), (270, 175), 25, 2)

rect(screen, (0, 0, 0), (120, 270, 160, 30))

pygame.draw.polygon(screen, (0, 0, 0), [[170, 160], [180, 150],  [65, 110], [60, 120]])


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True


pygame.quit()







