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
# 3> update Affichage de l'écran de mise à jour
# pygame.display.update()

# Dessiner l'avion du héros
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (150, 300))

# La méthode de mise à jour peut être appelée uniformément après que tout le travail de dessin a été effectué.
pygame.display.update()

while True:
    pass

pygame.quit()