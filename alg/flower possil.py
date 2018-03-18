'''
        입력의 첫줄에는 테스트 케이스의 수 50이하
        각 테스트 케이스는 세줄로 주어진다.
        첫 줄에는 두 볼록 껍질에 포함된 점의 수 n , m 1~100사이
        다음 줄에는 2n개의 실수로 첫 볼록 껍질에 포함된 점의 좌표(x,y)가 시계 반대 방향 순서대로 주어짐
        그 다음줄에는 2m개의 실수로 첫 볼록 껍질에 포함된 점의 좌표(x,y)가 시계 반대 방향 순서대로 주어짐
        각 좌표는 [0.100]범위의 실수로 소수점 밑 최대 두자리 까지만 주어짐.
        1
        5 5
        35.74 35.85 69.64 50.00 73.52 82.55 43.50 92.22 17.67 76.18
        16.47 8.02 60.98 14.62 66.80 37.74 45.89 67.22 13.04 55.19
'''
import matplotlib.pyplot as plt
import numpy as np

class argx:
    def __init__(self,x,y):
        self.x = x
        self.y = y
'''배열'''
def decompose(objarr):
    size_array=len(objarr)
    for i in range(0,size_array-1):
        if objarr[i].x < objarr[i+1].x:
            tuple = [objarr[i],objarr[i+1]]
            lower.append(tuple)
        elif objarr[i].x > objarr[i+1].x:
            tuple = [objarr[i], objarr[i+1]]
            upper.append(tuple)
'''a_x값,b_x값 , x '''
def between(a, b, x):
    return ((a.x <= x and x <= b.x ) or (b.x <= x and x <= a.x))

def at(a,b,x):
    dy=b.y-a.y
    dx=b.x-a.x
    result=float(a.y)+float(dy)*(x-a.x)/float(dx)
    return result

def vertical(x):
    minUp=float(1e20)
    maxLow=float(-1e20)

    for i in range(0, len(upper)):
        if(between(upper[i][0], upper[i][1], x)):
            minUp=min([minUp, at(upper[i][0], upper[i][1], x)])
    for i in range(0,len(lower)):
        if(between(lower[i][0],lower[i][1],x)):
            maxLow=max([maxLow,at(lower[i][0],lower[i][1],x)])
    return  minUp-maxLow

lower=[]
upper=[]
first_array=[]
second_array=[]
xi_array1=[]
xi_array2=[]
size=0

scale=int(input())

while(size<scale):
    case=input().split(" ")

    divice1 = input().split(" ")
    divice2 = input().split(" ")
    for i in range(0,int(case[0])*2):
       temp=divice1[i].split(".")
       tem = argx(int(temp[0]), int(temp[1]))
       xi_array1.append(int(temp[0]))
       first_array.append(tem)
    for i in range(0,int(case[1])*2):
        temp= divice2[i].split(".")
        tem = argx(int(temp[0]), int(temp[1]))
        xi_array2.append(int(temp[0]))
        second_array.append(tem)
    size=size+1

decompose(first_array)
decompose(second_array)
'''수직선이 두 다각형을 모두 만나는 x좌표의 범위를 구한다.'''
lo=float(max([min(xi_array1),min(xi_array2)]))
hi=float(min([max(xi_array1),max(xi_array2)]))
print(lo)
print(hi)
if hi < lo :
   print("0")
else:

    for i in range(0,20):
        aab=(lo*2+hi)/3.0
        abb=(lo+hi*2)/3.0
        if vertical(aab) < vertical(abb):
            lo=aab
        else:
            hi=abb
    print(max(0.0,vertical(hi)))


'''
print(vertical(20))
plt.scatter([x_array],[y_array],marker='*')
plt.scatter([xi_array],[yi_array],marker='+')
plt.show()
'''
