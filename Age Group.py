import pygame
import datetime
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 760, 500
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
FONT = pygame.font.Font(None, 36)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Age Group Calculator")

# Input box
input_box = pygame.Rect(200, 100, 250, 40)
text = ''
output_text = ""
age_text = ""
active = False

def calculate_age_group(dob):
    try:
        birth_date = datetime.datetime.strptime(dob, "%d-%m-%Y").date()
        today = datetime.date.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

        if age < 3:
            return age, "Infant"
        elif 3 <= age < 10:
            return age, "Child"
        elif 10 <= age < 13:
            return age, "Pre-Teen"
        elif 13 <= age < 18:
            return age, "Teenager"
        elif 18 <= age < 30:
            return age, "Young Adult"
        elif 30 <= age < 45:
            return age, "Adult"
        elif 45 <= age < 60:
            return age, "Middle-aged"
        else:
            return age, "Senior"
    except ValueError:
        return None, "Invalid Date Format! Use DD-MM-YYYY"

# Main loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active = True
            else:
                active = False
        elif event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    age, output_text = calculate_age_group(text)
                    if age is not None:
                        age_text = f"Your Age: {age} years"
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

    # Render input box
    color = BLACK if active else GRAY
    pygame.draw.rect(screen, color, input_box, 2)
    txt_surface = FONT.render(text, True, BLACK)
    screen.blit(txt_surface, (input_box.x + 10, input_box.y + 5))

    # Render output text
    output_surface = FONT.render(output_text, True, BLACK)
    screen.blit(output_surface, (200, 250))

    # Render age text
    age_surface = FONT.render(age_text, True, BLACK)
    screen.blit(age_surface, (200, 300))

    # Instructions
    instruction_surface = FONT.render("Enter DOB (DD-MM-YYYY) and press Enter", True, BLACK)
    screen.blit(instruction_surface, (130, 50))

    pygame.display.flip()

pygame.quit()
sys.exit()
