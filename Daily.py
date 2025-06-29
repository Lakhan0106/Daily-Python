## python first program

print("Hello World")

## pandas

import pandas as pd

mydata = {
    "name" : ["Lakhan"],
    "age": 21,
    "designation": ["Data Engineer"],
}

print(pd.DataFrame(mydata))

## Pandas Series 

a = [1,2,3,4,5]

myvar= pd.Series(a)
print(myvar)

print(myvar[2])

print(pd.Series(a, index=["x","y","z","l","m"]))


##creating series using Dictionary


mydata={"Name":"Lakhan","Age":21,"DEsg":"DE"}

myv= pd.Series(mydata)
print(myv)

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)


## DataFrames in python 
newdata ={
    
    "Name":["Lakhan","Yashal","Ujwal"],
    "Age":[21,21,22],

}

new = pd.DataFrame(newdata)
print(new)
## loc attribute to locate 
print(new.loc[0])


data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df)

## Read CSV file

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
print(df)

