import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data_df = pd.read_csv("Data.csv")
print(data_df.head())
print(data_df.info())

for col in data_df.columns:
    missing_data = data_df[col].isna().sum()
    missing_percent = missing_data/len(data_df)*100
    print(f"Column {col}: has {missing_percent}% missing data")
fig, ax = plt.subplots(figsize=(8, 5))
sns.heatmap(data_df.isna(), cmap="Blues", cbar=False, yticklabels=False)
plt.show()

x = data_df.iloc[:, :-1].values
y = data_df.iloc[:, -1].values
print(x)
print(y)
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])
print(x)

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder="passthrough")
x = ct.fit_transform(x)
print(x)
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)
print(y)

from sklearn.model_selection import train_test_split
np.random.seed(42)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train[:, 3:] = sc.fit_transform(x_train[:, 3:])
print(x_train)
x_test[:, 3:] = sc.fit_transform(x_test[:, 3:])
print(x_test)