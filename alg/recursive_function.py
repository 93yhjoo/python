def check(move,n):
    for i in range(1,20):
        value=(i - 0.5) * pow(2, n)
        if move is int(value): return i
        elif move < value: return False

def moving(spin ,n):
    total=spin+n
    if(total%2 is 0):
        return "back"
    else:
        return "front"
def recursive(t,n,d,move):
    rule=(d - 0.5) * pow(2, n)
    if move is int(rule):
        moving(spin,n)
        print(dimension.index(int(n)))
        if move ==t:
            return print("end")
        move = move + 1
        recursive(t,1,1,move)
    else:
        confirm=check(move,n)
        if confirm is False:
            n=n+1
            recursive(t,n,d,move)
        else:
            recursive(t, n, confirm, move)
user_dimension=input()
get=user_dimension.split(" ")
spin=int(get[0])
time=int(get[1])
dimension=[0]*15
for j in range(spin):
    dimension[15-3*(j+1)]=spin-j

print(dimension)
recursive(time,1.0,1.0,1)

print(dimension)