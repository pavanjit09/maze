import random

def create_maze(size):
    maze = [[' ' for _ in range(size)] for _ in range(size)]
    exit_x, exit_y = random.randint(0, size-1), random.randint(0, size-1)
    maze[exit_x][exit_y] = 'E'  # E stands for Exit
    return maze, (exit_x, exit_y)

def print_maze(maze, player_pos):
    size = len(maze)
    for i in range(size):
        for j in range(size):
            if (i, j) == player_pos:
                print("P", end=" ")  # P stands for Player
            else:
                print(maze[i][j], end=" ")
        print()

def move_player(player_pos, direction, size):
    x, y = player_pos
    if direction == "up" and x > 0:
        x -= 1
    elif direction == "down" and x < size - 1:
        x += 1
    elif direction == "left" and y > 0:
        y -= 1
    elif direction == "right" and y < size - 1:
        y += 1
    else:
        print("Invalid move!")
    return (x, y)

def escape_the_maze():
    print("Welcome to Escape the Maze!")
    size = 5  # Size of the maze (5x5 grid)
    maze, exit_pos = create_maze(size)
    player_pos = (0, 0)  # Player starts at the top-left corner (0, 0)
    
    while player_pos != exit_pos:
        print_maze(maze, player_pos)
        move = input("Enter your move (up, down, left, right): ").lower()
        player_pos = move_player(player_pos, move, size)
    
    print("Congratulations! You've escaped the maze!")

# Run the game
escape_the_maze()
