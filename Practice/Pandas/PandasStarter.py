import pandas as pd
import numpy as np

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'Hank'],
    'Department': ['HR', 'IT', 'IT', 'Marketing', 'HR', 'IT', 'Marketing', 'Finance'],
    'Salary': [70000, 85000, 95000, 62000, 72000, 91000, 68000, 75000],
    'Years_Experience': [5, 8, 12, 3, 6, 10, 4, 7],
    'Bonus': [5000, None, 8000, 3000, 4500, None, 4000, 6000],
    'Hire_Date': ['2020-01-15', '2018-06-23', '2016-11-02', '2022-04-10', '2019-08-19', '2017-12-01', '2021-07-12', '2019-03-25']
}
df = pd.DataFrame(data)
print(df)