def match(w_pos,pos,w_word,word):
    try:
        if w_word[w_pos] is word[pos]:
            if len(w_word) -1 is w_pos and len(word) -1 is pos :
                print(word)
                return
            w_pos = w_pos + 1
            pos = pos + 1
            match(w_pos, pos, w_word, word)
        elif w_word[w_pos] is '*':
            if len(w_word) - 1 is w_pos:
                print(word)
                return
            get = word[pos]
            temp = w_pos + 1
            if get is w_word[temp]:
                w_pos = temp
            else:
                pos = pos + 1
            match(w_pos, pos, w_word, word)
        elif w_word[w_pos] is '?':

            get = word[pos]
            if len(w_word) - 1 is w_pos:
                print(word)
                return
            w_pos = w_pos + 1
            pos = pos + 1
            match(w_pos, pos, w_word, word)
        else:
            return
    except IndexError:
        return



def match_start(wild_word,word):
    check=False
    pos=0
    wild_word_position=0
    check=match(0,0,wild_word,word)



case=int(input())
for i in range(0,case):
    wild_word=input()
    word_num=int(input())
    list=[]
    for j in range(0,word_num):
        list.append(input())
    for j in range(0,word_num):
        match_start(wild_word,list[j])