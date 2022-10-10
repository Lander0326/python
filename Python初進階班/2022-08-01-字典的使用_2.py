
'''
car1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "color": "White"
}

car2 = {
  "brand": "KIA",
  "model": "SUV",
  "year": 2022
}
car1.update(car2)

print(car1)
'''

car1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "color": "White"
}

car2 = {
  "brand": "KIA",
  "model": "SUV",
  "year": 2022
}

x = car1.pop('sex','沒有這個key')

print(car1)
print(x)