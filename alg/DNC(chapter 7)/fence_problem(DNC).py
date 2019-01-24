import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


#분할 정복 7.4~7.5 울타리 잘라내기
def init_bar(fence):
    x = []
    y = []
    for i in range(len(fence)):
        x.append(i)
        y.append(fence[i])
    #plt.figure()
    plt.bar(x,fence,width=1.0,color='b')
    #plt.show()
def solve(left, right):
    ##one fence
    if left is right:
        return fence[left]
    middle=int((left+right) /2)
    ##recursive Divice
    result=max(solve(left,middle),solve(middle+1,right))
    low=middle
    high=middle+1
    height=min(fence[low],fence[high])

    ##높이 책정
    result=max(result,height*2)
    while left<low or high<right :
        if high < right and (low is left or fence[low-1] < fence[high+1]) :
            high=high+1
            height=min(height,fence[high])
        else:
            low=low-1
            height=min(height,fence[low])
        result=max(result,height*(high-low+1))
    return result

def animate(i):
    x = []
    y=[]
    for j in range(len(fence)):
        x.append(j)
        y.append(0)

    return plt.bar(x, y, width=1.0, color='r')


fig=plt.figure()
problem_case=input()
for i in range(int(problem_case)):
    num_fence=input()
    high_fence=input()
    fence=high_fence.split(" ")
    fence=list(map(int,fence))
    ans=solve(0,len(fence)-1)
    print(ans)
anim = animation.FuncAnimation(fig, animate, init_func=init_bar(fence), frames=200, interval=1000, blit=True)
plt.show()