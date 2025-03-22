from random import randint
search={'A':3,'B':1,'C':2,'D':2} #凯撒加密基本位移量
key=[] #单个字符的凯撒加密密钥
change_key_list=[] #换位加密密钥
def key_create(answer):  #每个答案生成专属的密钥
    for i in answer:
        temp_key=search[i]+4*randint(0,5) #（恶魔微笑）
        key.append(temp_key)
def encrypt(answer):  #凯撒加密
    index_answer=0
    temp_all=''
    for i in answer:
        temp_only=chr((((ord(i)-65)+key[index_answer])%26)+65)
        temp_all+=temp_only
        index_answer+=1
    return temp_all
def change_encrypt(answer,key):  #换位加密
    temp=['' for k in range(len(answer))]
    for i in range(len(answer)):
        index_temp=(i+key)%len(answer)
        temp[index_temp]=answer[i]
    output_temp=''
    for st in temp:   #列表元素整合
        output_temp+=st
    return output_temp
def unify_all(answer): #格式统一为大写
    temp=''
    for st in answer:
        if 'a'<=st<='z':
            st=chr(ord(st)-97+65)
        temp+=st
    return temp
def change_key_create(answer,time=3):   #换位加密密钥生成，time表示循环几次，time值课更改
    time_temp=0
    while time_temp<time:
        temp=int(input('你想移动几位'))
        if abs(temp)>=len(answer):  #优化
            temp=temp%len(answer)
        time_temp+=1
        change_key_list.append(temp)
def check(answer):  #确保答案只有ABCD
    check_list=['A','B','C','D','a','b','c','d']
    temp=''
    for st in answer:
        if st in check_list:
            temp+=st
    return temp
answer_orignal=input('原本的答案')
answer_orignal=unify_all(check(answer_orignal))  #排除干扰，以免影响后面的加密
key_create(answer_orignal)
change_key_create(answer_orignal)
answer_temp=encrypt(answer_orignal)
for i in range(len(change_key_list)): #换位重复加密，密钥采用换位加密密钥生成的全部密钥
    answer_temp=change_encrypt(answer_temp,change_key_list[i])
print(answer_temp)
#以下部分可以删除或者注释掉
print(key) #显示凯撒加密密钥
print(answer_orignal) #显示优化后的原答案
print(change_key_list) #显示换位加密的密钥
