import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'Hank'],
    'Department': ['HR', 'IT', 'IT', 'Marketing', 'HR', 'IT', 'Marketing', 'Finance'],
    'Salary': [70000, 85000, 95000, 62000, 72000, 91000, 68000, 75000],
    'Years_Experience': [5, 8, 12, 3, 6, 10, 4, 7],
    'Bonus': [5000, None, 8000, 3000, 4500, None, 4000, 6000],
    'Hire_Date': ['2020-01-15', '2018-06-23', '2016-11-02', '2022-04-10', '2019-08-19', '2017-12-01', '2021-07-12', '2019-03-25']
}
df = pd.DataFrame(data)

print("--- Column-Based DataFrame ---")
print(df)

print("\n" + "="*50 + "\n")

row_data = [
    ['Ivy', 'IT', 88000, 9, 7000, '2020-05-20'],
    ['Jack', 'Finance', 92000, 11, 8500, '2018-10-15'],
    ['Karen', 'Marketing', 65000, 2, 2000, '2023-01-10']
]

columns = ['Name', 'Department', 'Salary', 'Years_Experience', 'Bonus', 'Hire_Date']

df2 = pd.DataFrame(row_data, columns=columns)

print("--- Built from List of Lists / Row Array ---")
print(df2)

print("\n" + "="*50 + "\n")

record_data = [
    {'Name': 'Leo', 'Department': 'IT', 'Salary': 105000, 'Years_Experience': 15, 'Bonus': 12000, 'Hire_Date': '2015-06-01'},
    {'Name': 'Mia', 'Department': 'HR', 'Salary': 78000, 'Years_Experience': 6, 'Bonus': 5500, 'Hire_Date': '2020-11-11'},
    {'Name': 'Noah', 'Department': 'Finance', 'Salary': 83000, 'Years_Experience': 8, 'Bonus': 6800, 'Hire_Date': '2019-07-22'}
]

df3 = pd.DataFrame(record_data)

print("--- Built from List of Dictionaries / Records ---")
print(df3)

print("\n" + "="*50 + "\n")

master_df = pd.concat([df, df2, df3], ignore_index=True)
print("--- MASTER DataFrame (Combined) ---")
print(master_df)