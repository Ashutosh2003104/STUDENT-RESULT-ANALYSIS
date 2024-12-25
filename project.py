import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("Expanded_data_with_more_features.csv")
print(df.head())
print(df.describe())
print(df.info())


print(df.isnull().sum())

# dropping Column Unnamed
df = df.drop("Unnamed: 0", axis = 1)
print(df)

#Change Weekly Study Hours Column

df["WklyStudyHours"] = df["WklyStudyHours"].str.replace("05-Oct", "5-10")
print(df.head())

#Gender Distribution using Seaborn library to analyse data
plt.figure(figsize = (4,3))
ax =sns.countplot(data = df, x="Gender")
ax.bar_label(ax.containers[0])
ax.set_title("Gender Distribution")
plt.show()


gb = df.groupby("ParentEduc").agg({"MathScore": 'mean',"ReadingScore": 'mean', "WritingScore": 'mean'})
print(gb)

sns.heatmap(gb)
plt.show()

sns.boxplot(data = df, x = "MathScore") 
plt.show()
sns.boxplot(data = df, x = "WritingScore") 
plt.show()
print(df["EthnicGroup"].unique())
groupA = df.loc[(df['EthnicGroup'] == "Group A")].count()
groupB = df.loc[(df['EthnicGroup'] == "Group B")].count()
groupC = df.loc[(df['EthnicGroup'] == "Group C")].count()
groupD = df.loc[(df['EthnicGroup'] == "Group D")].count()
groupE = df.loc[(df['EthnicGroup'] == "Group E")].count()


ay= sns.countplot(data = df, x = 'EthnicGroup')
ay.bar_label(ax.containers[0])