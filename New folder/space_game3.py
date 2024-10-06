import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Knowledge Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Player properties
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 40
PLAYER_COLOR = BLUE
PLAYER_SPEED = 5
PLAYER_HEALTH = 100

# Asteroid properties
ASTEROID_WIDTH, ASTEROID_HEIGHT = 40, 40
ASTEROID_COLOR = RED
ASTEROID_SPEED = 3

# Set FPS
FPS = 60

questions = [
    {"question": "What is the largest planet in our solar system?", "choices": ["Earth", "Mars", "Jupiter", "Venus"], "correct": 3},
    {"question": "What galaxy is Earth located in?", "choices": ["Andromeda", "Milky Way", "Sombrero", "Whirlpool"], "correct": 2},
    {"question": "Which planet is known as the Red Planet?", "choices": ["Mercury", "Venus", "Mars", "Jupiter"], "correct": 3},
    {"question": "Which planet has the most moons?", "choices": ["Jupiter", "Saturn", "Mars", "Uranus"], "correct": 1},
    {"question": "What is the name of Earth's moon?", "choices": ["Europa", "Titan", "Ganymede", "The Moon"], "correct": 4},
    {"question": "What is the hottest planet in our solar system?", "choices": ["Mercury", "Venus", "Mars", "Jupiter"], "correct": 2},
    {"question": "Who was the first human to walk on the moon?", "choices": ["Buzz Aldrin", "Yuri Gagarin", "Neil Armstrong", "John Glenn"], "correct": 3},
    {"question": "What is the smallest planet in our solar system?", "choices": ["Earth", "Mars", "Mercury", "Venus"], "correct": 3},
    {"question": "What is the name of the largest volcano in the solar system?", "choices": ["Mount Everest", "Olympus Mons", "Mauna Kea", "Vesuvius"], "correct": 2},
    {"question": "Which planet has the Great Red Spot?", "choices": ["Earth", "Mars", "Jupiter", "Saturn"], "correct": 3},
    {"question": "How many planets are in the solar system?", "choices": ["7", "8", "9", "10"], "correct": 2},
    {"question": "Which planet is closest to the sun?", "choices": ["Mercury", "Venus", "Earth", "Mars"], "correct": 1},
    {"question": "What is the name of the first artificial satellite launched into space?", "choices": ["Voyager", "Hubble", "Sputnik", "Apollo"], "correct": 3},
    {"question": "How long does it take for light from the Sun to reach Earth?", "choices": ["8 seconds", "8 minutes", "8 hours", "8 days"], "correct": 2},
    {"question": "Which planet is known for its rings?", "choices": ["Jupiter", "Saturn", "Uranus", "Neptune"], "correct": 2},
    {"question": "What is the primary gas found in the Earth's atmosphere?", "choices": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Helium"], "correct": 3},
    {"question": "What is the term for a star that suddenly increases in brightness?", "choices": ["Comet", "Supernova", "Asteroid", "Quasar"], "correct": 2},
    {"question": "Which planet is known for its tilted rotation?", "choices": ["Mars", "Venus", "Uranus", "Mercury"], "correct": 3},
    {"question": "What is the name of the dwarf planet beyond Neptune?", "choices": ["Pluto", "Eris", "Ceres", "Haumea"], "correct": 1},
    {"question": "What is the name of the galaxy closest to the Milky Way?", "choices": ["Andromeda", "Triangulum", "Whirlpool", "Sombrero"], "correct": 1},
    {"question": "What force keeps the planets in orbit around the sun?", "choices": ["Magnetism", "Gravity", "Inertia", "Electricity"], "correct": 2},
    {"question": "How old is the universe approximately?", "choices": ["13.8 million years", "4.5 billion years", "13.8 billion years", "100 billion years"], "correct": 3},
    {"question": "Which mission successfully landed the first humans on the Moon?", "choices": ["Apollo 8", "Apollo 11", "Gemini 6", "Skylab 2"], "correct": 2},
    {"question": "What planet is known as Earth's twin?", "choices": ["Venus", "Mars", "Mercury", "Neptune"], "correct": 1},
    {"question": "What is the closest star to Earth?", "choices": ["Sirius", "Alpha Centauri", "Betelgeuse", "The Sun"], "correct": 4},
]

current_question = None
question_answered = False

# Function to display the score and health
def display_info(score, health):
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    health_text = font.render(f"Health: {health}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(health_text, (10, 50))

# Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('D:\\projects\\nasa 24\\New folder\\spaceship.png').convert_alpha()  # Load player image
        self.image = pygame.transform.scale(self.image, (PLAYER_WIDTH, PLAYER_HEIGHT))  # Scale the image
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - PLAYER_HEIGHT - 10)
        self.speed = PLAYER_SPEED
        self.health = PLAYER_HEALTH

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

# Asteroid Class
class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('D:\\projects\\nasa 24\\New folder\\asteroid.png').convert_alpha()  # Load asteroid image
        self.image = pygame.transform.scale(self.image, (ASTEROID_WIDTH, ASTEROID_HEIGHT))  # Scale the image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - ASTEROID_WIDTH)
        self.rect.y = random.randint(-100, -40)
        self.speed = ASTEROID_SPEED

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.rect.x = random.randint(0, WIDTH - ASTEROID_WIDTH)
            self.rect.y = random.randint(-100, -40)

def ask_question():
    global current_question, question_answered
    if current_question is None:
        current_question = random.choice(questions)
        question_answered = False

    # Display the question
    font = pygame.font.SysFont(None, 28)
    question_text = font.render(current_question["question"], True, WHITE)
    screen.blit(question_text, (50, 200))

    # Display answer choices
    for i, choice in enumerate(current_question["choices"], start=1):
        choice_text = font.render(f"{i}. {choice}", True, WHITE)
        screen.blit(choice_text, (50, 250 + i * 30))

def check_answer(event_key):
    global current_question, question_answered
    if question_answered:
        return

    if event_key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
        answer = event_key - pygame.K_1 + 1
        question_answered = True
        if answer == current_question["correct"]:
            return True  # Correct answer
        else:
            return False  # Incorrect answer

    question_answered = True
    current_question = None

# Handling rewards and penalties
def handle_answer(is_correct, player, score):
    if is_correct:
        player.health = min(player.health + 20, 100)  # Increase health, max 100
        score += 10  # Increase score for correct answers
    else:
        player.health -= 20  # Decrease health for wrong answers
        if player.health <= 0:
            return False, score  # Game Over
    return True, score

# Main game function
def main():
    all_sprites = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()

    player = Player()
    all_sprites.add(player)

    # Create initial asteroids
    for _ in range(5):
        asteroid = Asteroid()
        all_sprites.add(asteroid)
        asteroid_group.add(asteroid)

    score = 0
    running = True
    clock = pygame.time.Clock()

    # Load the background image
    background = pygame.image.load('D:\\projects\\nasa 24\\New folder\\space_background.jpg').convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                is_correct = check_answer(event.key)
                if is_correct is not None:
                    running, score = handle_answer(is_correct, player, score)

        # Update all sprites
        all_sprites.update()

        # Check for collisions between player and asteroids
        if pygame.sprite.spritecollideany(player, asteroid_group):
            player.health -= 10
            if player.health <= 0:
                running = False  # Game Over

        # Draw the background image
        screen.blit(background, (0, 0))

        # Draw the player, asteroids, and info
        all_sprites.draw(screen)
        display_info(score, player.health)

        # Question time!
        ask_question()

        # Display the frame
        pygame.display.flip()

    # Display Game Over message
    font = pygame.font.SysFont(None, 48)
    game_over_text = font.render("Game Over!", True, WHITE)
    screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 25))
    pygame.display.flip()
    pygame.time.wait(2000)

    pygame.quit()

# Run the game
if __name__ == "__main__":
    main()
