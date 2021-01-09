"""
km= float(input("公里數"))
v1=100
v1=100+ (km-1)*30
print(v1)
"""
"""
age=int(input("年齡:"))
if(age>=18):
    print("已成年")
else:
    print("未成年")
"""

#if(運算):
    #要執行的項目
"""
pwd=input("密碼:")
if(pwd=="1234"):
    print("登入成功")
else:
    print("登入失敗")
"""
"""
#分別輸入國英數並取得平均成績
#若平均>=80,可出國
v1=int(input("國文:"))
v2=int(input("英文:"))
v3=int(input("數學:"))
avg=(v1+v2+v3)/3
if(avg>=80):
    print("符合條件")
else:
    print("不符合")
"""
"""
#華氏=攝氏*(9/5)+32
#攝氏=(華氏-32)*5/9
a=input("輸入大寫C或F並按下enter")
if(a=="C"):
    C=input("請輸入攝氏溫度")
    calc=float(C)*(9/5)+32
    print("您輸入的攝氏溫度為{},換算成華氏為{}".format(C,calc))
else:
    F=input("請輸入華氏溫度")
    calc=(float(F)-32)*5/9
    print("您輸入的華氏溫度為{},換算成攝氏溫度為{}".format(F, calc))
"""
"""
i=input("輸入C或F並按下enter")
if(i.upper()=="C"):
    f=float(input("請輸入華氏溫度:"))
    c=(f-32)*5/9
    print(f"您輸入的華氏溫度為{f},換算成攝氏溫度為{c}")
elif i.upper()=="F":
    c=float(input("請輸入攝氏溫度"))
    f=c*(9/5)+32
    print(f"您輸入的攝氏溫度為{c},換算成華氏溫度為{f}")
else:
    print("輸入錯誤")
"""
'''
#conda list random / pip list random 先查詢是否有安裝此套件
#conda install random / pip install random安裝套件
#取得隨機亂數random
import random as r #3.導入random工具組, 並命名為r
#4設定49個連續號
lotto=range(1,50)
#利用r.sample函數隨機取得lotto中6個"不"重複的號碼
print(r. sample(lotto,6))
'''
''''
#range(...)#流水號
x=["apple","banana","orange","cherry"]
y=[88,90,95]
z=range(1,50)
for j in x:
    if(j=="cherry"):
     print(y[2])
'''
'''
x=[66,75,21,35,45,12,15,63,58,74]
no=3
for j in x:
     print(j,no)
     no+=2
'''
'''
sum=0
i=1
while i <=3: #1.2.3
    sum += i 
    i +=1
print("sum:",sum,"i:",i)
#print("sum:", sum)
'''
sum=0
for i in range(3): 
    sum += i
print("sum:",sum, "i:", i)
 




    
