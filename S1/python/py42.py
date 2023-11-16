rectangle.py:
def area(length,width):
	return length*width
def perimeter(length, width):
	return 2 * (length + width)
circle.py:
import math

def area(radius):
	return math.pi * radius ** 2

def perimeter(radius):
	return 2 * math.pi * radius
cuboid.py:
def area(length, width, height):
	return 2 * (length * width + width * height + height * length)
def volume(length, width, height):
	return length * width * height
sphere.py:
import math
def area(radius):
	return 4 * math.pi * radius ** 2
def volume(radius):
	return (4 / 3) * math.pi * radius ** 3
Importing statements in main.py:
Selective import:
from graphics.rectangle import area as circle_area,perimeter as rect_perimeter
from graphics.circle import area as circle_area,perimeter as circle_perimeter
from graphics.3D_graphics.cuboid import area as cuboid_area,volume as cubiod_volume
from graphics.3D_graphics.sphere import area as cuboid_area,volume as sphere_volume
rect_length,rect_width=5,10
circle_radius=7
cuboid_length,cubiod_width,cuboid_height=3,4,5
sphere_radius=6
print("rectangle area:",rec_area(rect_length,rect_width))
print("rectangle perimeter:",rect_perimeter(rect_length,rect_width))
print("circle area:",circle_area(circle_radius))
print("circle perimeter:",circle_perimeter(circle_radius))
print("cuboid area:",cuboid_area(cuboid_length,cubiod_width,cuboid_height))
print("cuboid volume:",cuboid_volume(cuboid_length,cubiod_width,cuboid_height))
print("sphere area:",sphere_area(sphere_radius))
print("sphere volume:",sphere_volume(sphere_radius))
import everything(*):
from graphics.rectangle import *
from graphics.circle import *
from graphics.3D_graphics.cuboid import *
from graphics.3D_graphics.sphere import *
rect_length, rect_width = 5, 10
circle_radius = 7
cuboid_length, cuboid_width, cuboid_height = 3, 4, 5
sphere_radius = 6
print("rectangle area:",rec_area(rect_length,rect_width))
print("rectangle perimeter:",rect_perimeter(rect_length,rect_width))
print("circle area:",circle_area(circle_radius))
print("circle perimeter:",circle_perimeter(circle_radius))
print("cuboid area:",cuboid_area(cuboid_length,cubiod_width,cuboid_height))
print("cuboid volume:",cuboid_volume(cuboid_length,cubiod_width,cuboid_height))
print("sphere area:",sphere_area(sphere_radius))
print("sphere volume:",sphere_volume(sphere_radius))
