from tkinter import *
import numpy as np

#red=1
#blue=2
#green=3
#yellow=4

cube1 = np.array([
    [0, 4, 0],
    [0, 2, 0],
    [3, 4, 4],
    [0, 1, 0]
])
cube2 = np.array([
    [0, 2, 0],
    [0, 4, 0],
    [3, 4, 1],
    [0, 1, 0]
])
cube3 = np.array([
    [0, 4, 0],
    [0, 3, 0],
    [3, 2, 1],
    [0, 3, 0]
])
cube4 = np.array([
    [0, 3, 0],
    [0, 3, 0],
    [3, 4, 1],
    [0, 1, 0]
])


def turn_right(cube):
    if cube == 1:
        temp_cube=cube1[2, 0]
        temp_cube1=cube1[2, 1]
        cube1[0, 1] = cube1[2, 0]
        cube1[2, 1] = temp_cube
        temp_cube = cube1[2, 2]
        cube1[2, 2] = temp_cube1
        cube1[0, 1]=temp_cube
    if cube == 3:
        temp_cube=cube2[2, 0]
        temp_cube1=cube2[2, 1]
        cube2[0, 1] = cube2[2, 0]
        cube2[2, 1] = temp_cube
        temp_cube = cube2[2, 2]
        cube2[2, 2] = temp_cube1
        cube2[0, 1]=temp_cube
    if cube == 3:
        temp_cube=cube3[2, 0]
        temp_cube1=cube3[2, 1]
        cube3[0, 1] = cube3[2, 0]
        cube3[2, 1] = temp_cube
        temp_cube = cube3[2, 2]
        cube3[2, 2] = temp_cube1
        cube3[0, 1]=temp_cube
    if cube == 4:
        temp_cube=cube4[2, 0]
        temp_cube1=cube4[2, 1]
        cube4[0, 1] = cube4[2, 0]
        cube4[2, 1] = temp_cube
        temp_cube = cube4[2, 2]
        cube4[2, 2] = temp_cube1
        cube4[0, 1]=temp_cube
def turn_left(cube):
    if cube==4:
        temp_cube = cube1[2, 2]
        temp_cube1 = cube1[2, 1]
        cube1[0, 1] = cube1[2, 2]
        cube1[2, 1] = temp_cube
        temp_cube = cube1[2, 0]
        cube1[2, 0] = temp_cube1
        cube1[0, 1] = temp_cube
    if cube==4:
        temp_cube = cube2[2, 2]
        temp_cube1 = cube2[2, 1]
        cube2[0, 1] = cube2[2, 2]
        cube2[2, 1] = temp_cube
        temp_cube = cube2[2, 0]
        cube2[2, 0] = temp_cube1
        cube2[0, 1] = temp_cube
    if cube==4:
        temp_cube = cube3[2, 2]
        temp_cube1 = cube3[2, 1]
        cube3[0, 1] = cube3[2, 2]
        cube3[2, 1] = temp_cube
        temp_cube = cube3[2, 0]
        cube3[2, 0] = temp_cube1
        cube3[0, 1] = temp_cube
    if cube==4:
        temp_cube = cube4[2, 2]
        temp_cube1 = cube4[2, 1]
        cube4[0, 1] = cube4[2, 2]
        cube4[2, 1] = temp_cube
        temp_cube = cube4[2, 0]
        cube4[2, 0] = temp_cube1
        cube4[0, 1] = temp_cube
def turn_down(cube):
    pass
def turn_up(cube):
    pass
