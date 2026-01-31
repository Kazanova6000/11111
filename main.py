import pygame
import sys

# ????????????? Pygame
pygame.init()

# ????????? ??????
WIDTH = 800
HEIGHT = 600
CELL_SIZE = 80
RADIUS = 30

# ?????
BLUE = (0, 100, 255)
BLACK = (0, 0, 0)
RED = (255, 50, 50)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
GREEN = (50, 200, 50)

# ?????? ???? (8x7 ??? ? ???????)
ROWS = 8
COLS = 7

# ??????? ?????
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Four in a Row")
clock = pygame.time.Clock()

# ??????
font = pygame.font.Font(None, 60)
small_font = pygame.font.Font(None, 40)

# ??????? ????
board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
current_player = 1
game_over = False


def draw_board():
    # ???
    screen.fill((30, 30, 30))

    # ?????? ????? ??? ?????
    for col in range(COLS):
        for row in range(ROWS):
            pygame.draw.rect(screen, BLUE,
                             (col * CELL_SIZE + 10, row * CELL_SIZE + 70,
                              CELL_SIZE - 20, CELL_SIZE - 20))
            pygame.draw.circle(screen, BLACK,
                               (col * CELL_SIZE + CELL_SIZE // 2,
                                row * CELL_SIZE + 70 + CELL_SIZE // 2),
                               RADIUS + 5)

    # ?????? ?????
    for col in range(COLS):
        for row in range(ROWS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, RED,
                                   (col * CELL_SIZE + CELL_SIZE // 2,
                                    HEIGHT - (row * CELL_SIZE + CELL_SIZE // 2)),
                                   RADIUS)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, YELLOW,
                                   (col * CELL_SIZE + CELL_SIZE // 2,
                                    HEIGHT - (row * CELL_SIZE + CELL_SIZE // 2)),
                                   RADIUS)

    # ?????? New Game
    pygame.draw.rect(screen, GREEN, (WIDTH - 160, 10, 150, 50))
    new_game_text = small_font.render("New Game", True, WHITE)
    screen.blit(new_game_text, (WIDTH - 155, 20))

    # ????????? ???????? ??????
    player_color = RED if current_player == 1 else YELLOW
    player_text = small_font.render(f"Player {current_player}", True, player_color)
    screen.blit(player_text, (20, 10))


def drop_piece(col, player):
    for row in range(ROWS):
        if board[row][col] == 0:
            board[row][col] = player
            return row
    return -1


def check_win(player):
    # ???????? ????????????
    for row in range(ROWS):
        for col in range(COLS - 3):
            if all(board[row][col + i] == player for i in range(4)):
                return True

    # ???????? ??????????
    for row in range(ROWS - 3):
        for col in range(COLS):
            if all(board[row + i][col] == player for i in range(4)):
                return True

    # ???????? ?????????? ??????-????
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if all(board[row + i][col + i] == player for i in range(4)):
                return True

    # ???????? ?????????? ??????-?????
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if all(board[row - i][col + i] == player for i in range(4)):
                return True

    return False


def show_game_over():
    # ?????????????? ???
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 200))
    screen.blit(overlay, (0, 0))

    # ?????
    game_over_text = font.render("GAME OVER", True, WHITE)
    play_again_text = small_font.render("Play again? (Enter - Yes, Esc - No)", True, YELLOW)

    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 60))
    screen.blit(play_again_text, (WIDTH // 2 - play_again_text.get_width() // 2, HEIGHT // 2 + 20))
    pygame.display.flip()

    # ???? ??????? ???????
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Enter - ????? ????
                    return True
                elif event.key == pygame.K_ESCAPE:  # Esc - ?????
                    return False


# ???????? ???? ????
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            # ???????? ?????? New Game
            if WIDTH - 160 <= x <= WIDTH - 10 and 10 <= y <= 60:
                # ????? ????
                board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
                current_player = 1
                game_over = False
            elif not game_over:
                # ?????????? ??????? ??? ?????
                col = x // CELL_SIZE
                if 0 <= col < COLS:
                    row = drop_piece(col, current_player)
                    if row != -1:
                        if check_win(current_player):
                            game_over = True
                        else:
                            # ????? ??????
                            current_player = 2 if current_player == 1 else 1

    # ?????????
    draw_board()

    # ???? ???? ????????, ?????????? ?????????
    if game_over:
        result = show_game_over()
        if result:  # ???? ?????? Enter
            # ????? ????
            board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
            current_player = 1
            game_over = False
        else:  # ???? ?????? Esc
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()