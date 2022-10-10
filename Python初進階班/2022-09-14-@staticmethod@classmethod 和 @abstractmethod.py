
'''StaticMethods 靜態方法

class People_StaticMethods:
    def __init__(self):
        pass

    def sleep(self, sleep_hour):
        print('Sleeping hours :', sleep_hour)

    @staticmethod
    def work(work_hour):
        print('Working hours :', work_hour)

m = People_StaticMethods()
m.sleep(3)

People_StaticMethods.work(4)

'''


'''ClassMethods 類方法

class People_ClassMethods:
    def __init__(self):
        pass

    def sleep(self, sleep_hour):
        print('Sleeping hours :', sleep_hour)

    @classmethod
    def work(cls, work_hour):
        print('Working hours :', work_hour)
        cls().sleep(6)


People_ClassMethods.work(5)


class People_StaticMethods:
    def __init__(self):
        pass

    def sleep(self, sleep_hour):
        print('Sleeping hours :', sleep_hour)

    @staticmethod
    def work(work_hour):
        print('Working hours :', work_hour)
        People_StaticMethods.sleep(4)


m = People_StaticMethods()
m.sleep(3)

People_StaticMethods.work(4)
'''

''' AbstractMethods 抽象方法'''

import abc

# Python 3.4+

class Employee(abc.ABC):
    @abc.abstractmethod
    def work(self):
        return NotImplemented


class Andy(Employee):
    def work(self):
        print('work')


class Max(Employee):
    def sleep(self):
        print('sleep')


Andy().work()
Max().sleep()