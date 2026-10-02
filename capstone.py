import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("data.csv")

print(data.head(3))
print(data.tail(3))

print(data.info())
print(data.describe())

print(data.isnull().sum())

subset = data.iloc[41:76]
print(subset)

highest = data.loc[data["Votes"].idxmax()]
print(highest)

plt.boxplot([
    data["IMDB_Rating"],
    data["Runtime"]
])
plt.title("Rating and Runtime")
plt.show()

plt.scatter(data["IMDB_Rating"], data["Runtime"])
plt.xlabel("IMDB Rating")
plt.ylabel("Runtime")
plt.title("Rating and Runtime")
plt.show()

plt.hist(data["IMDB_Rating"])
plt.title("Rating Distribution")
plt.show()

plt.hist(data["Runtime"])
plt.title("Runtime Distribution")
plt.show()

sns.countplot(x="Rating", data=data)
plt.xticks(rotation=45)
plt.title("Movie Ratings")
plt.show()