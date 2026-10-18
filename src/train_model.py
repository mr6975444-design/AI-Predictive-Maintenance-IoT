import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    classification_report,
    confusion_matrix
)


# --------------------------------------------------
# 1. Load dataset
# --------------------------------------------------

DATA_PATH = "data/iot_sensor_data.csv"
MODEL_PATH = "models/predictive_maintenance_model.pkl"

data = pd.read_csv(DATA_PATH)

print("=" * 60)
print("PREDICTIVE MAINTENANCE MODEL TRAINING")
print("=" * 60)

print(f"\nDataset shape: {data.shape}")

print("\nFirst 5 rows:")
print(data.head())


# --------------------------------------------------
# 2. Basic data validation
# --------------------------------------------------

print("\nMissing values:")
print(data.isnull().sum())

# Remove rows containing missing values, if any
data = data.dropna()


# --------------------------------------------------
# 3. Select features and target
# --------------------------------------------------

features = [
    "temperature",
    "vibration",
    "current"
]

target = "failure"

X = data[features]
y = data[target]


print("\nFeatures:")
print(features)

print("\nTarget:")
print(target)


# --------------------------------------------------
# 4. Split dataset
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", len(X_train))
print("Testing samples :", len(X_test))


# --------------------------------------------------
# 5. Train Random Forest model
# --------------------------------------------------

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

print("\nTraining model...")

model.fit(X_train, y_train)

print("Model training completed!")


# --------------------------------------------------
# 6. Make predictions
# --------------------------------------------------

y_pred = model.predict(X_test)


# --------------------------------------------------
# 7. Evaluate model
# --------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, zero_division=0)
recall = recall_score(y_test, y_pred, zero_division=0)

print("\n" + "=" * 60)
print("MODEL PERFORMANCE")
print("=" * 60)

print(f"Accuracy : {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall   : {recall:.4f}")

print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))


# --------------------------------------------------
# 8. Save trained model
# --------------------------------------------------

os.makedirs("models", exist_ok=True)

joblib.dump(model, MODEL_PATH)

print("\nModel saved successfully!")
print(f"Location: {MODEL_PATH}")
