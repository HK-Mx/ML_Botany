import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier
import joblib # Para guardar el modelo y el scaler
from sklearn.metrics import classification_report # Para el reporte final



X = df_train_final.drop(columns=["success", "Unnamed: 0"])
y = df_train_final["success"]


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, stratify=y, random_state=42
)

modelo_xgb = XGBClassifier(eval_metric='logloss', random_state=42)
params_xgb = {
    'n_estimators': [100], 
    'max_depth': [6]      
}

grid_xgb = GridSearchCV(modelo_xgb, params_xgb, cv=5, scoring='f1', n_jobs=-1)
grid_xgb.fit(X_train, y_train)


mejor_modelo_final = grid_xgb.best_estimator_

print("Mejores parámetros finales:", grid_xgb.best_params_)


joblib.dump(mejor_modelo_final, "new_model.pkl")
joblib.dump(scaler, "new_scaler.pkl")
