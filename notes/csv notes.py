import csv

# with open('weather_data.csv', 'r') as weather_data:
#     weather_data_list = weather_data.readlines()
#
# print(weather_data_list)
#
# with open('weather_data.csv', 'r') as weather_data:
#     data = csv.reader(weather_data)
#     temps = []
#     for row in data:
#         if row[1] != 'temp':
#             temps.append(int(row[1]))
#     print(temps)

import pandas

data = pandas.read_csv('weather_data.csv')
print(data)
temp = data['temp']
print(temp)

data_dict = data.to_dict()
print(data_dict)

print(temp.max())
# can also do data.condition, or data.temperature

# Get data in row

monday = data[data.day == 'Monday']
print(data[data.temp == temp.max()])
print(monday.condition)

# Create dataframe from scratch
data_dict = {
    'students': ['Amy', 'James', 'Shivam'],
    'grades': [545, 234, 123]

}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv('student-info.csv')
