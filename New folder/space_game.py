import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load assets (Images, Fonts, and Sounds)
# You can download appropriate space-themed images for the spaceship and background

# Player spaceship
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
spaceship_img = pygame.image.load("spaceship.png")
spaceship_img = pygame.transform.scale(spaceship_img, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

# Background
background_img = pygame.image.load("space_background.jpg")
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

# Laser (Projectile)
laser_img = pygame.image.load("laser.png")
laser_img = pygame.transform.scale(laser_img, (5, 30))



# Enemy (Asteroid or Alien)
enemy_img = pygame.image.load("asteroid.png")
enemy_img = pygame.transform.scale(enemy_img, (50, 50))

# Set FPS (Frames per second)
FPS = 60

# Define the Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = spaceship_img
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 50)
        self.speed = 5
        self.health = 100

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

# Define the Laser class
class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = laser_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = -7

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()

# Define the Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-150, -100)
        self.speed = random.randint(3, 6)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.rect.x = random.randint(0, WIDTH - self.rect.width)
            self.rect.y = random.randint(-150, -100)
            self.speed = random.randint(3, 6)

# Game loop function
def main():
    # Sprite groups
    all_sprites = pygame.sprite.Group()
    lasers = pygame.sprite.Group()
    enemies = pygame.sprite.Group()

    # Create player
    player = Player()
    all_sprites.add(player)

    # Spawn multiple enemies
    for i in range(5):
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

    # Score and health
    score = 0
    font = pygame.font.Font(None, 36)

    # Game loop
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Shooting laser
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                laser = Laser(player.rect.centerx, player.rect.top)
                all_sprites.add(laser)
                lasers.add(laser)

        # Update all sprites
        all_sprites.update()

        # Check for collisions between lasers and enemies
        hits = pygame.sprite.groupcollide(lasers, enemies, True, True)
        for hit in hits:
            score += 1
            enemy = Enemy()
            all_sprites.add(enemy)
            enemies.add(enemy)

        # Check for collisions between player and enemies
        if pygame.sprite.spritecollideany(player, enemies):
            player.health -= 1
            if player.health <= 0:
                running = False

        # Draw everything
        screen.blit(background_img, (0, 0))
        all_sprites.draw(screen)

        # Display score and health
        score_text = font.render(f"Score: {score}", True, WHITE)
        health_text = font.render(f"Health: {player.health}", True, WHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(health_text, (10, 40))

        # Flip the display
        pygame.display.flip()

    pygame.quit()

# Run the game
if __name__ == "__main__":
    main()
