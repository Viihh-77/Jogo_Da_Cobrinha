import pygame
import sys
import random
from pygame.locals import *

pygame.init()
pygame.mixer.init()

som_comer = pygame.mixer.Sound('cheezburguer.wav')
som_explosao = pygame.mixer.Sound('explosão.wav')

pygame.mixer.music.load('tema repo.wav')
pygame.mixer.music.play(-1)

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Tela Inicial - Meu Jogo')
mainClock = pygame.time.Clock()

BACKGROUND_COLOR = (0, 100, 0)
BUTTON_COLOR = (255, 100, 100)
BUTTON_HOVER_COLOR = (255, 150, 150)
TEXT_COLOR = (255, 255, 255)
HIGHLIGHT_COLOR = (255, 255, 0)
SNAKE_COLOR = (192, 114, 109)
FOOD_COLOR = (255, 0, 0)
TITLE_COLOR = (255, 255, 255)

BLOCK_SIZE = 20

cenario = pygame.image.load('fundoo.jpg')
cenario = pygame.transform.scale(cenario, (800, 600))

font = pygame.font.SysFont('Arial', 80, bold=True)
small_font = pygame.font.SysFont('Arial', 30)

def draw_text(text, font, color, surface, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    surface.blit(text_surface, text_rect)

def draw_button(text, surface, x, y, w, h, color, hover_color):
    mx, my = pygame.mouse.get_pos()
    button_rect = pygame.Rect(x, y, w, h)
    if button_rect.collidepoint((mx, my)):
        pygame.draw.rect(surface, hover_color, button_rect, border_radius=10)
    else:
        pygame.draw.rect(surface, color, button_rect, border_radius=10)

    text_surface = small_font.render(text, True, TEXT_COLOR)
    text_rect = text_surface.get_rect(center=(x + w // 2, y + h // 2))
    surface.blit(text_surface, text_rect)

    return button_rect

def start_game():
    snake = [(100, 100), (80, 100), (60, 100)]
    direction = (BLOCK_SIZE, 0)
    food = (
        random.randint(0, (800 - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
        random.randint(0, (600 - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
    )
    score = 0
    running = True

    while running:
        screen.fill(BACKGROUND_COLOR)
        screen.blit(cenario, (0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_UP and direction != (0, BLOCK_SIZE):
                    direction = (0, -BLOCK_SIZE)
                elif event.key == K_DOWN and direction != (0, -BLOCK_SIZE):
                    direction = (0, BLOCK_SIZE)
                elif event.key == K_LEFT and direction != (BLOCK_SIZE, 0):
                    direction = (-BLOCK_SIZE, 0)
                elif event.key == K_RIGHT and direction != (-BLOCK_SIZE, 0):
                    direction = (BLOCK_SIZE, 0)

        head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        snake = [head] + snake[:-1]

        if head == food:
            som_comer.play()
            snake.append(snake[-1])
            food = (
                random.randint(0, (800 - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
                random.randint(0, (600 - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
            )
            score += 1

        if (head in snake[1:] or
            head[0] < 0 or head[0] >= 800 or
            head[1] < 0 or head[1] >= 600):
            som_explosao.play()
            draw_text("Game Over!", font, (255, 0, 0), screen, 400, 200)
            draw_text("Pressione ESC para voltar", small_font, TEXT_COLOR, screen, 400, 300)
            pygame.display.update()
            pygame.time.wait(2000)
            return

        for part in snake:
            pygame.draw.rect(screen, SNAKE_COLOR, (*part, BLOCK_SIZE, BLOCK_SIZE))

        pygame.draw.rect(screen, FOOD_COLOR, (*food, BLOCK_SIZE, BLOCK_SIZE))

        score_text = small_font.render(f"Pontuação: {score}", True, TEXT_COLOR)
        screen.blit(score_text, (10, 10))

        pygame.display.update()
        mainClock.tick(10)

def main_menu():
    while True:
        screen.fill(BACKGROUND_COLOR)
        screen.blit(cenario, (0, 0))

        draw_text('Meu Jogo', font, TITLE_COLOR, screen, 400, 80)

        play_button = draw_button("Jogar", screen, 300, 250, 200, 50, BUTTON_COLOR, BUTTON_HOVER_COLOR)
        about_button = draw_button("Sobre", screen, 300, 350, 200, 50, BUTTON_COLOR, BUTTON_HOVER_COLOR)
        quit_button = draw_button("Sair", screen, 300, 450, 200, 50, BUTTON_COLOR, BUTTON_HOVER_COLOR)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if play_button.collidepoint(pygame.mouse.get_pos()):
                    start_game()
                if about_button.collidepoint(pygame.mouse.get_pos()):
                    about()
                if quit_button.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        mainClock.tick(60)

def about():
    running = True
    while running:
        screen.fill(BACKGROUND_COLOR)
        screen.blit(cenario, (0, 0))

        draw_text('Sobre o Jogo', font, HIGHLIGHT_COLOR, screen, 400, 80)
        draw_text('Este é um jogo da cobrinha feito com Pygame!', small_font, TEXT_COLOR, screen, 400, 250)
        draw_text('Use as setas para jogar. ESC volta ao menu.', small_font, TEXT_COLOR, screen, 400, 350)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False

        pygame.display.update()
        mainClock.tick(60)

if __name__ == "__main__":
    main_menu()
