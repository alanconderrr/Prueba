import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('netflix_titles.csv')

df.dropna(subset=['show_id'], inplace=True)
df.fillna('Desconocido', inplace=True)

print(df.info())
print(df.head())

print(df['type'].value_counts())

plt.figure(figsize=(6,4))
sns.countplot(data=df, x='type', palette='Set2')
plt.title('Películas vs Series en Netflix')
plt.show()

top_10_years = df['release_year'].value_counts().nlargest(10)

plt.figure(figsize=(10,5))
top_10_years.plot(kind='bar', color='coral')
plt.title('Títulos lanzados por año (Top 10)')
plt.xlabel('Año')
plt.ylabel('Cantidad')
plt.xticks(rotation=45)
plt.show()