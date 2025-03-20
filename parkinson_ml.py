import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score,f1_score, roc_auc_score, confusion_matrix

import pickle

data = pd.read_csv('parkinsons.data')

print("Columns in dataset:", data.columns)

X = data.drop(['name', 'status'], axis=1)
y = data['status']

print("Missing values:\n", X.isnull().sum())

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train) 
X_test_scaled = scaler.transform(X_test)  

#training
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)

accuracy = accuracy_score(y_test , y_pred)
precision = precision_score(y_test,y_pred)
recall =recall_score(y_test,y_pred)
f1 = f1_score(y_test,y_pred)
roc_auc = roc_auc_score(y_test,model.predict_log_proba(X_test_scaled) [:, 1])
print(f"Accuracy : {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"recall: {recall:.2f}")
print(f"F1-Score: {f1:.2f}")
print(f"ROC-AUC: {roc_auc:.2f}")

# cm = confusion_matrix(y_test, y_pred)
# sns.heatmap(cm,annot=True, fmt ='d', cmap='Blues')
# plt.title("Confusion Matrix")
# plt.xlabel("predicted")

cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm,annot=True, fmt ='d', cmap='Blues')
plt.title("Confusion Matrix")
plt.xlabel("predicted")
plt.ylabel("Actual")
plt.show()

# eda
plt.figure(figsize=(10,8))
sns.heatmap(data.drop('name',axis =1).corr(), annot=False, cmap='coolwarm')
plt.title("Feature correlative Heatmap")
plt.show()

sns.countplot(x='status', data=data)
plt.title("Distribution of parkinson's status")
plt.show()

print("Training set shape:", X_train_scaled.shape)
print("Testing set shape:", X_test_scaled.shape)


# importance
importances = model.feature_importances_
feature_names = X.columns
feature_importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
feature_importance_df = feature_importance_df.sort_values('Importance', ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x='Importance', y='Feature', data=feature_importance_df)
plt.title("Feature Importance in Random Forest")
plt.show()

#model save

pickle.dump(model, open('Parkinson_model.pkl','wb'))
pickle.dump(scaler, open('scaler.pkl','wb'))