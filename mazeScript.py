import time
import os
from random import randint

width = 11
height = 11

maze = []
xy = [1,1]

drawB = True
os.system('mode con lines=50 cols=100')
for i in range(height):
    maze.append('')
    maze[i] = list(['1' for j in range(width)])

maze[1][1] = '0'

def draw (maze):
    time.sleep(0.01)
    #os.system('cls')
    for i in range(len(maze)):
        line = ''
        for j in range(len(maze[i])):                               
            if (maze[i][j] == '1'):
                line += '██'
            elif (maze[i][j] == '0'):
                line += '  '
            elif (maze[i][j] == '2'):
                line += 'OO'
                xy = [i,j]
            elif (maze[i][j] == '3'):
                line += '░░'
        print(line)

def punch(maze, xy, vect):
            if (vect == 0 and maze[xy[0]][xy[1] - 2] != '0'):
                maze[xy[0]][xy[1] - 1] = '0'
                maze[xy[0]][xy[1] - 2] = '0'
                if (drawB):
                    draw(maze)
                
            elif (vect == 1 and maze[xy[0] - 2][xy[1]] != '0'):
                maze[xy[0] - 1][xy[1]] = '0'
                maze[xy[0] - 2][xy[1]] = '0'
                if (drawB):
                    draw(maze)
                
            elif (vect == 2 and maze[xy[0]][xy[1] + 2] != '0'):
                maze[xy[0]][xy[1] + 1] = '0'
                maze[xy[0]][xy[1] + 2] = '0'
                if (drawB):
                    draw(maze)
                
            elif (vect == 3 and maze[xy[0] + 2][xy[1]] != '0'):
                maze[xy[0] + 1][xy[1]] = '0'
                maze[xy[0] + 2][xy[1]] = '0'
                if (drawB):
                    draw(maze)
                
            return maze

while(True):
    for i in range(1, height, 2):
        for j in range(1, width, 2):
            rand = randint(0, 4)
            if (rand == 0 and maze[i][j] == '0' and j != 1):
                maze = punch(maze, [i,j], rand)
                    
            if (rand == 1 and maze[i][j] == '0' and i != 1):
                maze = punch(maze, [i,j], rand)
                    
            if (rand == 2 and maze[i][j] == '0' and j != width - 2):
                maze = punch(maze, [i,j], rand)
                    
            if (rand == 3 and maze[i][j] == '0' and i != height - 2):
                maze = punch(maze, [i,j], rand)

    ext = True
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            if (maze[i][j] == '1' and maze[i - 1][j] == '1' and maze[i][j - 1] == '1' and maze[i + 1][j] == '1' and maze[i][j + 1] == '1' and maze[i][j] == '1' and maze[i - 1][j - 1] == '1' and maze[i + 1][j - 1] == '1' and maze[i - 1][j + 1] == '1' and maze[i + 1][j + 1] == '1'):
                ext = False
    if (ext):
        draw(maze)
        break

# 0
#1+3
# 2
#variables--------------------------------------------------------
d = 0
speed=1
step = 0
esc="no"
xy = [1,1]
maze[width - 2][height - 2] = '3'
#functions--------------------------------------------------------
def busyWay():
    fxy=[0,0]
    if(d==0):fxy=[xy[0]-1,xy[1]]
    elif(d==1):fxy=[xy[0],xy[1]-1]
    elif(d==2):fxy=[xy[0]+1,xy[1]]
    elif(d==3):fxy=[xy[0],xy[1]+1]
    if(maze[fxy[0]][fxy[1]]=='1'):
        print("yes")
        return "yes"
    elif(maze[fxy[0]][fxy[1]]=='3'):
        print("this is the end")
        return "end"
    elif(maze[fxy[0]][fxy[1]]=='0'):
        print("no")
        return "no"
def oneStep(fb):#forward/back
    global maze
    global xy
    step=1
    if(fb=='back'):step=-1
    maze[xy[0]][xy[1]]='0'
    if(d==0):xy = [xy[0]-step,xy[1]]
    if(d==1):xy = [xy[0],xy[1]-step]
    if(d==2):xy = [xy[0]+step,xy[1]]
    if(d==3):xy = [xy[0],xy[1]+step]
    maze[xy[0]][xy[1]]='2'
def turn(side):#direction, side
    global d
    if(side=='right'):
        if(d==0):d=3
        elif(d==1):d=0
        elif(d==2):d=1
        elif(d==3):d=2
    if(side=='left'):
        if(d==0):d=1
        elif(d==1):d=2
        elif(d==2):d=3
        elif(d==3):d=0
#main part--------------------------------------------------------
#os.system('cls')
while(esc=='no'):
    draw(maze)
    print("----------------Debag----------------------")
    if(busyWay()=='no'):oneStep('forward')
    elif(busyWay()=='yes'):
        turn('right')
        oneStep('forward')
        if(busyWay()=='yes'):
            oneStep('back')
            turn('left')
            oneStep('forward')
            if(busyWay()=='yes'):
                oneStep('back')
                turn('left')
    elif(busyWay()==3):esc='yes'
    print("----------------Data-----------------------")
    print("Cords: ["+str(xy[0])+":"+str(xy[1])+"]")
    print("Direction: "+str(d))
    time.sleep(speed)
   # os.system('cls')
    step += 1
print("Steps: "+str(step))
print("You win")




