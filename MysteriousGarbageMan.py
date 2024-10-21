import pygame
import sys
import random
from bloki import *

pygame.init()

TITLE = "Mysterious Garbage Man"
BG_COLOR = (255, 255, 255)
MAP_IMAGE_PATH = "img/mapa.png"

def load_map(image_path):
    map_image = pygame.image.load(image_path)
    return pygame.transform.scale(map_image, (4000, 4000))

def main():
    global black_objects
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption(TITLE)

    # Dodanie obrazka jako czarnego obiektu
    for i in range(5):
        smieci_image = pygame.image.load(random.choice(SMIECI_IMAGE_PATH))
        smieci_scale = 4
        smieci_image = pygame.transform.scale(smieci_image, (int(smieci_image.get_width() * smieci_scale), int(smieci_image.get_height() * smieci_scale)))
        black_object_rect = smieci_image.get_rect()
        black_object_rect= (black_objects)  # Ustawienie pozycji obiektu
        black_objects.append(black_object_rect)

    black_objects = [
        pygame.Rect(3600, 500, 30, 30),
        pygame.Rect(1200, 2000, 30, 30),
        pygame.Rect(3000, 3000, 30, 30),
        pygame.Rect(1800, 2600, 30, 30),
        pygame.Rect(500, 3000, 30, 30)
    ]

    
    map_image = load_map(MAP_IMAGE_PATH)

    images = {
        'down': [pygame.transform.scale(pygame.image.load(f'img/down{i}.png'), (90, 90)) for i in range(1, 5)],
        'left': [pygame.transform.scale(pygame.image.load(f'img/left{i}.png'), (90, 90)) for i in range(1, 5)],
        'right': [pygame.transform.scale(pygame.image.load(f'img/right{i}.png'), (90, 90)) for i in range(1, 5)],
        'up': [pygame.transform.scale(pygame.image.load(f'img/up{i}.png'), (90, 90)) for i in range(1, 5)],
        'idle_down': pygame.transform.scale(pygame.image.load('img/idle_down.png'), (90, 90)),
        'idle_left': pygame.transform.scale(pygame.image.load('img/idle_left.png'), (90, 90)),
        'idle_up': pygame.transform.scale(pygame.image.load('img/idle_up.png'), (90, 90)),
        'idle_right': pygame.transform.scale(pygame.image.load('img/idle_right.png'), (90, 90))
    }

    player_x = 920 - images['down'][0].get_width() // 2
    player_y = 250 - images['down'][0].get_height() // 2
    player_speed = 5

    camera_rect = pygame.Rect(0, 0, 3000, 3000)
    camera_speed = player_speed
    clock = pygame.time.Clock()

    last_image_change_time = pygame.time.get_ticks()

    collected_blocks = 0
    total_weight = 0  # Variable to keep track of the total weight of collected garbage
    bag_capacity = 5  # Maximum capacity of the bag in kilograms
    font = pygame.font.Font(None, 36)
    block_respawn_delay = 30 * 1000  # 30 sekund
    collected_block_times = []

    def update_collected_blocks():
        nonlocal collected_blocks, total_weight
        current_time = pygame.time.get_ticks()
        for i in range(len(collected_block_times) - 1, -1, -1):
            block_time, block_weight, block_rect = collected_block_times[i]
            if current_time - block_time >= block_respawn_delay:
                black_objects.append(block_rect)
                total_weight -= block_weight
                del collected_block_times[i]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    for obj in black_objects:
                        if pygame.Rect(player_x, player_y, images['down'][0].get_width(), images['down'][0].get_height()).colliderect(obj):
                            black_objects.remove(obj)
                            # Generate random weight between 0.55kg and 2.05kg
                            garbage_weight = random.uniform(0.55, 2.05)
                            total_weight += garbage_weight
                            if total_weight > bag_capacity:
                                total_weight = bag_capacity  # Limit worka
                            collected_blocks += 1
                            collected_block_times.append((pygame.time.get_ticks(), garbage_weight, obj))
                            print("Podniesiono")

        keys = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()
        if current_time - last_image_change_time >= 200:
            if keys[pygame.K_w]:
                images['up'].append(images['up'].pop(0))
            if keys[pygame.K_a]:
                images['left'].append(images['left'].pop(0))
            if keys[pygame.K_s]:
                images['down'].append(images['down'].pop(0))
            if keys[pygame.K_d]:
                images['right'].append(images['right'].pop(0))
            last_image_change_time = current_time

        if keys[pygame.K_a]:
            player_x -= player_speed
        if keys[pygame.K_d]:
            player_x += player_speed
        if keys[pygame.K_w]:
            player_y -= player_speed
        if keys[pygame.K_s]:
            player_y += player_speed

        player_x = max(0, min(player_x, 4000 - images['down'][0].get_width()))
        player_y = max(0, min(player_y, 4000 - images['down'][0].get_height()))

        if any(pygame.Rect(player_x, player_y, images['down'][0].get_width(), images['down'][0].get_height()).colliderect(block_rect) for block_rect in block_rects):
            # Jeśli występuje kolizja z jakimkolwiek prostokątem z block_rects, zablokuj ruch gracza w tym kierunku.
            if keys[pygame.K_a]:
                player_x += player_speed  # Jeśli gracz wciska klawisz A, cofnij ruch w prawo.
            elif keys[pygame.K_d]:
                player_x -= player_speed  # Jeśli gracz wciska klawisz D, cofnij ruch w lewo.
            if keys[pygame.K_w]:
                player_y += player_speed  # Jeśli gracz wciska klawisz W, cofnij ruch w dół.
            elif keys[pygame.K_s]:
                player_y -= player_speed  # Jeśli gracz wciska klawisz S, cofnij ruch w górę.


        if player_x - camera_rect.x < (screen.get_width() + 800) // 6 and camera_rect.x > 0:
            camera_rect.x -= camera_speed
        elif player_x - camera_rect.x > (screen.get_width() - 400) * 5 // 6 and camera_rect.x < map_image.get_width() - screen.get_width():
            camera_rect.x += camera_speed
        if player_y - camera_rect.y < (screen.get_height() + 100) // 6 and camera_rect.y > 0:
            camera_rect.y -= camera_speed
        elif player_y - camera_rect.y > (screen.get_height() - 400) * 5 // 6 and camera_rect.y < map_image.get_height() - screen.get_height():
            camera_rect.y += camera_speed

        screen.fill(BG_COLOR)
        screen.blit(map_image, (0 - camera_rect.x, 0 - camera_rect.y))

        # Rysowanie smieci
        for obj in black_objects:
            screen.blit(smieci_image, (obj.x - camera_rect.x, obj.y - camera_rect.y))

        player_position = (player_x - camera_rect.x, player_y - camera_rect.y)

        if keys[pygame.K_w]:
            screen.blit(images['up'][0], player_position)
        elif keys[pygame.K_a]:
            screen.blit(images['left'][0], player_position)
        elif keys[pygame.K_d]:
            screen.blit(images['right'][0], player_position)
        elif keys[pygame.K_s]:
            screen.blit(images['down'][0], player_position)
        else:
            screen.blit(images['idle_down'], player_position)

        # Wyświetlenie licznika klocków
        text_weight = font.render(f"Worek: {total_weight:.2f} kg", True, (0, 0, 0))
        screen.blit(text_weight, (screen.get_width() - text_weight.get_width() - 10, 50))

        update_collected_blocks()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
