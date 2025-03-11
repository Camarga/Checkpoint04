import math
from decimal import Decimal

#Exercise 1
#list
capital = ['London', 'Paris', 'Roma', 'Bruselas']
#tuple
sea = ('Mediterranean Sea', 'Caribean Sea', 'Red Sea')
#float
temperature = 37.8
#integer
users = 48
#decimal
num_one = Decimal(20.6)
num_two = Decimal(6.6)
result = num_one / num_two
print(result)
#dicctionary
city = {
  'name' : 'Vitoria',
  'population' : '260000',
  'location' : 'north of Spain',
}

#Exercise 2
temperature = 37.8
print(math.ceil(temperature))

#Exercise 3
temperature = 37.8
print(math.sqrt(temperature))

#Exercise 4
print(city['name'])

#Exercise 5
print(sea[1])

#Exercise 6
capital.append('Madrid')
print(capital)

#Exercise 7
capital = ['London', 'Paris', 'Roma', 'Bruselas']
capital[1] = 'Madrid'
print(capital)

#Exercise 8
capital.sort()
print(capital)

#Exercise 9
sea = ('Mediterranean Sea', 'Caribean Sea', 'Red Sea')
sea += ('Yelow Sea',)
print(sea)