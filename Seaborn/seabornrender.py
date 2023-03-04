import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

tips_df = sns.load_dataset('tips')
print(tips_df.head())
sns.set_theme()
sns.histplot(data=tips_df["total_bill"])
plt.show()
print(tips_df["total_bill"].value_counts().sort_values(ascending=False))
sns.kdeplot(data=tips_df["total_bill"])
plt.show()
sns.displot(data=tips_df, x="total_bill", col="time", kde=True)
plt.show()
print(tips_df.head())
sns.barplot(data=tips_df, x="sex", y="tip", estimator=np.mean)
plt.show()
sns.countplot(data=tips_df, x="sex")
plt.show()
sns.boxplot(data=tips_df, x="day", y="total_bill", hue="sex", palette="Blues")
plt.legend(loc=0)
plt.show()
tips_fg = sns.FacetGrid(data=tips_df, row="smoker", col="time")
tips_fg.map(sns.scatterplot, 'total_bill', 'tip')
plt.show()

new_fg = sns.FacetGrid(data=tips_df, col="sex", hue="smoker",
                       col_order=["Female", "Male"], palette='Set2',
                       height=4, aspect=1.4)
new_fg.map(sns.scatterplot, 'total_bill', 'tip', s=100, edgecolor='b', alpha=0.7)
new_fg.add_legend()
plt.show()

penguins_df = sns.load_dataset('penguins')
sns.jointplot(data=penguins_df, x="flipper_length_mm", y="bill_length_mm", hue="species")
plt.show()
sns.pairplot(data=penguins_df, hue="species")
plt.show()

flights_df = sns.load_dataset("flights")
flights = pd.pivot_table(flights_df, index='month', columns='year', values='passengers')
sns.heatmap(data=flights, cmap='Blues', linecolor='white', linewidths=1)
plt.show()

cereal_df = pd.read_csv('cereal.csv')
print(cereal_df.head())
fields = ['shelf', 'weight', 'cups', 'rating']
cereal_df_new = cereal_df.drop(fields, axis=1)
print(cereal_df_new.head())
cereal_corr = cereal_df_new.corr()
ones_corr = np.ones_like(cereal_corr, dtype=bool)
mask = np.triu(ones_corr)
sns.heatmap(data=cereal_corr, mask=mask)
plt.show()
adjusted_mask = mask[1:, :-1]
adjusted_mask_corr = cereal_corr.iloc[1:, :-1]
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(data=adjusted_mask_corr, mask=adjusted_mask,
            annot=True, fmt=".2f", cmap="Blues", vmin=-1, vmax=1,
            linecolor='white', linewidths=0.5)
yticks = [i.upper() for i in adjusted_mask_corr.index]
xticks = [i.upper() for i in adjusted_mask_corr.columns]
ax.set_yticklabels(yticks, rotation=0)
ax.set_xticklabels(xticks, rotation=90)
plt.show()