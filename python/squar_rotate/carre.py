import pygame
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("3D Square Rotation")

vertices = [(1,1,0), (1,-1,0), (-1,-1,0), (-1,1,0), (1,1,2), (1,-1,2), (-1,-1,2), (-1,1,2)]

edges = [(0,1), (1,2), (2,3), (3,0), (4,5), (5,6), (6,7), (7,4), (0,4), (1,5), (2,6), (3,7)]

angle = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))

    for vertex in vertices:
        x,y,z = vertex
        y -= math.sin(angle)
        x -= math.cos(angle)
        vertex = (x,y,z)

    for edge in edges:
        vertex1 = vertices[edge[0]]
        vertex2 = vertices[edge[1]]
        pygame.draw.line(screen, (255,255,255), vertex1, vertex2)

    angle += 0.1

    pygame.display.flip()

pygame.quit()