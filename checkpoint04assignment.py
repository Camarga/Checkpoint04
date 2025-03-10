import math

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
media_of_cost = 6.987869
#dicctionary
city = {
  'name' : 'Vitoria',
  'population' : '260000',
  'location' : 'north of Spain',
}

#Exercise 2
temperature = 37.8
print(int(temperature))

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
sea = list(sea)
sea.append('Yelow Sea')
sea = tuple(sea)
print(sea)