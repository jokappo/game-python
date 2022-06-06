import pygame
from projectile import Projectile
#creer une class joueur
class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 20
        self.velocity = 3
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def damage(self, amount):
        if self.health - amount > amount :
            self.health -= amount



    def update_health_bar(self, surface):
        # dession de la bare
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y + 20, self.max_health, 10])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y + 20, self.health, 10])

    def launch_projectile(self):
        # nouveil instance de projectil
        self.all_projectiles.add(Projectile(self))






    def move_right(self):
        # si le joueur n'est pas en colision ave un monstre
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity


    def move_left(self):
       # if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x -= self.velocity



