import pygame
import ScreenGroup as sg


class Prize(pygame.sprite.Sprite):

    def __init__(self, imageFile):
        pygame.sprite.Sprite.__init__(self)
        print imageFile
        image = pygame.image.load('assets/' + imageFile).convert_alpha()
        self.image = image
        self.rect = image.get_rect()

        # create font and text for prize
        self.prizeFont = pygame.font.SysFont('Sans', 50)
        self.prizeText = self.prizeFont.render('2504,35', True, (255, 255, 255))

        # create font and text for location
        self.locationFont = pygame.font.SysFont('Sans', 20)
        self.locationText = self.locationFont.render('In MY location from town', True, (255, 255, 255))

        self.image.blit(self.prizeText, self.rect)
        self.image.blit(self.locationText, self.rect)

    def setPrize(self, prizeAmount):
        pass

    def setLocation(self, location):
        pass

    def test(self):
        self.rect.y += 1