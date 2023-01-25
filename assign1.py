import pandas as pd/home/ubantu/Desktop/dataset/qs-world-university-rankings-2017-to-2022-V2.csv

df = pd.read_csv('/home/ubantu/Desktop/dataset/qs-world-university-rankings-2017-to-2022-V2.csv')

df.head()


df.faculty_count.isnull()


df.describe()

df.year.describe()

df.describe(include='all')

df.max()

df.min()

newdf = df.isnull()

print(newdf)

df.dtypes

newdf.dtypes


import label encoder

from sklearn import preprocessing

label_encoder = preprocessing.LabelEncoder()
df["region"]=label_encoder.fir_transform(data["region"])
df.head()

label_encoder = preprocessing.LabelEncoder()
df["region"]=label_encoder.fir_transform(data["region"])

