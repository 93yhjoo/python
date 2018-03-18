"""재귀함수 사용하기"""

def hasWord(x,y,argstart,word):
    flag=False
    dx=[-1,-1,-1,0,0,1,1,1]
    dy=[-1,0,1,-1,1,-1,0,1]
    """구현 사항: PRETTY 일 경우 R 접근 경로 2가지"""

    """마지막 문자까지 검색하여 다시 재귀해서 들어왔을 시 탈출"""
    if(argstart>=len(word)):
        flag=True
    else:
        for d in range(len(dx)):
            xi=x+dx[d]
            yi=y+dy[d]
            try:
                if(xi>= 0 and yi >= 0):
                    if(li[xi][yi]==word[argstart:argstart+1]):
                        stack.append([xi,yi])
                        flag=True
                        hasWord(xi,yi,argstart+1,word)
                        break
                else:
                    continue
            except IndexError as e:
                continue
        if flag == False:
            stack.clear()




li = [['U','R','L','P','M'],['X','P','R','E','T'],['G','I','A','E','T'],['X','T','N','Z','Y'],['X','O','Q','R','S']]

stack=[]
start=1
usr=str(input())
for x in range(len(li)):
    if(len(usr) == 1):
        try:
            y=li[x].index(usr)
            stack.append([x,y])
        except ValueError as e:
            continue
    else:
        try:
            y = li[x].index(usr[:start])
            stack.append([x, y])
            hasWord(x,y,start,usr)
        except ValueError as e:
            continue


if(len(stack)==0):
    print("존재 하지 않습니다")
else:
    print(stack)