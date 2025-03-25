import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Dataset sintético de ejemplo
data = pd.DataFrame({
    'urgency': [5, 3, 4, 2, 1],
    'days_left': [1, 5, 2, 10, 15],
    'task_type': [0, 1, 2, 0, 1],  # 0=teórica, 1=práctica, 2=ensayo
    'mode_label': [0, 1, 2, 0, 1]   # 0=Teórico, 1=Práctico, 2=Creativo
})

X = data[['urgency', 'days_left', 'task_type']]
y = data['mode_label']

model = RandomForestClassifier()
model.fit(X, y)

# Guardar el modelo
joblib.dump(model, 'planner/ml_model.pkl')
print("Modelo entrenado y guardado en planner/ml_model.pkl")
