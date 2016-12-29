# CodeSkulptor GUI module
from pygame import * 

# Event handler
def tick():
    print ("tick!")

# Register handler
timer = pygame.create_timer(1000, tick)

# Start timer
timer.start()
