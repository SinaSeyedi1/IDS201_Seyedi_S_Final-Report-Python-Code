import pandas as pd
import matplotlib.pyplot as plt

# This uploads the excel file into python.
file_path = 'r"C:/Users/sinas/OneDrive/Desktop/Introduction to Data Science/Library.xlsx"'
df = pd.read_excel(r"C:/Users/sinas/OneDrive/Desktop/Introduction to Data Science/Library.xlsx")

# This method removes extra whitespaces from the excel sheet.
df.columns = df.columns.str.strip()

# This function creates the figure, in this case there are 3 histograms. It also allows for scaling of the window.
fig, axs = plt.subplots(3, 1, figsize=(20, 15))

# This is the histogram for Age, showing the frequency.
axs[0].hist(df['Age'].dropna(), bins=20, color='purple', edgecolor='black')
axs[0].set_title('Age')
axs[0].set_xlabel('Data for Age')
axs[0].set_ylabel('Frequency')
axs[0].grid(True)

# This is the histogram for Product Preference, showing the count.
product_preference_counts = df['Product Preference'].value_counts()
axs[1].bar(product_preference_counts.index, product_preference_counts.values, color='black', edgecolor='black')
axs[1].set_title('Product Preferences')
axs[1].set_xlabel('Count of Product Preferences')
axs[1].set_ylabel('Count')
axs[1].tick_params(axis='x', rotation=60)
axs[1].grid(True)

# This is the histogram for Profession, showing the count.
profession_counts = df['Profession'].value_counts()
axs[2].bar(profession_counts.index, profession_counts.values, color='yellow', edgecolor='black')
axs[2].set_title('Professions')
axs[2].set_xlabel('Count of Professions')
axs[2].set_ylabel('Count')
axs[2].tick_params(axis='x', rotation=60)
axs[2].grid(True)

# This function displays the program
plt.show()