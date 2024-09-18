import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = [
    [-1, -1, -1],
    [1, -1, -1],
    [1, 1, -1],
    [-1, 1, -1],
    [-1, -1, 1],
    [1, -1, 1],
    [1, 1, 1],
    [-1, 1, 1]
]

edges = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 4),
    (0, 4),
    (1, 5),
    (2, 6),
    (3, 7)
]

surfaces = [
    (0, 1, 2, 3),
    (4, 5, 6, 7),
    (0, 4, 7, 3),
    (1, 5, 6, 2),
    (3, 2, 6, 7),
    (0, 1, 5, 4),
]

colors = {
    'red': (1, 0, 0),
    'green': (0, 1, 0),
    'blue': (0, 0, 1),
    'yellow': (1, 1, 0)
}

cube_colors = [
    ['red', 'green', 'blue', 'yellow', 'red', 'green'],
    ['green', 'yellow', 'red', 'blue', 'yellow', 'blue'],
    ['blue', 'red', 'yellow', 'green', 'blue', 'red'],
    ['yellow', 'blue', 'green', 'red', 'green', 'yellow']
]

def draw_cube(cube_idx, position, scale_factor):
    scaled_vertices = [[v * scale_factor for v in vertex] for vertex in vertices]

    glBegin(GL_QUADS)
    for i, surface in enumerate(surfaces):
        glColor3fv(colors[cube_colors[cube_idx][i]])
        for vertex in surface:
            glVertex3fv([v + p for v, p in zip(scaled_vertices[vertex], position)])
    glEnd()

    glBegin(GL_LINES)
    glColor3fv((0, 0, 0))
    for edge in edges:
        for vertex in edge:
            glVertex3fv([v + p for v, p in zip(scaled_vertices[vertex], position)])
    glEnd()

def main():
    pygame.init()

    pygame.display.set_mode((400, 650), DOUBLEBUF | OPENGL | RESIZABLE)

    pygame.display.set_caption("IIS. It is insane!")

    gluPerspective(45, (400 / 650), 0.1, 50.0)
    
    glTranslatef(0, -4, -25)

    glEnable(GL_DEPTH_TEST)
    
    rotation = [0, 0]
    translation = [0, 0]
    max_up_angle = 30
    max_down_angle = 20
    scaling_factor = 1.0
    hover_scaling = 1.3
    
    cubes_position = [(0, i * 2.5, 0) for i in range(4)]

    rotating_x = 0
    rotating_y = 0

    while True:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == VIDEORESIZE:
                glViewport(0, 0, event.w, event.h)
                gluPerspective(45, (event.w / event.h), 0.1, 50.0)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    rotating_y = -1
                if event.key == pygame.K_RIGHT:
                    rotating_y = 1
                if event.key == pygame.K_UP:
                    rotating_x = -1
                if event.key == pygame.K_DOWN:
                    rotating_x = 1

            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                    rotating_y = 0
                if event.key in [pygame.K_UP, pygame.K_DOWN]:
                    rotating_x = 0

            if event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = event.pos
                if 500 < mouse_x < 700 and 100 < mouse_y < 500:
                    scaling_factor = hover_scaling
                else:
                    scaling_factor = 1.0

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                        translation[0] -= 0.5
                    else:
                        translation[1] += 0.5
                if event.button == 5:
                    if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                        translation[0] += 0.5
                    else:
                        translation[1] -= 0.5

        rotation[1] += rotating_y * 5

        new_x_rotation = rotation[0] + rotating_x * 5
        if -max_down_angle <= new_x_rotation <= max_up_angle:
            rotation[0] = new_x_rotation

        glPushMatrix()
        glTranslatef(translation[0], translation[1], 0)

        glRotatef(rotation[0], 1, 0, 0)
        glRotatef(rotation[1], 0, 1, 0)

        for i, position in enumerate(cubes_position):
            draw_cube(i, (position[0], position[1], position[2]), scaling_factor)

        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
