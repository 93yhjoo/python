def partialsum(array):
    temp=[array[0]]*len(array)
    for i in range(1,len(array)):
        temp[i]=int(temp[i-1])+int(array[i])
    return temp


case = int(input())
count=0
for i in range(case):
    str=input().split(' ')
    box_num=str[0]
    child_num=str[1]
    #박스안에 있는 인형들의 갯수
    box_include=input().split(" ")

    #분할 집합 구현
    psum=partialsum(box_include)

    for standard in range(len(psum)):
        for move in range(standard,len(psum)):
            temp=0
            point=standard-1
            if point<0:
                temp=int(psum[move])%int(str[1])
            else:
                temp = (int(psum[move])-int(psum[point]))%int(str[1])
            if temp == 0:
                count+=1


print(count)


