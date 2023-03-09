import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

data_to_get = ['Gray', 'Cinnamon', 'Black']
fur_number_list = []
for data_name in data_to_get:
    fur_number_list.append(data[data['Primary Fur Color'] == data_name]['Primary Fur Color'].count())

print(fur_number_list)

data_dict = {
    'Fur Color': data_to_get,
    'Count': fur_number_list

}

pandas.DataFrame(data_dict).to_csv('squirrel-fur-color.csv')
