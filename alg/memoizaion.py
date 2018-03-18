def match(wild_word,word):
    pos=0
    while len(word) >pos and len(wild_word) > pos and (wild_word[pos] == '?' or wild_word[pos] == word[pos]):
        pos+=1


case=int(input())
for i in range(0,case):
    wild_word=input()
    word_num=int(input())
    list=[]
    for j in range(0,word_num):
        list.append(input())
        wild_word.find()