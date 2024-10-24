import pygame
global block_rects
global black_objects
global BLACK_OBJECT_IMAGES

block_rects = [
            #las ciemny
            pygame.Rect(3900, 2000, 1, 2000),
            pygame.Rect(3200, 2300, 1000, 1),
            pygame.Rect(3535, 2900, 300, 300),
            pygame.Rect(3535, 3460, 300, 350),
            pygame.Rect(2970, 3460, 300, 350),
            pygame.Rect(2500, 3600, 2000, 1),
            pygame.Rect(2700, 3250, 200, 200),
            pygame.Rect(2650, 3200, 200, 200),
            pygame.Rect(2600, 3150, 200, 200),
            pygame.Rect(2550, 3100, 200, 200),
            pygame.Rect(2550, 3030, 200, 200),
            pygame.Rect(2440, 2900, 200, 200),
            pygame.Rect(2340, 2810, 200, 200),
            pygame.Rect(2170, 2700, 200, 200),
            pygame.Rect(3030, 2207, 200, 200),
            pygame.Rect(2870, 2400, 200, 200),
            pygame.Rect(2750, 2500, 400, 250),
            pygame.Rect(3000, 2600, 400, 200),
            pygame.Rect(3400, 2590, 200, 150),
            pygame.Rect(2600, 2400, 200, 200),
            pygame.Rect(2580, 2450, 200, 200),
            pygame.Rect(2650, 2350, 200, 200),
            pygame.Rect(2700, 2250, 200, 200),
            pygame.Rect(2750, 2200, 200, 200),
            pygame.Rect(2800, 2150, 200, 200),
            pygame.Rect(3710, 3235, 100, 100),
            #pustynia
            pygame.Rect(3500, 1180, 1, 1000),
            pygame.Rect(3100, 1980, 500, 1),
            pygame.Rect(2800, 1750, 500, 1),
            pygame.Rect(2760, 1850, 200, 1),
            pygame.Rect(2960, 1650, 1, 200),
            pygame.Rect(2720, 1850, 100, 100),
            pygame.Rect(2900, 2050, 100, 100),
            pygame.Rect(3000, 2050, 100, 100),
            pygame.Rect(3100, 1980, 100, 100),
            pygame.Rect(3300, 1350, 1, 400),
            pygame.Rect(3200, 1350, 100, 100),
            pygame.Rect(2830, 1250, 400, 100),
            pygame.Rect(2430, 1180, 400, 100),
            pygame.Rect(2570, 680, 1, 600),
            pygame.Rect(2550, 730, 100, 100),
            pygame.Rect(2400, 650, 400, 100),
            pygame.Rect(2400, 550, 400, 100),
            pygame.Rect(2500, 500, 400, 100),
            pygame.Rect(2500, 400, 400, 100),
            pygame.Rect(2580, 330, 400, 100),
            pygame.Rect(2650, 230, 400, 100),
            pygame.Rect(2750, 150, 400, 100),
            pygame.Rect(2750, 0, 400, 200),
            pygame.Rect(3550, 0, 600, 250),
            pygame.Rect(3050, 0, 600, 100),
            pygame.Rect(3750, 250, 600, 100),
            pygame.Rect(3830, 250, 1, 800),
            pygame.Rect(3745, 1000, 100, 100),
            pygame.Rect(3645, 1100, 100, 100),
            pygame.Rect(3500, 1180, 200, 100),
            pygame.Rect(2650, 830, 450, 150),
            pygame.Rect(3530, 650, 200, 150),
            pygame.Rect(3550, 380, 100, 50),
            pygame.Rect(3150, 380, 100, 50),
            pygame.Rect(0, 0, 350, 1000),
            pygame.Rect(300, 0, 320, 200),
            pygame.Rect(300, 200, 200, 50),
            pygame.Rect(0, 500, 980, 1),
            pygame.Rect(980, 500, 1, 900),
            pygame.Rect(1260, 500, 1, 500),
            pygame.Rect(1360, 1000, 1, 650),
            pygame.Rect(1350, 0, 1, 901),
            pygame.Rect(0, 200, 1401, 1),
            pygame.Rect(1000, 1400, 1, 400),
            pygame.Rect(800, 1800, 200, 1),
            pygame.Rect(800, 1800, 1, 200),
            pygame.Rect(800, 2000, 200, 1),
            pygame.Rect(1000, 2000, 1, 250),
            pygame.Rect(300, 2250, 700, 170),
            pygame.Rect(0, 2250, 700, 1),
            pygame.Rect(630, 2720, 600, 400),
            pygame.Rect(1030, 3120, 1, 900),
            pygame.Rect(200, 3420, 1000, 350),
            pygame.Rect(450, 3720, 1, 350),
            pygame.Rect(950, 2720, 1400, 1),
            pygame.Rect(1400, 1620, 600, 1),
            pygame.Rect(2000, 1620, 1,200),
            pygame.Rect(2000, 1820, 700, 1),
            pygame.Rect(1300, 1820, 300, 100),
            pygame.Rect(1800, 1820, 100, 300),
            pygame.Rect(1550, 1820, 50, 300),
            pygame.Rect(1300, 2270, 800, 150),
            pygame.Rect(1300, 2100, 300, 50)
    ]

black_objects = [
        pygame.Rect(3600, 500, 30, 30),
        pygame.Rect(1200, 2000, 30, 30),
        pygame.Rect(3000, 3000, 30, 30),
        pygame.Rect(1800, 2600, 30, 30),
        pygame.Rect(500, 3000, 30, 30)
    ]

SMIECI_IMAGE_PATH = [
    "img/smieci1.png",
    "img/smieci2.png",
    "img/smieci3.png",
    "img/smieci4.png",
    "img/smieci5.png",
    "img/smieci6.png",
    "img/smieci7.png",
    "img/smieci8.png",
    "img/smieci9.png",
    "img/smieci10.png",
    "img/smieci11.png",
    "img/smieci12.png",
    "img/smieci13.png",
    "img/smieci14.png",
]