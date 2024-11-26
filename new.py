import pygame
from sys import exit

# Constants
WIDTH, HEIGHT = 1000, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 28
LINE_SPACING = 40
MARGIN = 40

# Game states
class GameState:
    INTRO = 'intro'
    SCENE1 = 'scene1'
    SCENE2 = 'scene2'
    SCENE3 = 'scene3'
    SCENE4 = 'scene4'
    SCENE5 = 'scene5'
    SCENE6 = 'scene6'
    GAME_OVER = 'game_over'
    WIN = 'win'

# Initialize Pygame
pygame.init()

# Set up the game screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('The Lost Temple of Zanithar')
clock = pygame.time.Clock()

# Load font
all_fonts = pygame.font.Font('HadriaticBold-MVPXp.ttf', FONT_SIZE)

# Load and play the sound
intro_sound = pygame.mixer.Sound('ancient-rhythm-119039.mp3')
intro_sound.play(-1)  # Loop the sound

# Load images
intro_bgi = pygame.image.load("intro1.png")
scene1_bgi = pygame.image.load("jungle_path.png")
scene2_bgi = pygame.image.load("stone_guardian.jpeg")
scene3_bgi = pygame.image.load("bridge_of_serpents.jpeg")
scene4_bgi = pygame.image.load("hall_of_trials.jpeg")
scene5_bgi = pygame.image.load("chamber_of_reflection.jpeg")
scene6_bgi = pygame.image.load("inner_sanctum.jpeg")
game_over_bgi = pygame.image.load("game_over.jpeg")
win_bgi = pygame.image.load("win.jpeg")

# Scale images to fit the screen
intro_bgi = pygame.transform.scale(intro_bgi, (WIDTH, HEIGHT))
scene1_bgi = pygame.transform.scale(scene1_bgi, (WIDTH, HEIGHT))
scene2_bgi = pygame.transform.scale(scene2_bgi, (WIDTH, HEIGHT))
scene3_bgi = pygame.transform.scale(scene3_bgi, (WIDTH, HEIGHT))
scene4_bgi = pygame.transform.scale(scene4_bgi, (WIDTH, HEIGHT))
scene5_bgi = pygame.transform.scale(scene5_bgi, (WIDTH, HEIGHT))
scene6_bgi = pygame.transform.scale(scene6_bgi, (WIDTH, HEIGHT))
game_over_bgi = pygame.transform.scale(game_over_bgi, (WIDTH, HEIGHT))
win_bgi = pygame.transform.scale(win_bgi, (WIDTH, HEIGHT))

# Game state
game_state = GameState.INTRO

# Scene texts
intro_text = [
    "The Lost Temple of Zanithar",
    "",
    "You are an adventurer seeking the fabled Lost Temple of Zanithar,",
    "an ancient temple rumored to hold great knowledge and untold treasures.",
    "The temple, hidden deep within the jungle, is protected by",
    "deadly traps and guarded by mystical beings.",
    "Many have tried to find it, but none have returned.",
    "Armed with only your wits and a handful of clues,",
    "you venture into the unknown,",
    "hoping to succeed where others have failed.",
    "",
    "Press ENTER to begin your adventure..."
]

scene1_text = [
    "The Jungle Path",
    "",
    "You find yourself at the entrance to the jungle.",
    "The dense foliage obscures the path ahead,",
    "but you know the temple lies somewhere within.",
    "Two paths lie before you, but you sense only one will lead to the temple.",
    "",
    "1. Take the dark, narrow path on the left.",
    "2. Take the well-trodden path on the right.",
    "",
    "Enter your choice (1 or 2):"
]

scene2_text = [
    "The Stone Guardian",
    "After walking for some time, you stumble upon an ancient stone statue",
    "standing in the middle of the jungle. The statue is of a humanoid figure",
    "with glowing eyes, holding a sword pointed toward the ground.",
    "As you approach, the eyes light up, and a voice echoes through the jungle:",
    "'Only the wise may pass. Answer me this:",
    "'I speak without a mouth and hear without ears.",
    "I have no body, but I come alive with wind. What am I?'",
    "1. Echo",
    "2. Fire ",
    "Enter your choice (1 or 2):"
]

scene3_text = [
    "The Bridge of Serpents",
    "",
    "You follow the hidden path and reach a wide chasm.",
    "A crumbling stone bridge stretches across it,",
    "with serpent carvings running along the sides.",
    "The wind howls as the bridge sways slightly.",
    "",
    "1. Cross the bridge carefully.",
    "2. Search for another way around the chasm.",
    "",
    "Enter your choice (1 or 2):"
]

scene4_text = [
    "The Hall of Trials",
    "After crossing the chasm, you enter the temple itself.",
    "The stone walls are covered in ancient carvings and murals",
    "depicting the history of Zanithar.",
    "You find yourself in a large hall with three doors,",
    "each marked with different symbols.",
    "",
    "1. Enter the door with the symbol of a sun.",
    "2. Enter the door with the symbol of a snake.",
    "3. Enter the door with the symbol of an eye.",
    "Enter your choice (1, 2, or 3):"
]

scene5_text = [
    "The Chamber of Reflection",
    "",
    "Inside the chamber, there is a stone mirror that reflects",
    "not your image, but the image of a massive stone idol.",
    "The idol speaks to you in a booming voice:",
    "'Only those who see clearly may proceed.",
    "Answer my question to prove your worth:",
    "'The more you take, the more you leave behind. What am I?'",
    "1. Footsteps",
    "2. Shadows",
    "Enter your choice (1 or 2):"
]

scene6_text = ["The Inner Sanctum",
               "",
"You enter the inner sanctum. A golden pedestal holds the Eye of Zanithar", 
"a powerful crystal. A ghostly guardian appears:",
"Only the pure of heart can claim the Eye."
," Answer my riddle: 'I have cities, but no houses; forests",
"but no trees; and rivers, but no water. What am I?'"
"",
"",

"1. A map",
"2. A book",
"Choose 1 or 2:"
]

game_over_text = [
    "Game Over",
    "",
    "Your adventure has come to an untimely end.",
    "The temple's traps or guardians have claimed you,",
    "and your journey ends here.",
    "",
    "Press ENTER to try again..."
]

win_text = [
    "Congratulations!",
    "",
    "You have solved all the puzzles and claimed the Eye of Zanithar!",
    "You escape the temple with its power and knowledge.",
    "The Lost Temple of Zanithar becomes a legend,",
    "and you are remembered as the greatest adventurer to have ever lived.",
    "",
    "Press ENTER to play again..."
]

def draw_text(text_list):
    for i, line in enumerate(text_list):
        text_surface = all_fonts.render(line, True, WHITE)
        screen.blit(text_surface, (MARGIN, 50 + i * LINE_SPACING))

def get_user_input():
    input_text = ""
    input_rect = pygame.Rect(MARGIN, HEIGHT - 100, WIDTH - 2 * MARGIN, 50)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return input_text
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode
        
        pygame.draw.rect(screen, WHITE, input_rect, 2)
        text_surface = all_fonts.render(input_text, True, WHITE)
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 2))
        pygame.display.flip()

# Main game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if game_state == GameState.INTRO:
                    game_state = GameState.SCENE1

    # Drawing on the screen
    if game_state == GameState.INTRO:
        screen.blit(intro_bgi, (0, 0))
        draw_text(intro_text)

    elif game_state == GameState.SCENE1:
        screen.blit(scene1_bgi, (0, 0))
        draw_text(scene1_text)
        choice = get_user_input()
        if choice == "1":
            game_state = GameState.SCENE2
        elif choice == "2":
            game_state = GameState.GAME_OVER
            pygame.time.delay(5000)

    elif game_state == GameState.SCENE2:
        screen.blit(scene2_bgi, (0, 0))
        draw_text(scene2_text)
        choice = get_user_input()
        if choice == "1":
            game_state = GameState.SCENE3
        elif choice == "2":
            game_state = GameState.GAME_OVER
            pygame.time.delay(5000)

    elif game_state == GameState.SCENE3:
        screen.blit(scene3_bgi, (0, 0))
        draw_text(scene3_text)
        choice = get_user_input()
        if choice == "1":
            game_state = GameState.GAME_OVER
            pygame.time.delay(5000)
        elif choice == "2":
            game_state = GameState.SCENE4

    elif game_state == GameState.SCENE4:
        screen.blit(scene4_bgi, (0, 0))
        draw_text(scene4_text)
        choice = get_user_input()
        if choice == "1" or choice == "2":
            game_state = GameState.GAME_OVER
            pygame.time.delay(5000)
        elif choice == "3":
            game_state = GameState.SCENE5

    elif game_state == GameState.SCENE5:
        screen.blit(scene5_bgi, (0, 0))
        draw_text(scene5_text)
        choice = get_user_input()
        if choice == "1":
            game_state = GameState.SCENE6
        elif choice == "2":
            game_state = GameState.GAME_OVER
            pygame.time.delay(5000)

    elif game_state == GameState.SCENE6:
        screen.blit(scene6_bgi, (0, 0))
        draw_text(scene6_text)
        choice = get_user_input()
        if choice == "1":
            game_state = GameState.WIN
            pygame.time.delay(5000)
        elif choice == "2":
            game_state = GameState.GAME_OVER
            pygame.time.delay(5000)

    elif game_state == GameState.GAME_OVER:
        screen.blit(game_over_bgi, (0, 0))
        draw_text(game_over_text)
        if pygame.key.get_pressed()[pygame.K_RETURN]:
            game_state = GameState.INTRO

    elif game_state == GameState.WIN:
        screen.blit(win_bgi, (0, 0))
        draw_text(win_text)
        if pygame.key.get_pressed()[pygame.K_RETURN]:
            game_state = GameState.INTRO
            

    # Update the display after drawing
    pygame.display.update()

    # Cap the frame rate
    clock.tick(60)