import pandas as pd

df = pd.read_csv('decision_tree_dataset_with_target.csv')

# print(df)

from sklearn.preprocessing import LabelEncoder

inputs = df.drop('salary_more_then_100k', axis='columns')
target = df['salary_more_then_100k']

le_company = LabelEncoder()
le_job = LabelEncoder()
le_degree = LabelEncoder()

inputs['company'] = le_company.fit_transform(inputs['company']) 
inputs['job'] = le_job.fit_transform(inputs['job']) 
inputs['degree'] = le_degree.fit_transform(inputs['degree']) 

from sklearn import tree
from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(inputs, target, test_size=0.2, random_state=None)

model = tree.DecisionTreeClassifier()
model.fit(X_train, Y_train)

from sklearn.metrics import accuracy_score

predictions = model.predict(X_test)

print("Accuracy: ", accuracy_score(Y_test, predictions) * 100, "%")
