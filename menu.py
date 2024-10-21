import pygame
import sys
from MysteriousGarbageMan import main  # Importowanie funkcji main() z gry

# Inicjalizacja Pygame
pygame.init()

# Ustawienia ekranu
WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Menu")

# Kolory
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Wczytanie tła
background_image = pygame.image.load('img/tlo.png').convert()
background_image = pygame.transform.scale(background_image, (1920, 1080))

# Funkcja rysująca tekst na ekranie
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

# Funkcja rysująca przycisk
def draw_button(surface, color, x, y, width, height, text, text_color, font):
    pygame.draw.rect(surface, color, (x, y, width, height))
    draw_text(text, font, text_color, surface, x + width / 2, y + height / 2)

# Główna pętla menu
def main_menu():
    menu_font = pygame.font.Font(None, 40)
    button_font = pygame.font.Font(None, 30)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if start_button.collidepoint(mouse_pos):
                    # Po kliknięciu przycisku "Start" uruchom grę
                    main()  # Wywołanie funkcji main() z gry
                elif options_button.collidepoint(mouse_pos):
                    # Po kliknięciu przycisku "Opcje" otwórz nowe okno
                    open_options_window()

        # Rysowanie tła
        screen.blit(background_image, (0, 0))

        # Rysowanie przycisku "Start"
        start_button = pygame.Rect(900, 350, 200, 50)
        draw_button(screen, GRAY, start_button.x, start_button.y, start_button.width, start_button.height, "Start", BLACK, button_font)

        # Rysowanie przycisku "Opcje"
        options_button = pygame.Rect(900, 450, 200, 50)
        draw_button(screen, GRAY, options_button.x, options_button.y, options_button.width, options_button.height, "Opcje", BLACK, button_font)

        pygame.display.flip()

def open_options_window():
    options_screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    options_screen.fill(WHITE)
    pygame.display.set_caption("Opcje")
    options_font = pygame.font.Font(None, 40)
    back_button = pygame.Rect(900, 1000, 200, 50)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if back_button.collidepoint(mouse_pos):
                    running = False

        options_screen.blit(background_image, (0, 0))
        draw_button(options_screen, GRAY, back_button.x, back_button.y, back_button.width, back_button.height, "Powrót", BLACK, options_font)
        # Przykładowy tekst w drugim oknie
        draw_text("W naszej grze MysteriousGarbageMan. Chodzi o zbieranie i segregację śmieci.", options_font, BLACK, options_screen, 1000, 100)
        draw_text("Na środku planszy znajduję się skup śmieci, w którym segregujesz zebrane wcześniej śmieci. ", options_font, BLACK, options_screen, 1000, 150)
        draw_text("Śmieci losowo pojawiają się na planszy.", options_font, BLACK, options_screen, 1000, 200)
        draw_text("Sterowanie:", options_font, BLACK, options_screen, 1000, 300)
        draw_text("e-interakcja", options_font, BLACK, options_screen, 1000, 350)
        draw_text("w-poruszanie się w górę", options_font, BLACK, options_screen, 1000, 400)
        draw_text("s-poruszanie się w dół", options_font, BLACK, options_screen, 1000, 450)
        draw_text("d-poruszanie się w prawo", options_font, BLACK, options_screen, 1000, 500)
        draw_text("a-poruszanie się w lewo", options_font, BLACK, options_screen, 1000, 550)
        pygame.display.flip()

if __name__ == "__main__":
    main_menu()