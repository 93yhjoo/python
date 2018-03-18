import math
import queue
import time
#소인수 분해 알고리즘.
start_time = time.time()
def factorization(n):
    q1=queue.Queue()
    sqrtn=int(math.sqrt(n))
    for div in range(2,sqrtn+1):
        while n%div == 0:
            n//=div
            q1.put(div)
    if n>1:
        q1.put(n)
    return q1


'''
number =int(input())
q=factorization(number)
for i in range(q.qsize()):
    print(q.get())
'''
'''
#시간적 소모가 엄청나다. n*m*(L1+L2)의 시간과 숫자의 범위가 많아 지면 더 오래 걸린다(f(X)+A만큼 걸림).120sec
case=int(input())
answer=case
for count in range(case):
    #배열 0=>약수의 개수, 1=>시작 범위,2=> 종결범위 양 끝 범위 숫자 포함
    output=0
    array = input().split(" ")
    for i in range(int(array[1]),int(array[2])+1):
        temp_q=factorization(i)
        #소인수 분해된 숫자로 통해 약수 구하기.
        pre_num=0
        current=0
        list = [0]
        for roop in range(temp_q.qsize()):
            #첫 순회시
            if pre_num==0:
                pre_num = temp_q.get()
                list[current] = list[current] + 1
            #첫 순회 이후로.
            else:
                current_num=temp_q.get()
                if pre_num==current_num:
                    list[current] =list[current]+1
                else:
                    list.append(1)
                    current+=1
                    pre_num = current_num
        total=1
        for check in range(len(list)):
            get=list[check]+1
            total*=get
        if total==int(array[0]):
            output+=1
    print(output)
'''

minFactor=list()
def eratosthenes2(n):
    minFactor.append(-1)
    minFactor.append(-1)
    for i in range(2,n+1):
        minFactor.append(i)
    sqrtn=int(math.sqrt(n))
    for i in range(2,sqrtn+1):
        if minFactor[i] == i :
            j=i*i
            while j <= n:
                if minFactor[j]==j:
                    minFactor[j]=i
                j+=i
def factor(n):
    q1=queue.Queue()
    while n > 1:
        q1.put(minFactor[n])
        n//=minFactor[n]
    return q1


'''
eratosthenes2(50)
number =int(input())
q=factor(number)
for i in range(q.qsize()):
    print(q.get())
'''
'''
#30sec
case=int(input())
answer=case
for count in range(case):
    #배열 0=>약수의 개수, 1=>시작 범위,2=> 종결범위 양 끝 범위 숫자 포함
    output=0
    array = input().split(" ")
    #가장 큰 수 범위 까지의 체거르기
    eratosthenes2(int(array[2]))
    for i in range(int(array[1]),int(array[2])+1):
        temp_q=factor(i)
        #소인수 분해된 숫자로 통해 약수 구하기.
        pre_num=0
        current=0
        list = [0]
        for roop in range(temp_q.qsize()):
            #첫 순회시
            if pre_num==0:
                pre_num = temp_q.get()
                list[current] = list[current] + 1
            #첫 순회 이후로.
            else:
                current_num=temp_q.get()
                if pre_num==current_num:
                    list[current] =list[current]+1
                else:
                    list.append(1)
                    current+=1
                    pre_num = current_num
        total=1
        for check in range(len(list)):
            get=list[check]+1
            total*=get
        if total==int(array[0]):
            output+=1
    print(output)
'''

#주어진 숫자의 가장 작은 소인수를 찾고
#소인수 분해에서  이 숫자가 몇 번이나 출현하는지 모두 계산
#만일 n(주어진 숫자)의 가장 작은 소인수가 p이고 이 소인수가 a번 출현하면
TM=1000*1000*10
eratosthenes2(TM)
minFactorPower=[0]*(TM+1)
Factors=[0]*(TM+1)
#11sec
def getFactorSmart():
    minFactor[1]=1
    for n in range(2,TM+1):
        if minFactor[n]==n:
            minFactorPower[n]=1
            Factors[n]=2
        else:
            p=minFactor[n]
            m=int(n/p)
            if p != minFactor[m]:
                minFactorPower[n] = 1

            else:
                minFactorPower[n]=minFactorPower[m]+1
            a=minFactorPower[n]
            Factors[n]=(int(Factors[m]/a))*(a+1)

getFactorSmart()

case=int(input())
answer=case
for count in range(case):
    output = 0
    array = input().split(" ")
    for i in range(int(array[1]), int(array[2]) + 1):
        if Factors[i] == int(array[0]):
            output+=1
print(output)
print("--- %s seconds ---" %(time.time() - start_time))