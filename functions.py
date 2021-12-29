import matplotlib.pyplot as plt
import numpy as np
from numpy import sqrt

# Displays heat map of given array
# Domain: 2D array of real numbers
# Range: None, displays heat map
def display(grid):
    plt.imshow(grid, cmap="hot", interpolation='nearest')
    plt.show()
    return

# Finds the distance between two points a and b
# Domain: two 2D coordinates
# Range: distance, x >= 0
def distance(a, b):
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

# Returns the interpolated temperature at a point bases off the temperature of its neighbours
# Domain: Input point; Array of neighbours with their temperatures
# Range: xER
def computeTemp(point, given):
    num = 0
    den = 0
    for k in range(len(given)):
        num += given[k][2] / distance(point, given[k])
        den += 1/distance(point, given[k])
    return num/den
# Finds the nearest neighbours by radius
# Domain: coordinate; array of neighbours and temperatures; n number of neighbours
# Range:
def radialNeighbours(coordinate, given, n):
    if n >= len(given):
        return given
    return

# Returns n nearest neighbours of a given point
# Domain: grid 2D array of Reals; point [y, x]; n number of neighbours
# Range: Array of points of the nearest n neighbours (could be more than n is many on last layer)

def computeNeighbours(grid, point, num):
    yl = len(grid)
    xl = len(grid[1])
    neighbours = []
    layer = 1
    n = 0
    while n < num:
        y = point[0] + layer
        x = point[1] + layer
        for i in range(2 * layer):
            if x < 0 or y < 0 or y >= yl or x >= xl:
                y -= 1
                continue
            if grid[y][x] != 0:
                neighbours.append([y, x, grid[y][x]])
                n += 1
            y -= 1
        y = point[0] - layer
        x = point[1] + layer
        for i in range(2 * layer):
            if x < 0 or y < 0 or y >= yl or x >= xl:
                x -= 1
                continue
            if grid[y][x] != 0:
                neighbours.append([y, x, grid[y][x]])
                n += 1
            x -= 1
        y = point[0] - layer
        x = point[1] - layer
        for i in range(2 * layer):
            if x < 0 or y < 0 or y >= yl or x >= xl:
                y += 1
                continue
            if grid[y][x] != 0:
                neighbours.append([y, x, grid[y][x]])
                n += 1
            y += 1
        y = point[0] + layer
        x = point[1] - layer
        for i in range(2 * layer):
            if x < 0 or y < 0 or y >= yl or x >= xl:
                x += 1
                continue
            if grid[y][x] != 0:
                neighbours.append([y, x, grid[y][x]])
                n += 1
            x += 1
        layer += 1
    return neighbours
    
# Returns n nearest neighbours of a given point
# Domain: given set of points; point [y, x]; n number of neighbours
# Range: Array of points of the nearest n neighbours
def radialNeighbours(point, given, num):
    if len(given) <= num:
        return given

    currentPoints = []
    nearest = []

    for i in range(len(given)):
        currentPoints.append(given[i])
        currentPoints[i].append(distance(point, currentPoints[i]))
    # print(currentPoints)

    dist = len(currentPoints[0]) - 1
    for i in range(num):
        index = 0
        for j in range(1, len(currentPoints)):
            if currentPoints[j][dist] < currentPoints[index][dist]:
                index = j
        nearest.append(currentPoints[index])
        currentPoints.pop(index)
    # print(nearest)
    return nearest