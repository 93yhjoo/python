def balance(amount,duration,rates,monthlyPayment):
    balance=amount
    for i in range(0,duration):
        balance*=(1+(rates/12.0)/100.0)
        balance-=monthlyPayment

    return balance
def payment(amount,duration,rates):
    low=0
    high=amount*(1+(rates/12.0)/100.0)
    for iterater in range(0,100):
        mid=(low+high)/2.0
        if(balance(amount,duration,rates,mid)<=0):
            high=mid
        else:
            low=mid
    return high

def score(count,win):
    get= win*100 // count
    return get
def bisection_function(lower,higher):
    mid = (lower + higher) / 2
    if (lower + 1 < mid):
        higer = mid
    else:
        lower=mid
Max=2000000000

case=int(input())
for i in range(0,case):
    str=input().split(' ')
    lower=int(str[0])
    lower_score=score(int(str[0]),int(str[1]))
    Max_win=Max-int(str[0])+int(str[1])
    higher_score=score(Max,Max_win)
    if(higher_score<=lower_score):
        print(-1)
    else:
        #만일 최저점~최고점의 차이가 1미만이면 중료,
        while lower+1<Max:
            mid=(lower+Max)//2
            mid_win = mid - int(str[0]) + int(str[1])
            mid_score = score(mid, mid_win)
            if lower_score == mid_score:
                lower=mid
            else:
                Max=mid
        print(Max-int(str[0]))
        '''
        #이분법
        while True:
            #A~B사이의 중간지점에서의 승률 찾기.
            mid=(lower+Max)//2
            mid_win = mid - int(str[0]) + int(str[1])
            mid_score=score(mid,mid_win)
            #만일 최저점~최고점의 차이가 1미만이면 중료,
            if lower+1<Max:
                print(mid-int(str[0]))
                break
            else:
                if lower_score == mid_score:
                    lower=mid
                    
                else:
                    Max=mid
        '''