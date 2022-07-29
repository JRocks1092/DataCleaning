import pandas as pd

df = pd.read_csv("mergedData.csv")
df.drop(["Unnamed: 0", "Luminosity"], axis=1,inplace=True)
df.dropna()
df.reset_index(drop=True, inplace=True)
df.to_csv("finalData.csv")