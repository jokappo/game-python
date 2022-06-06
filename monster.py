import pygame
import random


#creation de class de monstre
class Monster(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10/1000
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540
        self.velocity = random.randint(1, 3)

    def damage(self, amount):
        #infliger les degat
        self.health -= amount

        # verification si vie<0
        if self.health <= 0:
            #supprimer
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, 3)
            self.health = self.max_health


    def update_health_bar(self, surface):
        #def couleur
        bar_color = (111, 210, 46)
        #couleur arriere
        back_bar_color = (60, 63, 60)

        #position
        bar_position = [self.rect.x + 10, self.rect.y - 20 , self.health, 5]

        #position de l'arriere
        back_bar_position = [self.rect.x + 10, self.rect.y - 20, self.max_health, 5]

        #dession de la bare
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)


    def forward(self):
        #deplacement s'il n'y a pas de colision avec le joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        #si le monstre est en colision avec le monstre
        else:
            #infliger degat
            self.game.player.damage(self.attack)


