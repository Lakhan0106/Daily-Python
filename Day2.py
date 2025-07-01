## How to read CSV file in python

import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
print(df.to_string())

print(pd.options.display.max_columns)

## JSON data in dictionary

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)

print(df) 

## Reading data 

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
print(df.head(10))

print(df.tail())

print(df.info())

##Removing empty sells inside the data

new_df = df.dropna()
print(new_df)

## Replacing NUll value with C83

my_df = df.fillna({"Cabin" : "C82"})
print(my_df)

##REmoving Rows with NULL values

MYdf = df.dropna(subset=['Cabin'], inplace = True)
print(MYdf)

dfn = df.loc[1,"Cabin"] = "C88"
print(df.duplicated())

df.plot()
import pandas as pd
import matplotlib.pyplot as plt

df.plot()
plt.show()
