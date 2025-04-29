import pandas as pd
from sklearn.model_selection import train_test_split

data= pd.read_csv("data/housing.csv")

train, test = train_test_split(data, test_size=0.2, random_state=42)

train.to_csv("data/housing_train.csv", index=False)
test.to_csv("data/housing_test.csv", index=False)