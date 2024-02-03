import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Utils import *

pygame.init()

ancho_pantalla = 1000
alto_pantalla = 800
ancho_orto = 640
alto_orto = 480

pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Gráficos en PyOpenGL')


def inicializar_orto():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, ancho_orto, 0, alto_orto)


def dibujar_estrellas():
    glBegin(GL_POINTS)
    for p in estrellas:
        # arriba
        puntos.append((p[0], p[1]))
        glVertex2f(p[0], p[1])

        # lados inferior derecho
        puntos.append((p[0] + 12, p[1] - 32))
        glVertex2f(p[0] + 12, p[1] - 32)

        # lado del medio izquierdo
        puntos.append((p[0] - 20, p[1] - 15))
        glVertex2f(p[0] - 20, p[1] - 15)

        # lado del medio derecho
        puntos.append((p[0] + 20, p[1] - 15))
        glVertex2f(p[0] + 20, p[1] - 15)

        # lados inferior izquierdo
        puntos.append((p[0] - 12, p[1] - 32))
        glVertex2f(p[0] - 12, p[1] - 32)

        # arriba
        puntos.append((p[0], p[1]))
        glVertex2f(p[0], p[1])

    glEnd()
    dibujar_lineas_puntos()


def dibujar_lineas_estrellas():
    glLineWidth(2.0)
    glBegin(GL_LINES)
    glColor3f(0.0, 1.0, 0.0)
    for i in range(len(estrellas) - 1):
        glVertex2f(*estrellas[i])
        glVertex2f(*estrellas[i + 1])
    glEnd()


def dibujar_lineas_puntos():
    glLineWidth(2.0)
    glBegin(GL_LINES)
    glColor3f(0.0, 0.0, 1.0)
    for i in range(len(puntos) - 1):
        glVertex2f(*puntos[i])
        glVertex2f(*puntos[i + 1])
    glEnd()
    puntos.clear()


hecho = False
inicializar_orto()
glPointSize(5)

puntos = []
estrellas = []

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True
        elif evento.type == MOUSEBUTTONDOWN:
            p = pygame.mouse.get_pos()
            estrellas.append((map_value(0, ancho_pantalla, 0, ancho_orto, p[0]),
                              map_value(0, alto_pantalla, alto_orto, 0, p[1])))

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    dibujar_estrellas()

    if len(estrellas) >= 2:
        dibujar_lineas_estrellas()

    pygame.display.flip()
    pygame.time.wait(100)

pygame.quit()
