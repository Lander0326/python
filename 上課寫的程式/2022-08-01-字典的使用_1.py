# create a dictionary using curly brackets called john that stores name, phone, email, course and address
john = {'name': 'John', 'phone': 1234567890, 'email': 'john.doe@gmail.com', 'course': 'Python v3', 'address': '123 Front St City Country'}
print(john)

# create a dictionary using dict() called adam that stores name, phone, email, course
adam1 = dict(  [  ['name','Adam']  , ['phone',1234567890]  ]  )
print(adam1)

# 動態新增

adam = {}
adam['name']='Adam'
adam["phone"]=1234567890
print(adam)

john['address'] = None
print(john)

john.pop('address')

#print(john['sex'])
print(john.get('sex'))
print(john)

print(john.setdefault('sex'))
print(john)



def func1(x,y):
    return None

class 男人():
    pass