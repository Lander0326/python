'''

買電影票要付多少錢的問題?

1. 5 歲以下(不含 5 歲)的人不用錢
2. 學生可以買學生票 80 元
3. 5 歲 到 18 歲(不含 18 歲)之間的人可以買優待票 100 元
4. 18 歲以上買成人票 120 元

'''

age = int( input('請輸入年齡?(1-100之間的整數)') )
student = input('你是不是學生?(yes/no)')

if isinstance(age,int) and 1 <= age <= 100 and ( student == 'yes' or student == 'no'):

    print(f"年齡:{age}歲，學生-->{student}")

    if age < 5:
        print('不用錢')
    elif student == 'yes' :
        print('80元')
    elif 5 <= age < 18 :
        print('100元')
    else :
        print('120元')

else :

    print("資料輸入錯誤")

