# with open('weather_data.csv') as file:
#     data = file.readlines()
#     print(data)

# import csv
#
# with open('weather_data.csv') as file:
#     reader = csv.reader(file)
#     temperatures = []
#     for row in reader:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv('weather_data.csv')
# print(data)
print(data['temp'])
