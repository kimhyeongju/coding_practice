import pandas as pd
df = pd.read_csv('./pima-indians-diabetes.csv', names=['pregnant', 'plasma', 'pressure', 'thickness', 'insulin'
                                                       , 'BMI', 'pedigree', 'age', 'class'])
print(df.head(5))