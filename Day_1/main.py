import pandas as pd
import numpy as np
import sklearn


df = pd.read_csv("survey_results_public.csv", sep=",")
# print(df.shape)
# print(df.size)
# print(df.max)
df = df[["MainBranch", "Age", "Employment", "CodingActivities"]]
pd.set_option("display.max_columns", None)
# print(df.head())
predict = "CodingActivities"
df = df[[predict]]
print(df.head())
x = np.array(df.drop([predict], 1))
print(x)
