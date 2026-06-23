import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

df = pd.read_csv('loan_approval_data.csv')

inputs = df.drop('Loan_Status', axis='columns')
target = df['Loan_Status']

le_gender = LabelEncoder()
le_married = LabelEncoder()
le_education = LabelEncoder()
le_self_employed = LabelEncoder()

inputs['Gender'] = le_gender.fit_transform(inputs['Gender'])           
inputs['Married'] = le_married.fit_transform(inputs['Married'])       
inputs['Education'] = le_education.fit_transform(inputs['Education']) 
inputs['Self_Employed'] = le_self_employed.fit_transform(inputs['Self_Employed']) 

target_encoded = target.map({'Y': 1, 'N': 0})

X_train, X_test, Y_train, Y_test = train_test_split(inputs, target_encoded, test_size=0.2, random_state=42)

model = tree.DecisionTreeClassifier(random_state=42, max_depth=4)  # max_depth prevents overfitting
model.fit(X_train, Y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(Y_test, predictions) * 100
print(f"\n Accuracy on Test Set: {accuracy:.2f}%")

print("\n--- Classification Report ---")
print(classification_report(Y_test, predictions, target_names=['Rejected', 'Approved']))

print("\n--- Confusion Matrix ---")
print(confusion_matrix(Y_test, predictions))

importances = model.feature_importances_
feature_names = inputs.columns.tolist()

print("\n--- Feature Importance ---")
for name, importance in sorted(zip(feature_names, importances), key=lambda x: x[1], reverse=True):
    print(f"{name}: {importance:.3f}")
