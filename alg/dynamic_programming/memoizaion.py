cache=[[0 for cols in range(0,101)] for rows in range(0,101)]
def matchMemoized(w_pos,s_pos,word):
    ret=cache[w_pos][s_pos]
    if ret != -1: return ret
    while(s_pos<  len(word) and w_pos< len(word) and wild_word[w_pos]=='?' or wild_word[w_pos]==word[s_pos]):
        w_pos+=1
        s_pos+=1
    if w_pos==len(word):
        ret=s_pos
        return ret
    if wild_word[w_pos] == '*':
        for skip in range(0,len(word)):
            if(matchMemoized(w_pos+1,s_pos+skip)):
                ret =1
                return ret
    ret =0
    return ret
def match(w_pos, pos, word):
    try:
        if wild_word[w_pos] is word[pos]:
            if len(wild_word) -1 is w_pos and len(word) -1 is pos :
                print(word)
                return
            w_pos = w_pos + 1
            pos = pos + 1
            match(w_pos, pos, word)
        elif wild_word[w_pos] is '*':
            if len(wild_word) - 1 is w_pos:
                print(word)
                return
            get = word[pos]
            temp = w_pos + 1
            if get is wild_word[temp]:
                w_pos = temp
            else:
                pos = pos + 1
            match(w_pos, pos, word)
        elif wild_word[w_pos] is '?':

            get = word[pos]
            if len(wild_word) - 1 is w_pos:
                print(word)
                return
            w_pos = w_pos + 1
            pos = pos + 1
            match(w_pos, pos, word)
        else:
            return
    except IndexError:
        return



def match_start(word):
    check=False
    pos=0
    wild_word_position=0
    check=match(0,0,word)


case=int(input())
for i in range(0,case):
    wild_word=input()
    word_num=int(input())
    list=[]
    for j in range(0,word_num):
        list.append(input())
    for j in range(0,word_num):
        match_start(list[j])
