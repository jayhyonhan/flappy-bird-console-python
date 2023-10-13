import t_matrix, sys, time, keyboard, random # t_matrix is a custom module that creates a matrix type and it makes generating the level much more easier (Read it!)
from os import system, name
width = 100
height = 50
level_background = t_matrix.matrix(width, height, " ")
level = level_background
bird = [25, 20, 0.1] # [y(inverted), x]
jump_pressed = False
pipe = [0, 1] # [height, x]
pipe[0] = random.randint(1, height-height//4)
score = 0
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
while True:
    if pipe[1] <= 1:
        pipe[0] = random.randint(1, height-height//4)
        pipe[1] = width
    else:
        pipe[1] -= 1
    if (jump_pressed == True) and not(keyboard.is_pressed("f")): # press f to jump
        jump_pressed = False
    elif keyboard.is_pressed("f") and not(jump_pressed):
        jump_pressed = True
        bird[2] = -1.3
    bird[0] += bird[2]
    if bird[0]>len(level._mat):
        clear()
        print("Game Over")
        print(f"Score: {score}")
        exit()
    elif bird[0]<=0:
        clear()
        print("Game Over")
        print(f"Score: {score}")
        exit()
    bird[2] += 0.2 # gravity acceleration
    if bird[2] > 1.3:
        bird[2] = 1.3
    level.reset_mat()
    for i in range(0, pipe[0]+1):
        level._mat[i][pipe[1]-1] = "#"
        if pipe[1] > 1:
            level._mat[i][pipe[1]-2] = "#"
        if pipe[1] > 2:
            level._mat[i][pipe[1]-3] = "#"
    for j in range((pipe[0]+height//4), height):
        level._mat[j][pipe[1]-1] = "#"
        if pipe[1] > 1:
            level._mat[j][pipe[1]-2] = "#"
        if pipe[1] > 2:
            level._mat[j][pipe[1]-3] = "#"
    level._mat[int(bird[0])][bird[1]-1] = "B" # "drawing" the bird (yes I am using a B for the bird)
    if (pipe[1]-2) <= bird[1] <= (pipe[1]):
        if pipe[0] >= bird[0]:
            clear()
            print("Game Over")
            print(f"Score: {score}")
            exit()
        elif bird[0] >= (pipe[0]+height//4):
            clear()
            print("Game Over")
            print(f"Score: {score}")
            exit()
    if pipe[1] == bird[1]:
        score += 1
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
    output += f"\n\n{score}"
    sys.stdout.flush()
    time.sleep(0.05)
    clear()
    print(output)
    # replaced with line 33
    #level._mat[int(bird[0])][bird[1]] = " "