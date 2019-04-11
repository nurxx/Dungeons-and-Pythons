from random import randint, choice
import pprint
import sys

def rng(dim):
    map = []
    start_placed = False
    end_placed = False
    start_pos = (0,0)
    end_pos = (0,0)
    for i in range(0,dim):
        row = []
        for j in range(0,dim):
            row.append('#')
            if i == 0 or i == dim-1 or j==0 or j == dim-1:
                if start_placed == False:
                    if randint(0,int(dim*1.5)) == 1:
                        row[j] = 'S'
                        start_placed = True
                        start_pos = (i,j)
                if row[j] != 'S' and start_placed == True and end_placed == False:
                    if randint(0,int(dim*1.5)) == 2:
                        row[j] = 'G'
                        end_pos = (i,j)
                        end_placed = True
            if i ==dim -1 and j == dim -1:
                if start_placed == False:
                    row[j] = 'S'
                    start_pos = (i,j)
                    if end_placed == False:
                        end_pos = (i,1)
                        row[1] = 'G'
                        end_placed = True
                if start_placed == True and end_placed == False:
                    row[1] = 'G'
                    end_pos = (i,1)
                    end_placed = True
        map.append(row)

    maxLength = dim
    maxTurns = dim*4
    end_connect = False
    enemies_placed = False
    pprint.pprint(map)
    
    ex, ey = end_pos[0], end_pos[1]
    print(ex)
    print(ey)
    x, y = start_pos[0], start_pos[1]
    while end_connect == False or enemies_placed == False:
        for i in range(int(maxLength)):
            (dx, dy) = choice([(-1,0),(1,0),(0,1),(0,-1)])
            if x + dx < 0:
                dx = 1
            elif x + dx > dim - 1:
                dx = -1
            if y + dy < 0:
                dy = 1
            elif y + dy > dim - 1:
                dy = -1
                

            x += dx
            y += dy
            if map[x][y] != 'G' and map[x][y] != 'S':
                if randint(0,22) == 1:
                    map[x][y] = 'T'
                elif randint(0,22) == 2:
                    map[x][y] = 'E'
                    enemies_placed = True
                elif x + dx != ex and y + dy != ey and (x==0 or x == dim-1) and (y==0 or y == dim-1):
                    map[x][y] = '#'
                else:
                    map[x][y] = '.'
            elif map[x][y] == 'G':
                end_connect = True
        
    return map

listy = rng(6)


file_name = sys.argv
f = open(file_name[1], 'w')
for line in listy:
    for e in line:
        f.write(str(e))
    f.write('\n')
    
pprint.pprint(listy)
f.close()
