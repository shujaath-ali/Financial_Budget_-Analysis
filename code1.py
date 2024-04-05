import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#reading the dataset
data = pd.read_csv("C:\Users\Documents\India_budget_2021.csv") #Give the address of the dataset from your local machine
data.head()
print(data)
#merging all derived departments into main departments
data = data.iloc[[0,8,11,14,18,23,41,42,43],:]
row = {'Department /Ministry': 'OTHERS', 'Fund allotted(in ₹crores)': 592971.0800000001}
print(data)
#drawing a pie chart
df = data["Fund allotted(in ₹crores)"]
labels = data["Department /Ministry"]
plt.figure(figsize=(10, 7))
plt.pie(df, labels=labels, autopct='%1.1f%%', startangle=90, pctdistance=0.85, shadow =True)
central_circle = plt.Circle((0, 0), 0.5, color='white')
fig = plt.gcf()
fig.gca().add_artist(central_circle)
plt.rc('font', size=9)
plt.title("Distribution of The Budget", fontsize=9)
plt.show()