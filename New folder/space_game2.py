import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Player properties
PLAYER_WIDTH, PLAYER_HEIGHT = 40, 60
PLAYER_COLOR = (0, 0, 255)
PLAYER_SPEED = 5
PLAYER_JUMP = 15

# Platform properties
PLATFORM_WIDTH = 100
PLATFORM_HEIGHT = 20
PLATFORM_COLOR = GREEN

# Gravity and jumping mechanics
GRAVITY = 1
MAX_FALL_SPEED = 10

# Set FPS (Frames per second)
FPS = 60

# Define the Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - PLAYER_HEIGHT)
        self.speed = PLAYER_SPEED
        self.jump_power = PLAYER_JUMP
        self.vel_y = 0
        self.is_jumping = False

    def update(self, platform_group):  # Accept platform_group as an argument
        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

        # Apply gravity
        self.vel_y += GRAVITY
        if self.vel_y > MAX_FALL_SPEED:
            self.vel_y = MAX_FALL_SPEED
        self.rect.y += self.vel_y

        # Check if player is on a platform
        self.is_jumping = True
        for platform in platform_group:  # Use platform_group here
            if self.rect.colliderect(platform.rect) and self.vel_y > 0:
                self.rect.bottom = platform.rect.top
                self.is_jumping = False
                self.vel_y = 0

        # Jumping
        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.vel_y = -self.jump_power
            self.is_jumping = True

# Define the Platform class
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width=PLATFORM_WIDTH, height=PLATFORM_HEIGHT):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(PLATFORM_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Define the Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, width=PLATFORM_WIDTH//2, height=PLATFORM_HEIGHT):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = random.randint(2, 4)
        self.direction = random.choice([-1, 1])

    def update(self):
        self.rect.x += self.speed * self.direction
        # Reverse direction if the enemy hits the edges of the screen or platform
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.direction *= -1

# Game loop function
def main():
    # Sprite groups
    all_sprites = pygame.sprite.Group()
    platform_group = pygame.sprite.Group()  # Now properly defined
    enemy_group = pygame.sprite.Group()

    # Create player
    player = Player()
    all_sprites.add(player)

    # Create platforms
    platforms = [
        Platform(WIDTH//2 - 50, HEIGHT - 50),
        Platform(WIDTH//2 - 150, HEIGHT - 150),
        Platform(WIDTH//2 + 100, HEIGHT - 250),
        Platform(WIDTH//2 - 100, HEIGHT - 350),
        Platform(WIDTH//2, HEIGHT - 450)
    ]
    for plat in platforms:
        platform_group.add(plat)
        all_sprites.add(plat)

    # Create enemies
    enemy1 = Enemy(WIDTH // 2 - 75, HEIGHT - 160)
    enemy2 = Enemy(WIDTH // 2 + 50, HEIGHT - 360)
    enemy_group.add(enemy1, enemy2)
    all_sprites.add(enemy1, enemy2)

    # Game loop
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update all sprites and pass platform_group to player update
        player.update(platform_group)  # Pass the platform group here
        enemy_group.update()

        # Draw everything
        screen.fill(WHITE)
        all_sprites.draw(screen)

        # Check for collision with enemies
        if pygame.sprite.spritecollideany(player, enemy_group):
            print("Game Over!")
            running = False

        # Check if player reaches the top of the screen
        if player.rect.top <= 0:
            print("You Win!")
            running = False

        # Flip the display
        pygame.display.flip()

    pygame.quit()

# Run the game
if __name__ == "__main__":
    main()
