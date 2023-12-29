# Simple pygame program
import random
dots=[]
class dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx
        self.vy
    def draw(self):
        pygame.draw.circle(screen, (100, 100, 100), (self.x, self.y), 10)
    def update(self):
        self.vx = random.randint(-1,1)
        self.vy = random.randint(-1,1)
        self.x += self.vx 
        self.y += self.vy 

def updateScreen():
    # Fill the background with white
    screen.fill((255, 255, 255))
    
    # Flip the display
    pygame.display.flip()

def checkInputs():
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
def updateDots():
    for dot in dots:
        dot.update()
def drawDots():
    for dot in dots:
        dot.draw()


# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
running = True
while running:
    checkInputs()

    updateDots()
    drawDots()
        
    updateScreen()
# Done! Time to quit.
pygame.quit()
