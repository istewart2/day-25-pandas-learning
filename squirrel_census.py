import pandas

# how many grey, black or cinnamon squirrels are there?
data = pandas.read_csv("./squirrel_data.csv")
primary_fur_colour = data["Primary Fur Color"]

grey_count = len(data[primary_fur_colour == "Gray"])
red_count = len(data[primary_fur_colour == "Cinnamon"])
black_count = len(data[primary_fur_colour == "Black"])

squirrel_colour_dictionary = {
    "Fur colour": ["grey", "red", "black"],
    "Count": [grey_count, red_count, black_count]
}
print(squirrel_colour_dictionary)

# build dataframe, then export to squirrel_count.csv
squirrel_dataframe = pandas.DataFrame(squirrel_colour_dictionary)
squirrel_dataframe.to_csv("squirrel_count.csv")

