import pygame

hero_rect = pygame.Rect(100, 500, 120, 125)

print("L'origine du héros %d %d" % (hero_rect.x, hero_rect.y))
print("La taille du héros %d %d" % (hero_rect.width, hero_rect.height))
print("%d %d" % hero_rect.size)
