import pygame
import sys
import random
from pygame.locals import *

# Inicialização do pygame
pygame.init()

# Configurações da tela
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Tela Inicial - Meu Jogo')
mainClock = pygame.time.Clock()

# Paleta de cores atualizada (tons pastel harmoniosos)
BACKGROUND_COLOR = (253, 246, 236)    # #FDF6EC
BUTTON_COLOR = (144, 200, 172)        # #90C8AC
BUTTON_HOVER_COLOR = (115, 169, 173)  # #73A9AD
TEXT_COLOR = (44, 51, 51)             # #2C3333
HIGHLIGHT_COLOR = (57, 91, 100)       # #395B64
SNAKE_COLOR = (92, 131, 116)          # #5C8374
FOOD_COLOR = (246, 114, 128)          # #F67280

# Tamanho dos blocos da cobrinha e comida
BLOCK_SIZE = 20

# Fontes
font = pygame.font.SysFont('Arial', 80, bold=True)
small_font = pygame.font.SysFont('Arial', 30)

# Função para desenhar texto
def draw_text(text, font, color, surface, x, y, letter_spacing=5):
    words = text.split(' ')
    x_offset = x - (font.size(text)[0] // 2)
    for word in words:
        word_surface = font.render(word, True, color)
        surface.blit(word_surface, (x_offset, y))
        x_offset += word_surface.get_width() + letter_spacing

# Função para desenhar botão
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

# Função do jogo da cobrinha
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

        # Mover a cobrinha
        head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        snake = [head] + snake[:-1]

        # Comer comida
        if head == food:
            snake.append(snake[-1])
            food = (
                random.randint(0, (800 - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
                random.randint(0, (600 - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
            )
            score += 1

        # Checar colisões
        if (
            head in snake[1:] or
            head[0] < 0 or head[0] >= 800 or
            head[1] < 0 or head[1] >= 600
        ):
            draw_text("Game Over!", font, (255, 0, 0), screen, 400, 200)
            draw_text("Pressione ESC para voltar", small_font, TEXT_COLOR, screen, 400, 300)
            pygame.display.update()
            pygame.time.wait(2000)
            return

        # Desenhar cobrinha
        for part in snake:
            pygame.draw.rect(screen, SNAKE_COLOR, (*part, BLOCK_SIZE, BLOCK_SIZE))

        # Desenhar comida
        pygame.draw.rect(screen, FOOD_COLOR, (*food, BLOCK_SIZE, BLOCK_SIZE))

        # Pontuação
        score_text = small_font.render(f"Pontuação: {score}", True, TEXT_COLOR)
        screen.blit(score_text, (10, 10))

        pygame.display.update()
        mainClock.tick(10)

# Tela do menu principal
def main_menu():
    while True:
        screen.fill(BACKGROUND_COLOR)
        draw_text('Meu Jogo', font, HIGHLIGHT_COLOR, screen, 400, 80, letter_spacing=10)

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

# Tela "Sobre"
def about():
    running = True
    while running:
        screen.fill(BACKGROUND_COLOR)
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

# Inicia o menu
if __name__ == "__main__":
    main_menu()