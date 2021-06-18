import pygame
import random
pygame.init()
screen_width = 590
screen_height = 590
gamewindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rock, Paper, Scissor")
white = (255, 255, 255)
red = (255, 0, 0)
orange = (255, 69, 0)
black = (0, 0, 0)
violet = (128,0,128)
cyan = (0,255,255)
blue = (0,0,255)

rock=pygame.image.load("rock paper scissor/rock.JPG")
paper=pygame.image.load("rock paper scissor/paper.JPG")
scissor=pygame.image.load("rock paper scissor/scissor.JPG")

font = pygame.font.SysFont(None, 45)

def text_screen(text, color,x,y):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x,y])

def win(player_choice,computer_choice):
    gamewindow.fill(cyan)
    text_screen("!!ROCK-PAPER-SCISSOR!!", black, 100, 10)
    text_screen("Player", violet ,50,100)
    text_screen("Computer", violet, 400, 100)
    text_screen('!!Press "ENTER" to play again!!', orange, 60, 450)

    if player_choice==computer_choice:
        text_screen("DRAW", red, 240, 250)
        if player_choice=="rock":
            gamewindow.blit(rock,[10,200])
            gamewindow.blit(rock, [420, 200])

        if player_choice=="paper":
            gamewindow.blit(paper,[10,200])
            gamewindow.blit(paper, [410, 200])

        if player_choice=="scissor":
            gamewindow.blit(scissor,[10,200])
            gamewindow.blit(scissor, [430, 200])


    elif (player_choice=="rock" and computer_choice=="scissor") or (player_choice=="paper" and computer_choice=="rock") or (player_choice=="scissor" and computer_choice=="paper"):
        text_screen("PLAYER", blue, 230, 250)
        text_screen("WIN", blue, 255, 280)
        if (player_choice=="rock" and computer_choice=="scissor"):
            gamewindow.blit(rock, [10, 200])
            gamewindow.blit(scissor, [430, 200])
        if (player_choice=="paper" and computer_choice=="rock"):
            gamewindow.blit(paper, [10, 200])
            gamewindow.blit(rock, [420, 200])
        if (player_choice=="scissor" and computer_choice=="paper"):
            gamewindow.blit(scissor, [10, 200])
            gamewindow.blit(paper, [410, 200])

    else:
        text_screen("PLAYER", red, 230, 250)
        text_screen("LOSE", red, 250, 280)
        if (player_choice == "rock" and computer_choice == "paper"):
            gamewindow.blit(rock, [10, 200])
            gamewindow.blit(paper, [410, 200])
        if (player_choice == "paper" and computer_choice == "scissor"):
            gamewindow.blit(paper, [10, 200])
            gamewindow.blit(scissor, [430, 200])
        if (player_choice == "scissor" and computer_choice == "rock"):
            gamewindow.blit(scissor, [10, 200])
            gamewindow.blit(rock, [420, 200])


def play(x,y):
    list=["rock","paper","scissor"]
    computer_choice = random.choice(list)
    if (20<=x<=169) and (200<=y<=356):
        player_choice="rock"
        win(player_choice,computer_choice)
    if (210<=x<=378) and (200<=y<=392):
        player_choice = "paper"
        win(player_choice, computer_choice)
    if (420<=x<=563) and (200<=y<=406):
        player_choice = "scissor"
        win(player_choice, computer_choice)

def gameloop():
    exit_game = False
    gamewindow.fill(cyan)
    text_screen("!!ROCK-PAPER-SCISSOR!!",black,100,10)
    text_screen("'CLICK' on your choice", black, 125, 100)
    gamewindow.blit(rock, [20, 200])
    gamewindow.blit(paper, [210, 200])
    gamewindow.blit(scissor, [420, 200])

    while exit_game != True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_RETURN:
                    gameloop()
            if event.type == pygame.MOUSEBUTTONDOWN:
                (x, y) = pygame.mouse.get_pos()
                play(x,y)

        pygame.display.update()
gameloop()