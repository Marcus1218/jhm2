import pygame
import random
import math
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
background_image = pygame.image.load('/Users/marcus/Trae/jhm2/Pygame/160995592.png')
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
player_image = pygame.image.load('/Users/marcus/Trae/jhm2/Pygame/主體.png')
player_image = pygame.transform.scale(player_image, (50, 60))
enemy_image = pygame.image.load('/Users/marcus/Trae/jhm2/Pygame/IMG_4106.PNG')
enemy_image = pygame.transform.scale(enemy_image, (50, 60))
heart_image = pygame.image.load('/Users/marcus/Trae/jhm2/Pygame/IMG_4113.PNG')
heart_image = pygame.transform.scale(heart_image, (50, 50))
game_over_image = pygame.image.load('/Users/marcus/Trae/jhm2/Pygame/9jhro9.jpg')
game_over_image = pygame.transform.scale(game_over_image, (screen_width, screen_height))
ammo_image = pygame.image.load('/Users/marcus/Trae/jhm2/Pygame/Python-logo-notext.svg.png')
ammo_image = pygame.transform.scale(ammo_image, (35, 35))
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Player settings
player_width = 50
player_height = 60
player_x = screen_width // 2
player_y = screen_height - player_height - 10
player_speed = 5

# Bullet settings
bullet_speed = 7
bullets = []

# Enemy settings
enemy_width = 50
enemy_height = 60
enemy_speed = 3
enemies = []

# Score
score = 0
font = pygame.font.SysFont(None, 36)

# Clock
clock = pygame.time.Clock()

# Difficulty settings
difficulty = None
hit_target = 0
max_misses = 0
lives = 3

# Function to display text
def display_text(text, size, color, x, y):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Function to shoot bullets in 360 degrees
def shoot_360(x, y):
    for i in range(40):
        angle = math.radians(i * (360 / 40))
        dx = math.cos(angle) * bullet_speed
        dy = math.sin(angle) * bullet_speed
        bullets.append([x, y, dx, dy])

# Main menu loop
menu = True
while menu:
    screen.fill(black)
    display_text('Select Difficulty', 48, white, screen_width // 2 - 150, screen_height // 2 - 100)
    display_text('1. Easy', 36, white, screen_width // 2 - 50, screen_height // 2 - 50)
    display_text('2. Normal', 36, white, screen_width // 2 - 50, screen_height // 2)
    display_text('3. Hard', 36, white, screen_width // 2 - 50, screen_height // 2 + 50)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                difficulty = 'easy'
                max_misses = 30
                lives = 10
                menu = False
            elif event.key == pygame.K_2:
                difficulty = 'normal'
                max_misses = 20
                lives = 5
                menu = False
            elif event.key == pygame.K_3:
                difficulty = 'hard'
                max_misses = 10
                lives = 3
                menu = False

# Main game loop
running = True
game_over = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
            player_x += player_speed
        if keys[pygame.K_SPACE]:
            bullets.append([player_x + player_width // 2, player_y, 0, -bullet_speed])
        if keys[pygame.K_z]:
            shoot_360(player_x + player_width // 2, player_y)

        for bullet in bullets:
            bullet[0] += bullet[2]
            bullet[1] += bullet[3]
            if bullet[1] < 0 or bullet[1] > screen_height or bullet[0] < 0 or bullet[0] > screen_width:
                bullets.remove(bullet)

        if random.randint(1, 20) == 1:
            enemies.append([random.randint(0, screen_width - enemy_width), 0])
        for enemy in enemies:
            enemy[1] += enemy_speed
            if enemy[1] > screen_height:
                enemies.remove(enemy)
                lives -= 1
                if lives <= 0:
                    game_over = True
        for bullet in bullets:
            for enemy in enemies:
                if (bullet[0] > enemy[0] and bullet[0] < enemy[0] + enemy_width and
                        bullet[1] > enemy[1] and bullet[1] < enemy[1] + enemy_height):
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    score += 1
                    break
        screen.blit(background_image, (0, 0))
        screen.blit(player_image, (player_x, player_y))
        for bullet in bullets:
            screen.blit(ammo_image, (bullet[0], bullet[1]))
        for enemy in enemies:
            screen.blit(enemy_image, (enemy[0], enemy[1]))
        score_text = font.render(f'Score: {score}', True, white)
        screen.blit(score_text, (10, 10))
        for i in range(lives):
            screen.blit(heart_image, (screen_width - (i + 1) * 55, 10))

    else:
        screen.blit(game_over_image, (0, 0))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()