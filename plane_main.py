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

    def __create_sprites(self):
        bg1 = Background()
        bg2 = Background(True)
        # groupe de base
        self.back_group = pygame.sprite.Group(bg1, bg2)
        # groupe d'ennemi
        self.enemy_group = pygame.sprite.Group()
        # groupe de héros
        self.hero_group = pygame.sprite.Group()

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

    def __check_collide(self):
        # Détection des collisions
        pass

    def __update_sprites(self):
        # Mise à jour du jeu de sprites
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)



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