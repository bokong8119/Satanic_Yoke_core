change_key=[]
answer='' 
search_range={}
search={'A':3,'B':1,'C':2,'D':2}
def create_key(search=search,range_index=5):
#生成凯撒加密解密密钥
    for i in ['A','B','C','D']:
        temp_range=0
        temp=[]
        temp.append(chr(ord(i)+search[i]))
        while temp_range<range_index:
            temp.append(chr(ord(temp[-1])+4))
            temp_range+=1
        search_range[i]=temp
def change_return(answer,key):  #换位加密法反向解密
    temp=['' for k in range(len(answer))]
    for i in range(len(answer)):
        index_temp=(i+key)%len(answer)
        temp[index_temp]=answer[i]
    output_temp=''
    for st in temp:   #列表元素整合
        output_temp+=st
    return output_temp
def change_key_create(answer,time=3):   #换位密钥
    time_temp=0
    while time_temp<time:
        temp=int(input('你想移动几位'))  #从左往右
        if abs(temp)>=len(answer):  #优化
            temp=temp%len(answer)
        time_temp+=1
        change_key.append(temp)
def change_return_all(answer):
    for i in range(len(change_key)-1,-1,-1): #倒过来
        answer=change_return(answer,-(change_key[i])) #有负号
    return answer
def return_judge(answer):  #凯撒加密法反向解密
    temp_all=''
    list_temp=['A','B','C','D']
    for j in range(len(answer)):
        for i in list_temp:
            if answer[j] in search_range[i]:
                temp_all+=i
                break
        else:
            return "答案或密钥有误，请重新输入"
    return temp_all
def unify_all(answer): #格式统一为大写
    temp=''
    for st in answer:
        if 'a'<=st<='z':
            st=chr(ord(st)-97+65)
        temp+=st
    return temp
answer_orignal=input('原本的答案')
answer_orignal=unify_all(answer_orignal)
change_key_create(answer_orignal)
answer=change_return_all(answer_orignal)
create_key(search)
temp=return_judge(answer)
print (temp)
