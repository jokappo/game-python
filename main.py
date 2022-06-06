import pygame
from game import Game
pygame.init()
# creer une class jeu

#generer la fenetre de notre jeux
pygame.display.set_caption("comet fall game")#nom de la fenetre"
screen = pygame.display.set_mode((1080, 720)) #dimmention de la fenetre

# arriere plan
background = pygame.image.load('assets/bg.jpg')

#charger jeu
game = Game()

running = True

#boucle tant que cette condition est vrai
while running:

    #appliquer arriere plan
    screen.blit(background, (0, -200))

    #appli image
    screen.blit(game.player.image, game.player.rect)

    #actualiser la  bare de vie
    game.player.update_health_bar(screen)

    #recuperer les project
    for projectile in game.player.all_projectiles:
        projectile.move()

    # recuperer les monstre du jeu
    for monster in game.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)


    #image du projectil
    game.player.all_projectiles.draw(screen)

    # appliqer l'image des monstre
    game.all_monsters.draw(screen)


   #verification de direction
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right() #vers la droite
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()#vers la gauche



    #mettre a jour l'ecran
    pygame.display.flip()



    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # que l'évenmn est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture")

        #detecter si un joueur lachr une touche du clavier
        elif event.type == pygame.KEYDOWN:
           game.pressed[event.key] = True

           #touche espase pour lancer projectile
           if event.key == pygame.K_SPACE:
               game.player.launch_projectile()


        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False


