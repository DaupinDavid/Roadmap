import email
import pandas as pd
# 
df = pd.read_csv("./clients.csv")
print("--- AVANT ---")
print(df)
df = df.drop_duplicates(subset=["email"])
print("--- APRES ---")
print(df)