
'''Property 特性一'''
'''
class Bank_acount:

    @property
    def password(self):
        return '密碼:123'

andy = Bank_acount()

print(andy.password)

#andy.password = '密碼:456'

'''

'''Property 特性二'''
'''

class Bank_acount:
    def __init__(self):
        self._password = '預設密碼 0000'

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @password.deleter
    def password(self):
        del self._password
        print('del complite')

andy = Bank_acount()
andy.password='1234'
del andy.password

print(andy.password)

'''


'''@property 的實際應用場景'''
''''''

from werkzeug.security import generate_password_hash, check_password_hash

class User:
    @property
    def password(self):
        raise AttributeError('password is not readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

andy = User()
andy.password = '1234'
print(andy.password_hash)
print(andy.verify_password('1234'))
print(andy.verify_password('5678'))