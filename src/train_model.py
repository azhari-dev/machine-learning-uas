# src/train_model.py

import joblib
from sklearn.ensemble import RandomForestRegressor

def train_random_forest(X_train, y_train, model_path):
    model = RandomForestRegressor(
        n_estimators=200,
        random_state=42,
        n_jobs=-1
    )
    model.fit(X_train, y_train)
    joblib.dump(model, model_path)
    return model