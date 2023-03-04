from mazelib import Maze
from mazelib.generate.Prims import Prims

N = 5
M = 5

mz = Maze()
mz.generator = Prims(N, M)
mz.generate()

mz.start = (0, 1)
mz.end = (N * 2, M * 2 - 1)


maze_str = str(mz)

print(maze_str)
maze_list = maze_str.split('\n')

for z, mark_list in enumerate(maze_list):
    for x, mark in enumerate(mark_list):
        put_maze_block(mc, mark, x, z)
        print(mark)
8iu
