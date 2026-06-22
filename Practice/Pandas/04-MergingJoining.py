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

dept_info = pd.DataFrame({
    'Department': ['HR', 'IT', 'Marketing', 'Finance'],
    'Manager': ['Sarah', 'Tom', 'Lisa', 'Mark'],
    'Floor': [1, 3, 2, 4]
})

df = pd.DataFrame(data)

print("\n" + "="*50);
print("--- Total Data Frame ---")
print("="*50 + "\n");

print(df)

print("\n" + "="*50);
print("--- A separate table for Department managers ---")
print("="*50 + "\n");

print(dept_info)

print("\n" + "="*50);
print("--- Inner Merge for department and employee data ---")
print("="*50 + "\n");

print(pd.merge(df, dept_info, on='Department', how='inner'))

print("\n" + "="*50);
print("--- Inner Merge for department and employee data ---")
print("="*50 + "\n");

new_hire = pd.DataFrame({'Name': ['Ivy'], 'Department': ['IT'], 'Salary': [88000]})
print(pd.concat([df, new_hire], ignore_index=True))