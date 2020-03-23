import pygame

#button class, maybe make this in another file as well
class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False

def RedrawWindow():
    gameDisplay.fill((0, 160, 0))

    # display background image - make this another class maybe in anther file
    background = pygame.image.load(
        "C:\\Users\\coold\\Desktop\\Poker Project\\pygame prototype\\images\\poker-table.png")
    gameDisplay.blit(background, (75, 75))
    pygame.display.update()

def DisplayAction():
    RedrawWindow()
    fold = button((200,0,0), 700, 500, 100, 80, "Fold")

if __name__ == __main__:
    #initialize screen
    pygame.init()

    gameDisplay = pygame.display.set_mode((1100,700))
    pygame.display.set_caption("Hold 'Em")


    gameExit = False

    #display buttons


    #event handler
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True




    pygame.quit()
    quit()