import pygame, sys
from element import *
from connectFour import *
from pygame.locals import *


pygame.init()

screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Menu")
skill = 30
defensiveness = 30
aggressiveness = 30
outputDefensiveness = 1
outputAggressiveness = 1
depth = 1
invertMinimax = False

def getFont(size):
    return pygame.font.SysFont("calibri", size, bold=True)

def renderText(screen, color, text, xPos, yPos, size):
    label = getFont(size).render(text, 1, color)
    screen.blit(label, (xPos, yPos))

def Button2(screen, x, y, width, height, color, action=None):
    global skill, defensiveness, aggressiveness, invertMinimax
    mousePos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    pygame.draw.rect(screen, color, (x, y, width, height))

    if x + width > mousePos[0] > x and y + height + 12 > mousePos[1] > y - 12:
        if click[0] == 1 and action != None:
            if action == "scroll1":
                skill = mousePos[0]
            elif action == "scroll2":
                defensiveness = mousePos[0]
            elif action == "scroll3":
                aggressiveness = mousePos[0]

def play():
    pygame.display.set_caption("Connect Four")
    startGame(depth, outputDefensiveness, outputAggressiveness, invertMinimax)
    mainMenu()


def settings():
    pygame.display.set_caption("Settings")
    while True:
        global depth, outputDefensiveness, outputAggressiveness
        screen.fill("black")
        mousePos = pygame.mouse.get_pos()

        optionsText = getFont(75).render("AI Settings: ", True, "White")
        optionsRect = optionsText.get_rect(center=(350, 50))
        skillText = getFont(45).render("Skill: ", True, "White")
        skillRect = optionsText.get_rect(center=(200, 100))
        defensivnessText = getFont(45).render("Defensiveness: ", True, "White")
        defensivnessRect = optionsText.get_rect(center=(200, 250))
        aggressivenessText = getFont(45).render("Aggressiveness: ", True, "White")
        aggressivenessRect = optionsText.get_rect(center=(200, 400))
        screen.blit(optionsText, optionsRect)
        screen.blit(skillText, skillRect)
        screen.blit(defensivnessText, defensivnessRect)
        screen.blit(aggressivenessText, aggressivenessRect)

        optionsBack = Button(None, (350, 630), "BACK", getFont(75), "White", "Green")

        optionsBack.changeColor(mousePos)
        optionsBack.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if optionsBack.checkForInput(mousePos):
                    mainMenu()

        # Skill
        Button2(screen, 30, 150, 400, 2, (255, 255, 255), action="scroll1")
        pygame.draw.rect(screen, (255, 255, 255), [skill, 150 - 12, 10, 24])
        depth = round((skill / 100 + 0.7), 0)
        renderText(screen, (255, 255, 255), str(depth), 480, 125, 45)

        # Defensiveness
        Button2(screen, 30, 300, 400, 2, (255, 255, 255), action="scroll2")
        pygame.draw.rect(screen, (255, 255, 255), [defensiveness, 300 - 12, 10, 24])
        outputDefensiveness = round((defensiveness / 100 + 0.7), 0)
        renderText(screen, (255, 255, 255), str(outputDefensiveness), 480, 275, 45)

        # Agressiveness
        Button2(screen, 30, 450, 400, 2, (255, 255, 255), action="scroll3")
        pygame.draw.rect(screen, (255, 255, 255), [aggressiveness, 450 - 12, 10, 24])
        outputAggressiveness = round((aggressiveness / 100 + 0.7), 0)
        renderText(screen, (255, 255, 255), str(outputAggressiveness), 480, 425, 45)

        pygame.display.update()

def mainMenu():
    global screen
    screen = pygame.display.set_mode((700, 700))

    while True:
        screen.fill("black")
        mousePos = pygame.mouse.get_pos()

        menuText1 = getFont(100).render("Connect Four", True, (255, 255, 255))
        menuRect1 = menuText1.get_rect(center=(350, 50))
        menuText2 = getFont(100).render("Main Menu", True, (255, 255, 255))
        menuRect2 = menuText2.get_rect(center=(375, 150))

        playButton = Button(pygame.image.load("menuRectangle.png"), (350, 300), "Play", getFont(75), "White", "Green")
        settingsButton = Button(pygame.image.load("menuRectangle.png"), (350, 450), "Settings", getFont(75), "White", "Green")
        quitButton = Button(pygame.image.load("menuRectangle.png"), (350, 600), "Quit", getFont(75), "White", "Green")

        screen.blit(menuText1, menuRect1)
        screen.blit(menuText2, menuRect2)

        for button in [playButton, settingsButton, quitButton]:
            button.changeColor(mousePos)
            button.update(screen)

        eventList = pygame.event.get()

        for event in eventList:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playButton.checkForInput(mousePos):
                    play()
                if settingsButton.checkForInput(mousePos):
                    settings()
                if quitButton.checkForInput(mousePos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


mainMenu()
