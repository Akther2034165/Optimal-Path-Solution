from sys import maxsize
from itertools import permutations

def tsp(matrix):
    V = len(matrix)
    var = [i for i in range(1, V)]
    s = 0
    min_path = maxsize
    next_per = permutations(var)
    
    for i in next_per:
        cw = 0
        k = s
        for j in i:
            cw += matrix[k][j]
            k = j 
        cw += matrix[k][s]
        min_path = min(min_path, cw)
        if min_path == cw:
            pos = i 
    
    return min_path, pos

def print_path(path, output_file):
    path_str = 'The Optimal path is : 1'
    for i in path:
        path_str += f' -> {i + 1}'
    path_str += ' -> 1\n'

    with open(output_file, 'w') as file:
        file.write(path_str)

graph =  [
         [  0, 5, 3, 2, 6, 4, 1, 8, 7,10],
         [  5, 0, 5, 3, 4, 5, 4, 8, 8, 9],
         [  3, 5, 0, 2, 4, 5, 2, 9, 8,10],
         [  2, 3, 5, 0, 3, 4, 3, 7, 6, 8],
         [  6, 5, 4, 3, 0, 1, 5, 3, 2, 4],
         [  4, 5, 5, 4, 1, 0, 4, 2, 1, 3],
         [  5, 5, 2, 3, 5, 4, 0, 6, 5, 7],
         [  8, 9, 5, 7, 3, 2, 6, 0, 1, 2],
         [  7, 8, 5, 6, 2, 1, 5, 1, 0, 3],
         [  9,10, 5, 8, 4, 3, 7, 2, 3, 0],
        ]

min_path, route = tsp(graph)
route = reversed(route)
output_file = "output.txt"
print_path(route, output_file)
