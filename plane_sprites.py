import random
import pygame
# Constantes pour la taille de l'écran
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# Création de constantes de temps pour les machines ennemies
CREATE_ENEMY_EVENT = pygame.USEREVENT


class GameSprite(pygame.sprite.Sprite):
    # Classe de base du génie du jeu
    def __init__(self, image_name, speed=1):
        # Appel de la méthode d'initialisation de la classe père
        super().__init__()

        # Chargement des images
        self.image = pygame.image.load(image_name)
        # Taille de l'ensemble
        self.rect = self.image.get_rect()
        # Vitesse d'enregistrement
        self.speed = speed

    def update(self, *args):
        # Mouvement par défaut dans le sens vertical
        self.rect.y += self.speed


class Background(GameSprite):
    def __init__(self, is_alt=False):
        image_name = "./images/background.png"
        super().__init__(image_name)

        # Déterminer si des images alternées sont disponibles ; si c'est le cas, placer l'image en haut de l'écran.
        if is_alt:
            self.rect.y = -self.rect.height
    """Sprites d'arrière-plan du jeu"""
    def update(self):
        # Appel à l'implémentation d'une méthode de la classe père
        super().update()

        # Déterminer s'il faut sortir de l'écran, si oui, placer l'image en haut de l'écran
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """Elfe ennemi"""

    def __init__(self):
        # 1. Appelle la méthode de la classe mère, crée le sprite de l'avion ennemi et spécifie l'image de l'avion ennemi.
        super().__init__("./images/enemy1.png")

        # 2. Fixer la vitesse initiale aléatoire de l'avion ennemi 1 ~ 3
        self.speed = random.randint(1, 3)

        # 3) Définir la position initiale aléatoire de l'avion ennemi
        self.rect.bottom = 0

        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        # 1. Appelez la méthode de la classe mère pour que l'avion ennemi se déplace dans le sens vertical.
        super().update()

        # 2. Détermine s'il vole hors de l'écran. Si c'est le cas, l'avion ennemi doit être retiré du jeu de sprites.
        if self.rect.y >= SCREEN_RECT.height:
            # print("Les avions ennemis s'envolent hors de l'écran...")
            # La méthode kill supprime le sprite de tous les groupes de sprites et le sprite est automatiquement détruit !
            self.kill()
    def __del__(self):
        print("L'avion ennemi a accroché %s" % self.rect)
