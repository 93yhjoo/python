def move(x,y,current_dic,count):
    if(current_dic=='right'):
        y+=1
    elif(current_dic=='left'):
        y-=1
    elif(current_dic=='up'):
        x-=1
    elif(current_dic=='down'):
        x+=1

    count += 1
    if(x == -1 or y == -1) or (x>=int(dimension[0]) or y>=int(dimension[1])):
        print(count)
    else:
        matching(x, y, current_dic, count)

def matching(x,y,current_direction,count):
        if (current_direction == 'right' and row[x][y] == '\\') or (current_direction == 'left' and row[x][y] == '/'):
            current_direction = "down"

        elif (current_direction == 'right' and row[x][y] == '/') or (current_direction == 'left' and row[x][y] == '\\'):
            current_direction = "up"

        elif (current_direction == 'up' and row[x][y] == '/') or (current_direction == 'down' and row[x][y] == '\\'):
            current_direction = "right"

        elif (current_direction == 'down' and row[x][y] == '/') or (current_direction == 'up' and row[x][y] == '\\'):
            current_direction = "left"

        move(x, y, current_direction, count)



box_dimension=input()
dimension=box_dimension.split(" ")
row=[]
for i in range(0,int(dimension[0])):
    temp=input()
    row.append(temp)
count=0
current_direction="right"
matching(0, 0, current_direction, count)