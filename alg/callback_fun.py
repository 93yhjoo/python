"""재귀함수 사용하기"""

def hasWord(x,y,argstart,word):
    dx=[-1,-1,-1,0,0,1,1,1]
    dy=[-1,0,1,-1,1,-1,0,1]
    for d in range(0,7):
        xi=dx[d]+x
        yi=dy[d]+y
        if xi < 0 or yi < 0:
            continue
        try:
            alpha=li[xi][yi]
            if alpha is word[argstart]:

                argstart=1+argstart
                if argstart is len(word):
                    print('{}을 찾았습니다.'.format(usr))
                    return True
                hasWord(xi,yi,argstart,word)

        except IndexError:
                continue






li = [['U','R','L','P','M'],['X','P','R','E','T'],['G','I','A','E','T'],['X','T','N','Z','Y'],['X','O','Q','R','S']]

check=False
usr=str(input())
for row in range(0,5):
    try:
        col=li[row].index(usr[0])
        if len(usr) > 1:
            check=hasWord(row,col,1,usr)
        else:
            print('{}을 찾았습니다.'.format(usr))
    except ValueError:
        if row is 4 and check is False:
            print('{}찾지 못했습니다.'.format(usr))
        continue
