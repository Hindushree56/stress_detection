import os
import pickle
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

data_dir = 'WESAD/S17'  # Change to the parent directory of all subject folders (e.g., 'WESAD')

X_all, y_all = [], []

for subject in os.listdir(data_dir):  # Loop over all subjects like S2, S3...
    if not subject.startswith('S'):
        continue

    filepath = os.path.join(data_dir, subject, subject + '.pkl')
    if not os.path.exists(filepath):
        continue

    with open(filepath, 'rb') as file:
        data = pickle.load(file, encoding='latin1')

    signals = data['signal']
    labels = data['label']

    min_len = min(len(signals['BVP']), len(signals['EDA']), len(signals['TEMP']))
    bvp = signals['BVP'][:min_len]
    eda = signals['EDA'][:min_len]
    temp = signals['TEMP'][:min_len]
    label = labels[:min_len]

    df = pd.DataFrame({
        'BVP': bvp.flatten(),
        'EDA': eda.flatten(),
        'TEMP': temp.flatten()
    })

    binary_label = np.array([1 if l != 0 else 0 for l in label])
    X_all.append(df)
    y_all.append(binary_label)

# Combine all subjects
X = pd.concat(X_all)
y = np.concatenate(y_all)

print("Final data shape:", X.shape)
print("Label distribution:", pd.Series(y).value_counts())

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Evaluate
y_pred = clf.predict(X_test)
print("Classification Report:\n", classification_report(y_test, y_pred))
