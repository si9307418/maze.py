import random

# генерируем лабиринт
def generate_maze(width, height):
    maze = [[1] * width + [1] for _ in range(height)] + [[1] * (width + 1)]
    for row in range(height):
        for column in range(width):
            if random.randint(0, 1):
                maze[row][column] *= 0
            else:
                if row == 0:
                    maze[row][column] *= 0
                else:
                    maze[row][column - 1] *= 0
    return maze

# находим путь к выходу
def solve_maze(maze, x, y):
    if maze[y][x] == 0:
        maze[y][x] = 2
        if solve_maze(maze, x + 1, y) or solve_maze(maze, x - 1, y) or solve_maze(maze, x, y + 1) or solve_maze(maze, x, y - 1):
            return True
    elif maze[y][x] == 1:
        return False
    elif maze[y][x] == 2:
        return False
    return True

# печатаем лабиринт
def print_maze(maze):
    for row in maze:
        print("".join(["#" if cell == 1 else " " for cell in row]))

# создаем лабиринт и печатаем его
maze = generate_maze(20, 10)
print_maze(maze)

# находим выход и печатаем лабиринт с путем к выходу
solve_maze(maze, 0, 0)
print_maze(maze)
