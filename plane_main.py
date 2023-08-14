import pygame
from plane_sprites import *


class PlaneGame(object):
    # Aircraft Wars Jeu principal

    def __init__(self):
        print("Initialisation du jeu")

        # 1. Créer une fenêtre pour le jeu
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2. Créer l'horloge du jeu
        self.clock = pygame.time.Clock()
        # 3. Appeler des méthodes privées, création de sprites et de groupes de sprites
        self.__create_sprites()
        # 4. Créer un événement de temporisation - création d'un ennemi 1s
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        # Tire une balle toutes les 0,5 secondes
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def __create_sprites(self):
        bg1 = Background()
        bg2 = Background(True)
        # groupe de base
        self.back_group = pygame.sprite.Group(bg1, bg2)
        # groupe d'ennemi
        self.enemy_group = pygame.sprite.Group()
        # Créer des sprites de héros et des groupes de sprites
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("Démarrer le jeu")

        while True:
            # Réglage de la fréquence de rafraîchissement
            self.clock.tick(60)
            # Auditeur d'événements
            self.__event_handler()
            # Détection des collisions
            self.__check_collide()
            # Mise à jour du jeu de sprites
            self.__update_sprites()
            # Mise à jour de l'affichage à l'écran
            pygame.display.update()

    def __event_handler(self):
        # Auditeur d'événements
        for event in pygame.event.get():
            # Déterminer s'il faut quitter le jeu
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                self.enemy_group.add(Enemy())
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

        # Obtenir les touches du clavier en utilisant les méthodes fournies par le clavier - tuple de touches
        keys_pressed = pygame.key.get_pressed()
        # Déterminer la valeur de l'index de la clé correspondante dans le tuple 1
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0

    def __check_collide(self):
        # Détection des collisions
        # 1. Les balles détruisent les avions ennemis.
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)

        # 2. Les avions ennemis s'écrasent sur les héros
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)

        # Déterminer si une liste a un contenu
        if len(enemies) > 0:
            # Laissez mourir les héros.
            self.hero.kill()

            # fin du jeu
            PlaneGame.__game_over()

    def __update_sprites(self):
        # Mise à jour du jeu de sprites
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)


    @staticmethod
    def __game_over():
        # Game Over
        print("Le jeu est terminé.")
        pygame.quit()
        exit()



if __name__ == '__main__':
    # Création d'objets de jeu
    game = PlaneGame()
    # Démarrer le jeu
    game.start_game()
