import pygame
from pygame.locals import *
import Prize as prizeGroup


class Screen():
    def __init__(self):
        # type: () -> object
        # start pygame
        pygame.init()
        # store screen info
        self.info = pygame.display.Info()
        # create app window
        self.display = pygame.display.set_mode((self.info.current_w, self.info.current_h), FULLSCREEN)
        # HWSURFACE | DOUBLEBUF | RESIZABLE | FULLSCREEN
        # set title for window
        pygame.display.set_caption('Jackpot Screen App')

        # create a clock for frames per second
        self.clock = pygame.time.Clock()

        # set window background
        self.bgPosition = (0, 0)
        origBg = pygame.image.load('assets/background.png').convert()
        self.bg = pygame.transform.scale(origBg, (self.info.current_w, self.info.current_h))
        self.quit = False

        # create a group for prizes
        self.prizes = pygame.sprite.Group()

    def setup(self):
        first = prizeGroup.Prize('first-supp.png')
        second = prizeGroup.Prize('second-supp.png')

        self.prizes.add(first)
        self.prizes.add(second)
        pass

    def loop(self):
        while not self.quit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.quit = True

            # attach the background
            self.display.blit(self.bg, self.bgPosition)

            # add prizes to screen
            self.prizes.draw(self.display)

            # change position
            for prize in self.prizes:
                prize.test()


            # render the display
            pygame.display.flip()

            # set the frame rate
            self.clock.tick(60)

    def test(self):
        pass

    def signalTermHandler(self):
        pygame.quit()
        quit()