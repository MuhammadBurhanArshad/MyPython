import pandas as pd

data = [
    {'Name': 'Leo', 'Department': 'IT', 'Salary': 105000, 'Years_Experience': 15, 'Bonus': 12000, 'Hire_Date': '2015-06-01'},
    {'Name': 'Mia', 'Department': 'HR', 'Salary': 78000, 'Years_Experience': 6, 'Bonus': 5500, 'Hire_Date': '2020-11-11'},
    {'Name': 'Noah', 'Department': 'Finance', 'Salary': 83000, 'Years_Experience': 8, 'Bonus': 6800, 'Hire_Date': '2019-07-22'},
    {'Name': 'Ethan', 'Department': 'Marketing', 'Salary': 92000, 'Years_Experience': 10, 'Bonus': 9000, 'Hire_Date': '2018-03-15'},
    {'Name': 'Ava', 'Department': 'Sales', 'Salary': 85000, 'Years_Experience': 7, 'Bonus': 6500, 'Hire_Date': '2019-09-20'},
    {'Name': 'Liam', 'Department': 'IT', 'Salary': 100000, 'Years_Experience': 12, 'Bonus': 11000, 'Hire_Date': '2016-01-05'},
    {'Name': 'Isabella', 'Department': 'HR', 'Salary': 75000, 'Years_Experience': 5, 'Bonus': 5000, 'Hire_Date': '2021-06-01'},
    {'Name': 'Oliver', 'Department': 'Finance', 'Salary': 90000, 'Years_Experience': 11, 'Bonus': 10000, 'Hire_Date': '2017-08-10'},
    {'Name': 'Sophia', 'Department': 'Marketing', 'Salary': 88000, 'Years_Experience': 9, 'Bonus': 8000, 'Hire_Date': '2018-11-15'},
    {'Name': 'Benjamin', 'Department': 'Sales', 'Salary': 82000, 'Years_Experience': 6, 'Bonus': 6000, 'Hire_Date': '2020-03-20'}
]

df = pd.DataFrame(data)

print("\n" + "="*50);
print("--- Total Data Frame ---")
print("="*50 + "\n");

print(df)   

print("\n" + "="*50);
print("--- First Three Rows ---")
print("="*50 + "\n");

print(df.head(3))   

print("\n" + "="*50);
print("--- Last Two Rows ---")
print("="*50 + "\n");

print(df.tail(2))   

print("\n" + "="*50);
print("--- Info of Table ---")
print("="*50 + "\n");

print(df.info())   

print("\n" + "="*50);
print("--- Summary of Table ---")
print("="*50 + "\n");

print(df.describe())   

print("\n" + "="*50);
print("--- Targeting Name Column from Table as Series ---")
print("="*50 + "\n");

print(df['Name'])   

print("\n" + "="*50);
print("--- Targeting Name Column from Table as DataFrame ---")
print("="*50 + "\n");

print(df[['Name']])   

print("\n" + "="*50);
print("--- Targeting Name & Salary Column from Table as DataFrame ---")
print("="*50 + "\n");

print(df[['Name', 'Salary']])   

print("\n" + "="*50);
print("--- Label Based Indexing ---")
print("="*50 + "\n");

df_name_index = df.set_index('Name')
print(df_name_index.loc['Leo']) 

print("\n" + "="*50);
print("--- Label Based Indexing ---")
print("="*50 + "\n");

df_name_index = df.set_index('Name')
print(df_name_index.loc['Leo']) 

print("\n" + "="*50);
print("--- Label Based Filtering as DataFrame ---")
print("="*50 + "\n");

print(df[df['Name'] == "Leo"]) 

print("\n" + "="*50);
print("--- Index Based Data Filtering ---")
print("="*50 + "\n");

print(df.iloc[2])  # iloc is for indexing column when we don't not about the column or row name

print("\n" + "="*50);
print("--- Salary > 75000 Filtering ---")
print("="*50 + "\n");

print(df[df['Salary'] > 75000])
