'''
閏年規則

公元年分非4的倍數，為平年。
公元年分為4的倍數但非100的倍數，为闰年。
公元年分為100的倍數但非400的倍數，为平年。
公元年分為400的倍數為閏年。

'''

year = int( input('請輸入公元年分?(整數)') )

'''
##  方法一
if year % 4 != 0  :
    print(f'{year}年是平年')
elif year % 100 != 0 :
    print(f'{year}年是閏年')
elif year % 400 != 0 :
    print(f'{year}年是平年') 
else :
    print(f'{year}年是閏年')
'''

'''
#  方法二
if (year % 4 != 0) or (year % 4 == 0 and year % 100 == 0 and year % 400 != 0) :
    print(f'{year}年是平年')
else :
    print(f'{year}年是閏年') 
'''

'''
#  方法三
if (year % 4 == 0 and year % 100 != 0) or \
        (year % 4 == 0 and year % 100 == 0 and year % 400 == 0) :
    print(f'{year}年是閏年')
else :
    print(f'{year}年是平年')
'''


#  方法四
if year % 100 == 0 :

    if year % 400 == 0 :

        print(f'{year}年是閏年')

    else :

        print(f'{year}年是平年')

else :

    if year % 4 == 0:

        print(f'{year}年是閏年')

    else :

        print(f'{year}年是平年')