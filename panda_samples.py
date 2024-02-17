# working with csv library
import csv

with open("./weather_data.csv") as weather_data:
    csv_data = csv.reader(weather_data)
    temperatures = []
    for row in csv_data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

# working with pandas instead
import pandas

data = pandas.read_csv("./weather_data.csv")

print(data["temp"])  # can specify columns by title (first row of csv file)
print(data.temp)  # pandas converts headings to attributes by default

data_as_dictionary = data.to_dict()
series_as_list = data["temp"].to_list()

series_average = data["temp"].mean()
series_high = data["temp"].max()

# get row data where day is Monday
monday = data[data.day == "Monday"]
monday_temp = monday.temp

# print row with max temp
max_temp = data.temp.max()
print(data[data.temp == max_temp])

# create dataframe from scratch
data_dictionary = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

my_dataframe = pandas.DataFrame(data_dictionary)
print(my_dataframe)
my_dataframe.to_csv("new_data.csv")
