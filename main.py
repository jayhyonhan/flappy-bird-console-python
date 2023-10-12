import t_matrix, sys, time, keyboard
from os import system, name
width = 100
height = 50
level_background = t_matrix.matrix(width, height, " ")
level = level_background
bird = [25, 10, 0.1] # [y(inverted), x]
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
while True:
    if keyboard.is_pressed(" "):
        bird[2] = -1
    bird[0] += bird[2]
    if bird[0]>len(level._mat):
        clear()
        print("Game Over")
        exit()
    elif bird[0]<=0:
        clear()
        print("Game Over")
        exit()
    bird[2] += 0.1 # gravity acceleration
    if bird[2] > 1:
        bird[2] = 1
    level.reset_mat()
    level._mat[int(bird[0])][bird[1]] = "B"
    output = ""
    for i in range(level.h+2):
        if i == 0:
            output += "# " * (level.w+2)
        elif i == level.h+1:
            output += "# " * (level.w+2)
        else:
            for j in range(level.w+2):
                if j==0:
                    output += "# "
                elif j==level.w+1:
                    output += "#"
                else:
                    output += str(level._mat[i-1][j-1])
                    if j < level.w+1:
                        output += " "
        if i < level.h+1:
            output += "\n"
    sys.stdout.flush()
    time.sleep(0.025)
    clear()
    print(output)
    #level._mat[int(bird[0])][bird[1]] = " "