import pygame

# Initialisation du jeu
pygame.init()

# Créer une fenêtre pour le jeu 480 * 700
screen = pygame.display.set_mode((480, 700))

# Dessiner l'image de fond
# 1> Chargement des données d'image
bg = pygame.image.load("./images/background.png")
# 2> blit Dessiner des images
screen.blit(bg, (0, 0))

# Dessiner l'avion du héros
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (150, 300))

# La méthode de mise à jour peut être appelée uniformément après que tout le travail de dessin a été effectué.
pygame.display.update()

# Création d'objets d'horlogerie
clock = pygame.time.Clock()

# Game Loop -> Signifie le début officiel du jeu !
i = 0

while True:

    # Vous pouvez spécifier la fréquence d'exécution du code à l'intérieur du corps de la boucle.
    clock.tick(60)

    print(i)

    i += 1

    pass

pygame.quit()