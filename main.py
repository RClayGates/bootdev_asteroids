#!/usr/bin/python3

# import std

# import non-std
import pygame

# import local
import constants as csts

# pygame setup
pygame.init()
pygame.display.set_caption("pygame Test")

# globals/consts

screen = pygame.display.set_mode((csts.SCREEN_WIDTH, csts.SCREEN_HEIGHT))
clock = pygame.time.Clock()



def main() -> None:
    print('Starting asteroids!')
    print(f"Screen width: {csts.SCREEN_WIDTH}")
    print(f"Screen height: {csts.SCREEN_HEIGHT}")
    test_surface = pygame.Surface(csts.SURFACE_SIZE)
    test_surface.fill(csts.WHITE)
    pygame.draw.aaline(test_surface, csts.RED, (0, csts.SURFACE_SIZE[1]), (csts.SURFACE_SIZE[0], 0))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        #clear the screen
        screen.fill(csts.BLACK)
        
        # draw to the screen
        # YOUR CODE HERE
        x = (csts.SCREEN_WIDTH/2) - (csts.SCREEN_WIDTH/2)
        y = (csts.SCREEN_HEIGHT/2) - (csts.SCREEN_HEIGHT/2)
        screen.blit(test_surface, (x, y))
    
        # flip() updates the screen to make our changes visible
        pygame.display.flip()
        
        # how many updates per second
        clock.tick(60)
    pygame.quit()

# code blocks

if __name__ == "__main__":

    main()