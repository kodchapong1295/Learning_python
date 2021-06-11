# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures= []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

# average = sum(temp_list) / len(temp_list)
average = data["temp"].mean()
max_temp = data["temp"].max()
print(max_temp)

#Get Data in Columns
print(data["condition"])
print(data.condition)

#Get Data in Rows
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

#create DataFrame from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores":[76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")


