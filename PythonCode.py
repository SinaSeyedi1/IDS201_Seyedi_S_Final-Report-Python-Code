import pandas as pd



df = pd.read_excel(r"C:/Users/sinas/OneDrive/Desktop/Introduction to Data Science/Library.xlsx")
df1=df.isnull()
df2=df.dropna()
df3=df.duplicated()
df4=df.drop_duplicates()
print() # Enter the df of choice to receive the desired output, for example "print(df4).
        # To calculate the measures of central tendency, enter print(df.mean(numeric_only=True)) for mean. print(df.median(numeric_only=True)) for median. print(df.mode(numeric_only=True)) for mode.  
        