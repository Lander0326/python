def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries <= 0:
            raise ValueError('invalid user response')
        print(reminder)

# ask_ok('請輸入英文 ： ','再來一次') # 邏輯錯誤
ans = ask_ok(prompt='請輸入英文 ： ',reminder='再來一次',retries=2) # 參數寫清楚可不對位置

if ans :
    print('答對了')
else :
    print('答錯了')