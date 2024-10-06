import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np
from PIL import Image

# Load the texture image
def load_texture(image_path):
    img = Image.open(image_path)
    img_data = np.array(list(img.getdata()), np.uint8)

    glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, 1)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.width, img.height, 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)

# Generate a spherical mesh
def sphere(radius, rings, sectors):
    vertices = []
    normals = []
    texcoords = []
    pi = np.pi
    pi_2 = pi / 2

    R = 1.0 / (rings - 1)
    S = 1.0 / (sectors - 1)
    for r in range(rings):
        for s in range(sectors):
            y = np.sin(-pi_2 + pi * r * R)
            x = np.cos(2 * pi * s * S) * np.sin(pi * r * R)
            z = np.sin(2 * pi * s * S) * np.sin(pi * r * R)

            vertices.append([x * radius, y * radius, z * radius])
            normals.append([x, y, z])
            texcoords.append([s * S, r * R])

    vertices = np.array(vertices, dtype=np.float32)
    normals = np.array(normals, dtype=np.float32)
    texcoords = np.array(texcoords, dtype=np.float32)

    return vertices, normals, texcoords

# Render the sphere
def draw_sphere(vertices, texcoords):
    glBegin(GL_QUADS)
    for i, vertex in enumerate(vertices):
        glTexCoord2fv(texcoords[i])
        glVertex3fv(vertex)
    glEnd()

def main(image_path):
    # Initialize pygame and create a window
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    # Set up modern OpenGL projection with glFrustum
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glFrustum(-1, 1, -1, 1, 1.5, 50.0)  # Replace gluPerspective
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -5)

    load_texture(image_path)

    radius = 1.0
    rings = 30
    sectors = 30
    vertices, normals, texcoords = sphere(radius, rings, sectors)

    clock = pygame.time.Clock()
    rotate_x = rotate_y = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Handle rotation
        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:
            x, y = pygame.mouse.get_rel()
            rotate_x += y * 0.2
            rotate_y += x * 0.2

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glEnable(GL_TEXTURE_2D)

        glPushMatrix()
        glRotatef(rotate_x, 1, 0, 0)
        glRotatef(rotate_y, 0, 1, 0)
        draw_sphere(vertices, texcoords)
        glPopMatrix()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main("C:\\Users\\veena\Desktop\\New folder\\mercury.jpg")  # Path to the image
