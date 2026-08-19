import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

df = pd.read_csv("data/training_data.csv")

le = LabelEncoder()
df["Category"] = le.fit_transform(df["Category"])

X = df.drop("Regret", axis=1)
y = df["Regret"]

lr = LogisticRegression(max_iter=1000)
lr.fit(X, y)

dt = DecisionTreeClassifier()
dt.fit(X, y)

joblib.dump(lr, "models/logistic_regression_model.pkl")
joblib.dump(dt, "models/decision_tree_model.pkl")
joblib.dump(le, "models/category_encoder.pkl")

print("Models Saved")