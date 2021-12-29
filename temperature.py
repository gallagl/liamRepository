import numpy as np
import matplotlib.pyplot as plt
import functions as f

# Set the size of the arrays
# circle/square indicates the search method for the nearest neighbours
y = 50
x = 50
tmpGrid = [[0 for j in range(x)] for i in range(y)]
circleGrid = [[0 for j in range(x)] for i in range(y)]
squareGrid = [[0 for j in range(x)] for i in range(y)]

# Given points and their respective temperatures (values)
given = [[4, 16, 1.001], [40, 37, 2.001], [23, 42, 2.001], [45, 22, 1.201],
         [20, 13, 1.001], [33, 3, 1.1001], [12, 40, 1.701], [23, 35, 1.7001],
         [14, 36, 1.901], [4, 37, 2.001], [11, 42, 1.801], [37, 4, 1.001],
         [30, 13, 1.001], [16, 33, 1.8001], [40, 16, 1.4001], [15, 25, 1.3001]]

# Number of nearest neighbours
num = 18
if num > len(given):
    num = len(given)

# Sets the temporary grid for the square search
for i in range(len(given)):
    tmpGrid[given[i][0]][given[i][1]] = given[i][2]

# Main function
for i in range(x):
    for j in range(y):
        neighbours = []
        squareNeighbours = []
        if tmpGrid[i][j] != 0:
            continue
        squareNeighbours = f.computeNeighbours(tmpGrid, [i, j], num)
        neighbours = f.radialNeighbours([i, j], given, num)

        squareGrid[i][j] = f.computeTemp([i, j], squareNeighbours)
        circleGrid[i][j] = f.computeTemp([i, j], neighbours)

for i in range(len(given)):
    circleGrid[given[i][0]][given[i][1]] = given[i][2]
    squareGrid[given[i][0]][given[i][1]] = given[i][2]

f.display(circleGrid)
f.display(squareGrid)





