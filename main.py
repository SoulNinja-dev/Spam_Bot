import sys
import time
import sys
import pygame
import pyautogui
from pygame.locals import *

mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption("Spam Bot")
screen = pygame.display.set_mode((350, 250), 0, 32)

font = pygame.font.SysFont(None, 20)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False


def menu():
    while True:
        screen.fill((255, 255, 255))
        draw_text('SPAM BOT', font, (0, 0, 0), screen, 130, 20)
        draw_text('press the button and go to place you wanna spam', font, (0, 0, 0), screen, 10, 150)

        draw_text('spam', font, (0,0,0), screen, 100,50)
        draw_text('quit', font,(0,0,0), screen, 155,50)

        button_1 = pygame.Rect(90, 70, 50, 50)
        button_2 = pygame.Rect(150, 70, 50, 50)
        mx, my = pygame.mouse.get_pos()

        if button_1.collidepoint((mx, my)):
            if click:
                app()
        if button_2.collidepoint((mx, my)):
            if click:
                sys.exit()
                pygame.quit()

        pygame.draw.rect(screen, ((0,0,0)), button_1)
        pygame.draw.rect(screen, ((0,0,0)), button_2)

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


def app():
    time.sleep(5)
    f = open("spam_text.txt", 'r')
    count = 0
    while count <= 20:
        pyautogui.typewrite("this is spam")
        pyautogui.press("enter")
        count += 1


menu()
