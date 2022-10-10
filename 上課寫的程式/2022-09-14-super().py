'''

class Animal(object):
    def __init__(self, animal_type):
        print('Animal Type:', animal_type)


class Mammal(Animal):
    def __init__(self):
        # call superclass
        super().__init__('Mammal')
        print('Mammals give birth directly')


dog = Mammal()

# Output: Animal Type: Mammal
#         Mammals give birth directly

'''

'''

class Mammal(object):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')


class Dog(Mammal):
    def __init__(self):
        print('Dog has four legs.')
        super().__init__('Dog')


d1 = Dog()



''''''

# changing base class to CanidaeFamily
class Dog(CanidaeFamily):
  def __init__(self):
    print('Dog has four legs.')

    # no need to change this
    super().__init__('Dog')
    
'''

'''多重繼承


class Animal:
    def __init__(self, Animal):
        print(Animal, 'is an animal.');


class Mammal(Animal):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')
        super().__init__(mammalName)


class NonWingedMammal(Mammal):
    def __init__(self, NonWingedMammal):
        print(NonWingedMammal, "can't fly.")
        super().__init__(NonWingedMammal)


class NonMarineMammal(Mammal):
    def __init__(self, NonMarineMammal):
        print(NonMarineMammal, "can't swim.")
        super().__init__(NonMarineMammal)


class Dog(NonMarineMammal, NonWingedMammal):
    def __init__(self):
        print('Dog has 4 legs.');
        super().__init__('Dog')


d = Dog()
print('')
bat = NonMarineMammal('Bat')

# Dog has 4 legs.
# Dog can't swim.
# Dog can't fly.
# Dog is a warm-blooded animal.
# Dog is an animal.
# 
# Bat can't swim.
# Bat is a warm-blooded animal.
# Bat is an animal.
'''