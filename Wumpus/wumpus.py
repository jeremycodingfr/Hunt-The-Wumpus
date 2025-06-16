import pygame
import random
import time
import sys

def check_neighbor_rooms(pos, item_list):
    exits = cave[pos]
    return any(item in cave[pos] for item in item_list)

def draw_room(pos, screen):
    x = 0
    y = 1
    exits = cave[player_pos]
    screen.fill((0, 0, 0))

    circle_radius = int((SCREEN_WIDTH // 2) * .75)
    pygame.draw.circle(screen, BROWN, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), circle_radius, 0)

    if exits[LEFT] > 0:
        pygame.draw.rect(screen, BROWN, ((0, SCREEN_HEIGHT // 2 - 40), (SCREEN_WIDTH // 4, 80)), 0)
    if exits[RIGHT] > 0:
        pygame.draw.rect(screen, BROWN, ((SCREEN_WIDTH - (SCREEN_WIDTH // 4), SCREEN_HEIGHT // 2 - 40), (SCREEN_WIDTH // 4, 80)), 0)
    if exits[UP] > 0:
        pygame.draw.rect(screen, BROWN, ((SCREEN_WIDTH // 2 - 40, 0), (80, SCREEN_HEIGHT // 4)), 0)
    if exits[DOWN] > 0:
        pygame.draw.rect(screen, BROWN, ((SCREEN_WIDTH // 2 - 40, SCREEN_HEIGHT - (SCREEN_WIDTH // 4)), (80, SCREEN_HEIGHT // 4)), 0)

    bats_near = check_neighbor_rooms(player_pos, bats_list)
    pit_near = check_neighbor_rooms(player_pos, pits_list)
    wumpus_near = check_neighbor_rooms(player_pos, [wumpus_pos, [-1, -1]])

    if wumpus_near:
        pygame.draw.circle(screen, RED, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), int((SCREEN_WIDTH // 2) * .5), 0)

    if player_pos in pits_list:
        pygame.draw.circle(screen, BLACK, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), int((SCREEN_WIDTH // 2) * .5), 0)

    screen.blit(player_img, (SCREEN_WIDTH // 2 - player_img.get_width() // 2, SCREEN_HEIGHT // 2 - player_img.get_height() // 2))

    if player_pos in bats_list:
        screen.blit(bat_img, (SCREEN_WIDTH // 2 - bat_img.get_width() // 2, SCREEN_HEIGHT // 2 - bat_img.get_height() // 2))

    if player_pos == wumpus_pos:
        screen.blit(wumpus_img, (SCREEN_WIDTH // 2 - wumpus_img.get_width() // 2, SCREEN_HEIGHT // 2 - wumpus_img.get_height() // 2))

    y_text_pos = 0
    pos_text = font.render("POS:" + str(player_pos), 1, (0, 255, 64))
    screen.blit(pos_text, (0, 0))
    arrow_text = font.render("Arrows: " + str(num_arrows), 1, (0, 255, 64))
    y_text_pos += pos_text.get_height() + 10
    screen.blit(arrow_text, (0, y_text_pos))

    if bats_near:
        bat_text = font.render("You hear the squeaking of bats nearby", 1, (0, 255, 64))
        y_text_pos += bat_text.get_height() + 10
        screen.blit(bat_text, (0, y_text_pos))
    if pit_near:
        pit_text = font.render("You feel a draft nearby", 1, (0, 255, 64))
        y_text_pos += pit_text.get_height() + 10
        screen.blit(pit_text, (0, y_text_pos))

    if player_pos in bats_list:
        pygame.display.flip()
        time.sleep(2.0)

def populate_cave():
    global player_pos, wumpus_pos
    player_pos = random.randint(1, 20)
    place_wumpus()
    for _ in range(NUM_BATS): place_bat()
    for _ in range(NUM_PITS): place_pit()
    for _ in range(NUM_ARROWS): place_arrow()

def place_wumpus():
    global wumpus_pos
    wumpus_pos = player_pos
    while wumpus_pos == player_pos:
        wumpus_pos = random.randint(1, 20)

def place_bat():
    bat_pos = player_pos
    while bat_pos == player_pos or bat_pos in bats_list or bat_pos == wumpus_pos or bat_pos in pits_list:
        bat_pos = random.randint(1, 20)
    bats_list.append(bat_pos)

def place_pit():
    pit_pos = player_pos
    while pit_pos == player_pos or pit_pos in bats_list or pit_pos == wumpus_pos or pit_pos in pits_list:
        pit_pos = random.randint(1, 20)
    pits_list.append(pit_pos)

def place_arrow():
    arrow_pos = player_pos
    while arrow_pos == player_pos or arrow_pos in bats_list or arrow_pos == wumpus_pos or arrow_pos in pits_list:
        arrow_pos = random.randint(1, 20)
    arrows_list.append(arrow_pos)

def check_room(pos):
    global player_pos, screen, num_arrows

    if player_pos == wumpus_pos:
        game_over("You were eaten by a WUMPUS!!!")
    if player_pos in pits_list:
        game_over("You fell into a bottomless pit!!")
    if player_pos in bats_list:
        screen.fill(BLACK)
        bat_text = font.render("Bats pick you up and place you elsewhere in the cave!", 1, (0, 255, 64))
        textrect = bat_text.get_rect(center=screen.get_rect().center)
        screen.blit(bat_text, textrect)
        pygame.display.flip()
        time.sleep(2.5)

        new_bat_pos = player_pos
        while new_bat_pos == player_pos or new_bat_pos in bats_list or new_bat_pos == wumpus_pos or new_bat_pos in pits_list:
            new_bat_pos = random.randint(1, 20)
        bats_list.remove(player_pos)
        bats_list.append(new_bat_pos)

        new_player_pos = player_pos
        while new_player_pos == player_pos or new_player_pos in bats_list or new_player_pos == wumpus_pos or new_player_pos in pits_list:
            new_player_pos = random.randint(1, 20)
        player_pos = new_player_pos

    if player_pos in arrows_list:
        screen.fill(BLACK)
        text = font.render("You have found an arrow!", 1, (0, 255, 64))
        textrect = text.get_rect(center=screen.get_rect().center)
        screen.blit(text, textrect)
        pygame.display.flip()
        time.sleep(2.5)
        num_arrows += 1
        arrows_list.remove(player_pos)

def reset_game():
    global num_arrows
    populate_cave()
    num_arrows = 3

def game_over(message):
    time.sleep(1.0)
    screen.fill(RED)
    text = font.render(message, 1, (0, 255, 64))
    textrect = text.get_rect(center=screen.get_rect().center)
    screen.blit(text, textrect)
    pygame.display.flip()
    time.sleep(2.5)
    print(message)
    pygame.quit()
    sys.exit()

def move_wumpus():
    global wumpus_pos
    if not mobile_wumpus or random.randint(1, 100) > wumpus_move_chance:
        return
    for new_room in cave[wumpus_pos]:
        if new_room and new_room != player_pos and new_room not in bats_list and new_room not in pits_list:
            wumpus_pos = new_room
            break

def shoot_arrow(direction):
    global num_arrows, player_pos
    if num_arrows == 0:
        return
    num_arrows -= 1
    if wumpus_pos == cave[player_pos][direction]:
        game_over("Your aim was true and you have killed the Wumpus!")
    else:
        print("Your arrow sails into the darkness, never to be seen again....")
        place_wumpus()
    if num_arrows == 0:
        game_over("You are out of arrows. You have died!")

def check_pygame_events():
    global player_pos
    event = pygame.event.poll()
    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
        pygame.quit()
        sys.exit()
    elif event.type == pygame.KEYDOWN:
        mods = pygame.key.get_mods()
        if event.key == pygame.K_LEFT:
            if mods & pygame.KMOD_SHIFT:
                shoot_arrow(LEFT)
            elif cave[player_pos][LEFT] > 0:
                player_pos = cave[player_pos][LEFT]
                move_wumpus()
        elif event.key == pygame.K_RIGHT:
            if mods & pygame.KMOD_SHIFT:
                shoot_arrow(RIGHT)
            elif cave[player_pos][RIGHT] > 0:
                player_pos = cave[player_pos][RIGHT]
                move_wumpus()
        elif event.key == pygame.K_UP:
            if mods & pygame.KMOD_SHIFT:
                shoot_arrow(UP)
            elif cave[player_pos][UP] > 0:
                player_pos = cave[player_pos][UP]
                move_wumpus()
        elif event.key == pygame.K_DOWN:
            if mods & pygame.KMOD_SHIFT:
                shoot_arrow(DOWN)
            elif cave[player_pos][DOWN] > 0:
                player_pos = cave[player_pos][DOWN]
                move_wumpus()

def print_instructions():
    print('''
                             Hunt The Wumpus!
Explore a 20-room cave and try to kill the Wumpus. Watch out for:
- Wumpus: You die if you enter its room.
- Pits: Fall in and die!
- Bats: They carry you to a random safe room.
Controls:
- Arrow keys to move
- SHIFT + Arrow to shoot
    ''')

# Configs
SCREEN_WIDTH = SCREEN_HEIGHT = 1000
NUM_BATS = 3
NUM_PITS = 1  # Fewer pits
NUM_ARROWS = 0
player_pos = 0
wumpus_pos = 0
num_arrows = 1
mobile_wumpus = False
wumpus_move_chance = 50

UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3
BROWN, BLACK, RED = (193, 154, 107), (0, 0, 0), (138, 7, 7)

cave = {
    1: [0, 8, 2, 5], 2: [0, 10, 3, 1], 3: [0, 12, 4, 2], 4: [0, 14, 5, 3],
    5: [0, 6, 1, 4], 6: [5, 0, 7, 15], 7: [0, 17, 8, 6], 8: [1, 0, 9, 7],
    9: [0, 18, 10, 8], 10: [2, 0, 11, 9], 11: [0, 19, 12, 10], 12: [3, 0, 13, 11],
    13: [0, 20, 14, 12], 14: [4, 0, 15, 13], 15: [0, 16, 6, 14], 16: [15, 0, 17, 20],
    17: [7, 0, 18, 16], 18: [9, 0, 19, 17], 19: [11, 0, 20, 18], 20: [13, 0, 16, 19]
}

bats_list = []
pits_list = []
arrows_list = []

print_instructions()
input("Press <ENTER> to begin.")

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF | pygame.HWSURFACE)
pygame.display.set_caption("Hunt the Wumpus")

bat_img = pygame.image.load('images/bat.png')
player_img = pygame.image.load('images/player.png')
wumpus_img = pygame.image.load('images/wumpus.png')
arrow_img = pygame.image.load('images/arrow.png')

font = pygame.font.Font(None, 36)
reset_game()

while True:
    check_pygame_events()
    draw_room(player_pos, screen)
    pygame.display.flip()
    check_room(player_pos)
