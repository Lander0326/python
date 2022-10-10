
'''

class Employee:
    def __init__(self):
        self.working_hour = 0 #屬性

    def work(self): #方法
        self.working_hour += 1
        print('Working:', self.working_hour)

andy = Employee()  # 類的實例化
andy.work() # 呼叫類的方法
print(andy.working_hour) # 呼叫類的屬性

'''

'''定義屬性的三種方法

class ThisTestClass:
    getName = 'Max'  #方法一：把屬性定義寫在init外面

    def __init__(self):
        self.getNameFromInit = 'Max__init__'  #方法二：把屬性定義寫在init內
        pass


if __name__ == "__main__":

    task = ThisTestClass()
    task.sendName = 'Max_sendName'  ##方法三：自己給屬性與參數

    print(task.getName)
    print(task.getNameFromInit)
    print(task.sendName)

'''

'''繼承

class Employee:
    def __init__(self):
        self.cut_tree = 3

class Andy(Employee):
    def __init__(self, get_gold):
        super().__init__()
        self.get_gold = get_gold

    def getDetails(self):
        print('==getDetails==')
        print('tree:', self.cut_tree)
        print('gold:', self.get_gold)


if __name__ == "__main__":
    andy = Andy(1)
    andy.getDetails()

'''


'''封裝

class Employee:
    def __init__(self):
        self.cut_tree = 3
        self.__myName = 'Suyu'
    def work(self):
        print('Working')
        self.__sleep()
    def __sleep(self):
        print('Sleeping')


if __name__ == "__main__":
    andy = Employee()
    andy.work()
    # andy.__sleep()
    print(andy.__myName)

'''


'''多型
class 員工:
    def work(self):
        print('員工 在工作')

class 孟芳(員工):
    def work(self):
        print('孟芳 在工作')

class 家翊(員工):
    def work(self):
        print('家翊 在工作')

# 家翊1 = 家翊()
# 家翊2 = 家翊()
# 家翊3 = 家翊()
#
# 家翊.work()
#
# 員工1 = 員工()
#
# 員工1.work()


list1 = [家翊(), 孟芳(), 孟芳(),家翊(),員工()]
for item in list1 :
    item.work()

'''