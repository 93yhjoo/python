#레벨 1은 ABC
#레벨 k는 A+(k-1문자열)+B+(k-1문자열)+C이다

memory=dict()
def recursive(argk,memory):
    if argk is 1:
        memory={1:"ABC"}
        return  memory[1]
    else:

        if argk in memory:
            return memory[argk]

        else:
            temp=recursive(argk - 1,memory)
            result = "A" + temp + "B" + temp + "C"
            memory={argk:result}
            return memory[argk]

user=input().split(" ")
k=int(user[0])
s=int(user[1])
t=int(user[2])
text=recursive(k,memory)
print(text[s-1:t])
