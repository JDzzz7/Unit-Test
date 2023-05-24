import random


class Node:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = False


def gen_grid(rows, cols) -> list:
    grid = [[] for i in range(rows)]
    for i in range(rows):
        for j in range(cols):
            cell = Node(j, i)
            grid[i].append(cell)
    return grid


if __name__ == '__main__':
    print(f'Hello and welcome!')
    rows = input("How many rows do you want in your grid? ")
    cols = input("How many columns do you want in your grid? ")
    # print(f'{gen_grid(int(rows), int(cols))}')

    grid = gen_grid(int(rows), int(cols))
    for i in range(len(grid)):
        for node in grid[i]:
            print(f'{node.x, node.y}')