import pandas as pd

# a. Read the provided CSV file 'data.csv'
df = pd.read_csv('data.csv')  # Replace 'path/to/your/data.csv' with the actual path

# c. Show the basic statistical description about the data
description = df.describe()
print(description)

# d. Check if the data has null values
null_values = df.isnull().sum()
print("Null Values:")
print(null_values)

# i. Replace the null values with the mean
df.fillna(df.mean(), inplace=True)

# e. Select at least two columns and aggregate the data using: min, max, count, mean
agg_columns = ['Duration', 'Pulse']  # Replace with actual column names
aggregated_data = df[agg_columns].agg(['min', 'max', 'count', 'mean'])
print("Aggregated Data:")
print(aggregated_data)

# f. Filter the dataframe to select the rows with calories values between 500 and 1000
filtered_df_1 = df[(df['Calories'] >= 500) & (df['Calories'] <= 1000)]

# g. Filter the dataframe to select the rows with calories values > 500 and pulse < 100
filtered_df_2 = df[(df['Calories'] > 500) & (df['Pulse'] < 100)]

# h. Create a new "df_modified" dataframe that contains all the columns from df except for "Maxpulse"
df_modified = df.drop(columns=['Maxpulse'])

# i. Delete the "Maxpulse" column from the main df dataframe
df.drop(columns=['Maxpulse'], inplace=True)

# j. Convert the datatype of Calories column to int datatype
df['Calories'] = df['Calories'].astype(int)

# k. Using pandas create a scatter plot for the two columns (Duration and Calories)
import matplotlib.pyplot as plt

plt.scatter(df['Duration'], df['Calories'])
plt.xlabel('Duration')
plt.ylabel('Calories')
plt.title('Scatter Plot: Duration vs Calories')
plt.show()
