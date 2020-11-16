import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('./iris.csv', names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])
print(df.head())

sns.pairplot(df, hue='species')
plt.show()