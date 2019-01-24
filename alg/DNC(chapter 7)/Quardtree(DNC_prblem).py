#분할 정복 7.2~7.3 쿼드 트리
# 입력된 쿼드 트리를 상하로 뒤집고 다시 퀴드 트리로 압축하여 출력하여라.

#방법1 주어진 쿼드 트리를 상하로 뒤집고 다시 퀴드 트리로 압축한다.
#방법2 DNC를 사용해 분할 정복 한다.


MAX_size=32
Matrix=[['w']*MAX_size for i in range(MAX_size)]
#재귀 함수를 통해 퀴드 트리 압축 해제....size를 통해 배열의 이동 크기 제어
def decompressed(it,y,x,size):
    character=next(it)
    if(character=='b' or character=='w'):
        for dy in range(size):
            for dx in range(size):
                Matrix[y+dy][x+dx]=character
    #character가 'x'인 경우.
    else:
        #압축 deep하게 들어가서 압축을 해제한다.
        half=size//2
        decompressed(it,y,x,half)
        decompressed(it,y,x+half,half)
        decompressed(it,y+half,x,half)
        decompressed(it,y+half,x+half,half)

#압축해제 후 상하반전 다시 압축 이렇게 하는 것보다
#규칙을 찾아 상하반전을 한 후 압축하는 편이 더 좋기에 reverse 재귀함수를 사용하자.
def reverse(it):
    character=next(it)
    #단일 색일 경우
    if character=='b' or character=='w':
        return character
    else:
        upperLeft=reverse(it)
        upperRight=reverse(it)
        lowerLeft=reverse(it)
        lowerRight=reverse(it)
        return 'x'+lowerLeft+lowerRight+upperLeft+upperRight


case = int(input())
count=0
for i in range(case):
    text=input()
    it2 = iter(text)
    new_string=reverse(it2)
    it=iter(new_string)
    decompressed(it,0,0,MAX_size)
    print(new_string)
for y in range(MAX_size):
    for x in range(MAX_size):
        print(Matrix[y][x],end='')
    print()

