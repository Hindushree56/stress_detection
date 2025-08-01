import pickle
import numpy as np

# Load the trained model
with open('stress_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Example: Dummy test input — must match training input features (e.g., ECG, EDA, ACC values)
test_sample = np.array([[0.12, 0.45, 0.02]])  # Replace with real data

# Predict the stress level
prediction = model.predict(test_sample)[0]


# Map label to human-readable class
label_map = {1: "Baseline", 2: "Stress", 3: "Amusement"}
print("Predicted Stress State:", label_map.get(prediction, "Unknown"))
