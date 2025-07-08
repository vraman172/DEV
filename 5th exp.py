import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create the data dictionary
data = {
    'ID': range(1, 11),
    'Age': np.random.randint(18, 65, size=10),
    'Income': np.random.randint(30000, 90000, size=10),
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Male'],
    'Education': ['High School', 'Bachelor', 'Master', 'PhD', 'Bachelor', 'Master', 'Bachelor',
                  'PhD', 'High School', 'Master']
}

# Create DataFrame
df = pd.DataFrame(data)

# Print first 5 rows and summary stats
print(df.head())
print(df.describe())

# Check for missing values
print(df.isnull().sum())

# Unique values for Gender and Education columns
print(df['Gender'].unique())
print(df['Education'].unique())

# Select Age and Income columns
selected_columns = df[['Age', 'Income']]
print(selected_columns.head())

# Filter rows where Age > 30
filtered_data = df[df['Age'] > 30]
print(filtered_data.head())

# Filter rows where Gender is Male and Education is Master
filtered_rows = df[(df['Gender'] == 'Male') & (df['Education'] == 'Master')]
print(filtered_rows.head())

# Plot histogram of Age
plt.hist(df['Age'], bins=5, edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Plot boxplot of Income
plt.boxplot(df['Income'])
plt.title('Income Distribution')
plt.ylabel('Income')
plt.show()

# Plot bar chart for Gender counts
gender_counts = df['Gender'].value_counts()
gender_counts.plot(kind='bar', color='skyblue')
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

# Plot pie chart for Education distribution
education_counts = df['Education'].value_counts()
education_counts.plot(kind='pie', autopct='%1.1f%%', colors=['gold', 'lightcoral', 'lightgreen', 'lightskyblue'])
plt.title('Education Distribution')
plt.ylabel('')
plt.show()

