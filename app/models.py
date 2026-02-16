import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

features = ['EmpSatisfaction', 'SpecialProjectsCount', 'Absences']
target = 'Termd'

MODEL_PATH = 'D:/Broadway/Data Science - 3 to 4.30/fastapi/models/logistic_regression.pkl'

def train_model():
    df = pd.read_csv('D:/Broadway/Data Science - 3 to 4.30/fastapi/data/HR_Dataset Refresh.csv')

    X = df[features]
    Y = df[target]

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42, stratify=Y
    )

    model = LogisticRegression(solver='liblinear', random_state=42, class_weight='balanced')

    model.fit(X_train, Y_train)

    model.predict(X_test)

    joblib.dump(model, MODEL_PATH)
    return model, features, target

def load_model():
    return joblib.load(MODEL_PATH)


