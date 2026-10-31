#Module built with pygame in order to draw queen puzzle solutions of n size
import pygame
from pathlib import Path

# Getting the curret directory path instead of a fixed folder value
current_dir = Path(__file__).parent.resolve()

gravity = 0.1

class QueenSprite:

    def __init__(self, img, target_posn):
        """ Create and initialize a queen for this
            target position on the board """
        self.image = img
        self.target_posn = target_posn
        (x, y) = target_posn
        self.posn = (x, 0)     # Start ball at top of its column
        self.y_velocity = 0    #    with zero initial velocity

    def update(self):
        self.y_velocity += gravity        # Gravity changes velocity
        (x, y) = self.posn
        new_y_pos = y + self.y_velocity   # Velocity moves the ball
        (target_x, target_y) = self.target_posn   # Unpack the position
        dist_to_go = target_y - new_y_pos         # How far to our floor?

        if dist_to_go < 0:                        # Are we under floor?
            self.y_velocity = - 0.6 * self.y_velocity     # Bounce
            new_y_pos = target_y + dist_to_go     # Move back above floor

        self.posn = (x, new_y_pos)                # Set our new position.

    def draw(self, target_surface):
        target_surface.blit(self.image, self.posn)

    def contains_point(self, pt):
        """ Return True if my sprite rectangle contains point pt """
        (my_x, my_y) = self.posn
        my_width = self.image.get_width()
        my_height = self.image.get_height()
        (x, y) = pt
        return ( x >= my_x and x < my_x + my_width and
                 y >= my_y and y < my_y + my_height) 
    
    def handle_click(self):
            self.y_velocity += -6   # Kick it up


class DukeSprite:

    def __init__(self, img, target_posn):
        self.image = img
        self.posn = target_posn
        self.anim_frame_count = 0
        self.curr_patch_num = 0

    def update(self):
        if self.anim_frame_count > 0:
           self.anim_frame_count = (self.anim_frame_count + 1 ) % 60
           self.curr_patch_num = self.anim_frame_count // 6

    def draw(self, target_surface):
        patch_rect = (self.curr_patch_num * 50, 10,
                       50, self.image.get_height()-10)
        target_surface.blit(self.image, self.posn, patch_rect)

    def contains_point(self, pt):
         """ Return True if my sprite rectangle contains  pt """
         (my_x, my_y) = self.posn
         my_width = self.image.get_width() / 10   #Found and corrected bug (ex. 1)
         my_height = self.image.get_height()
         (x, y) = pt
         return ( x >= my_x and x < my_x + my_width and
                  y >= my_y and y < my_y + my_height - 10)

    def handle_click(self):
         if self.anim_frame_count == 0:
            self.anim_frame_count = 5
            

def draw_board(the_board):
    """ Draw a chess board with queens, as determined by the the_board. """

    pygame.init()
    
    colors = [(255,0,0), (0,0,0)]    # Set up colors [red, black]
    n = len(the_board)         # This is an NxN chess board.
    surface_sz = 480           # Proposed physical surface size.
    sq_sz = surface_sz // n    # sq_sz is length of a square.
    surface_sz = n * sq_sz     # Adjust to exactly fit n squares.

    # Create the surface of (width, height), and its window.
    surface = pygame.display.set_mode((surface_sz, surface_sz))

    ball = pygame.image.load(str(current_dir) + "\\beach-ball-icon.png")

    # Use an extra offset to centre the ball in its square.
    # If the square is too small, offset becomes negative,
    #   but it will still be centered :-)
    ball_offset = (sq_sz-ball.get_width()) // 2

    all_sprites = []      # Keep a list of all sprites in the game  

    #BALL/PIECE:
    # Create a sprite object for each queen, and populate our list.
    for (col, row) in enumerate(the_board):
        a_queen = QueenSprite(ball,
                   (col*sq_sz+ball_offset, row*sq_sz+ball_offset))
        all_sprites.append(a_queen)

    #DUKE:
    # Load the sprite sheet
    duke_sprite_sheet = pygame.image.load(str(current_dir) + "\\duke_spritesheet.png")

    # Instantiate two duke instances, put them on the chessboard
    duke1 = DukeSprite(duke_sprite_sheet,(sq_sz*2, 0))
    duke2 = DukeSprite(duke_sprite_sheet,(sq_sz*5, sq_sz*3))

    # Add them to the list of sprites which our game loop manages
    all_sprites.append(duke1)
    all_sprites.append(duke2)
    
    my_clock = pygame.time.Clock()

    while True:
        # 1. POLL AND HANDLE EVENTS:
        # Look for an event from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            #print(ev)
            break

        #if ev.type != pygame.NOEVENT:   # Only print if an event happens!
        #    if ev.type != pygame.MOUSEMOTION:
        #        print(ev)
        
        if ev.type == pygame.KEYDOWN:
            key = ev.dict["key"]
            if key == 27:                  # On Escape key ...
                break                      #   leave the game loop.
            if key == ord("r"):
                colors[0] = (255, 0, 0)    # Change to red + black.
            elif key == ord("g"):
                colors[0] = (0, 255, 0)    # Change to green + black.
            elif key == ord("b"):
                colors[0] = (0, 0, 255)    # Change to blue + black.

        if ev.type == pygame.MOUSEBUTTONDOWN: # Mouse gone down?
            posn_of_click = ev.dict["pos"]
            for sprite in all_sprites:
                if sprite.contains_point(posn_of_click):
                    sprite.handle_click()
                    break

        # 2. UPDATE GAME ELEMENTS:
        # Ask every sprite to update itself.
        for sprite in all_sprites:
            sprite.update()
        
        # 3. DRAW SURFACES:
        # Draw a fresh background (a blank chess board)
        for row in range(n):           # Draw each row of the board.
            c_indx = row % 2           # Alternate starting color
            for col in range(n):       # Run through cols drawing squares
                the_square = (col*sq_sz, row*sq_sz, sq_sz, sq_sz)
                surface.fill(colors[c_indx], the_square)
                # Now flip the color index for the next square
                c_indx = (c_indx + 1) % 2

        # Now that squares are drawn, draw the queens.
        #for (col, row) in enumerate(the_board):        
        #  surface.blit(ball,
        #           (col*sq_sz+ball_offset,row*sq_sz+ball_offset))

        # Ask every sprite to draw itself.
        for sprite in all_sprites:
            sprite.draw(surface)
        
        # 4. SHOW SURFACES:
        pygame.display.flip()

        my_clock.tick(60)  # Waste time so that frame rate becomes 60 fps
    
    pygame.quit()

if __name__ == "__main__":
    #draw_board([0, 5, 3, 1, 6, 4, 2])    # 7 x 7 to test window size
    draw_board([6, 4, 2, 0, 5, 7, 1, 3])
    #draw_board([0])
    #draw_board([9, 6, 0, 3, 10, 7, 2, 4, 12, 8, 11, 5, 1])  # 13 x 13
    #draw_board([11, 4, 8, 12, 2, 7, 3, 15, 0, 14, 10, 6, 13, 1, 5, 9])

