import cv2
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


# import os
# import sys

# if sys.platform.startswith('win32'):
#     glut_dir = r'E:\python\backend_install\freeglut-3.0.0'  # Replace with the actual path to the GLUT library directory
#     # glut_dir = r'E:\python\backend_install'  # Replace with the actual path to the GLUT library directory
#     os.environ['PATH'] = glut_dir + ';' + os.environ['PATH']
#     print("Glut Found")


# import ctypes
# from ctypes import *
# glut_lib = ctypes.cdll.LoadLibrary(r'E:\python\backend_install\freeglut-3.4.0\include\GL')
# glut_lib.glutInit(ctypes.byref(ctypes.c_int(0)), None)


# Global variables
images_directory = r'E:\python\Betic\2D to 3D challenge\New folder\img14'
image_extension = '.bmp'
image_count = 10  # Number of stereoscopic images
current_image = 0
window_width, window_height = 800, 600

def load_images():
    images = []
    for i in range(image_count):
        image_path = f'{images_directory}/image{i}{image_extension}'
        image = cv2.imread(image_path)
        images.append(image)
    return images

def draw_3d_model():
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    # Set the position and orientation of the camera
    glTranslatef(0.0, 0.0, -5.0)
    
    # Draw your 3D model here using OpenGL commands
    
    glutSwapBuffers()

def key_callback(key, x, y):
    global current_image
    if key == b' ':
        current_image = (current_image + 1) % image_count
        glutPostRedisplay()

def main():
    # Initialize OpenGL and GLUT
    # glutInit()
    # glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
    # glutInitWindowSize(window_width, window_height)
    # glutCreateWindow(b"Stereoscopic 3D Model")
    
    # Load stereoscopic images
    images = load_images()
    
    # Register callback functions
    glutDisplayFunc(draw_3d_model)
    glutKeyboardFunc(key_callback)
    
    # Set OpenGL settings
    glEnable(GL_DEPTH_TEST)
    
    # Start the main loop
    glutMainLoop()

if __name__ == '__main__':
    main()
