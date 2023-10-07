# If and For Fuctions
cities = ['New York', 'Washington', 'Miami', 'Tehran']
if cities[0] == 'Tehran':
    print("Tehran is the first city")
else:
    print("Bummer!")
for city in cities:
    print(city)
print('Done!')

# Iterate over a dictionary
dictionary = {
    'New York' : 'Big',
    'Tehran' : 'Big',
    'Providence' : 'Small'
}
for key, value in dictionary.items():
    print("This city is {} and it is {}".format(key, value))

