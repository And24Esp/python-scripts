import random
import pygame
from pathlib import Path

current_dir = Path(__file__).parent.resolve()

card_list = list(range(52))
rnd = random.Random()
rnd.shuffle(card_list)
#print(card_list[:5])

def show_card(card_number,position):
    card_width = 936 / 13   #This measure excludes the sprite-list last column.
    card_height = 384 / 4
    patch_rectangle = ((card_number%13)*card_width, card_number//13*card_height,card_width, card_height)
    surface.blit(card_sprite_sheet, (position*72,0), patch_rectangle)

pygame.init()
card_sprite_sheet = pygame.image.load(str(current_dir) + '\\cards.png')

while True:
    ev = pygame.event.poll()
    if ev.type == pygame.QUIT:
        break
    surface = pygame.display.set_mode((72*5, 96))
    for i,v in enumerate(card_list[:5]): 
        show_card(card_list[v],i)
    pygame.display.flip()
