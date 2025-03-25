
import joblib
import pandas as pd

class MLPredictor:
    def __init__(self, model_path='planner/ml_model.pkl'):
        self.model = joblib.load(model_path)

    def predict_mode(self, urgency, days_left, task_type):
        # Create a DataFrame to match the model's expected input format
        X_test = pd.DataFrame([[urgency, days_left, task_type]], columns=['urgency', 'days_left', 'task_type'])
        prediction = self.model.predict(X_test)[0]
        mode_map = {0: 'Teórico', 1: 'Práctico', 2: 'Creativo'}
        return mode_map.get(prediction, 'Teórico')
