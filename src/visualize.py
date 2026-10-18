import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix


# --------------------------------------------------
# Paths
# --------------------------------------------------

DATA_PATH = "data/iot_sensor_data.csv"
MODEL_PATH = "models/predictive_maintenance_model.pkl"
OUTPUT_DIR = "outputs"

os.makedirs(OUTPUT_DIR, exist_ok=True)


# --------------------------------------------------
# Load data and model
# --------------------------------------------------

data = pd.read_csv(DATA_PATH)
model = joblib.load(MODEL_PATH)


# --------------------------------------------------
# 1. Sensor distributions
# --------------------------------------------------

fig, ax = plt.subplots(figsize=(8, 5))

ax.hist(data["temperature"], bins=30)

ax.set_title("Temperature Distribution")
ax.set_xlabel("Temperature")
ax.set_ylabel("Frequency")

plt.tight_layout()
plt.savefig(
    f"{OUTPUT_DIR}/temperature_distribution.png",
    dpi=300
)
plt.close()


fig, ax = plt.subplots(figsize=(8, 5))

ax.hist(data["vibration"], bins=30)

ax.set_title("Vibration Distribution")
ax.set_xlabel("Vibration")
ax.set_ylabel("Frequency")

plt.tight_layout()
plt.savefig(
    f"{OUTPUT_DIR}/vibration_distribution.png",
    dpi=300
)
plt.close()


fig, ax = plt.subplots(figsize=(8, 5))

ax.hist(data["current"], bins=30)

ax.set_title("Current Distribution")
ax.set_xlabel("Current")
ax.set_ylabel("Frequency")

plt.tight_layout()
plt.savefig(
    f"{OUTPUT_DIR}/current_distribution.png",
    dpi=300
)
plt.close()


# --------------------------------------------------
# 2. Failure vs Normal
# --------------------------------------------------

failure_counts = data["failure"].value_counts().sort_index()

labels = ["Normal", "Failure"]

fig, ax = plt.subplots(figsize=(7, 5))

ax.bar(labels, failure_counts.values)

ax.set_title("Normal vs Failure Cases")
ax.set_xlabel("Machine Condition")
ax.set_ylabel("Number of Records")

plt.tight_layout()
plt.savefig(
    f"{OUTPUT_DIR}/failure_distribution.png",
    dpi=300
)
plt.close()


# --------------------------------------------------
# 3. Confusion Matrix
# --------------------------------------------------

features = [
    "temperature",
    "vibration",
    "current"
]

X = data[features]
y = data["failure"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

y_pred = model.predict(X_test)

cm = confusion_matrix(y_test, y_pred)

fig, ax = plt.subplots(figsize=(7, 6))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["Normal", "Failure"],
    yticklabels=["Normal", "Failure"],
    ax=ax
)

ax.set_title("Confusion Matrix")
ax.set_xlabel("Predicted")
ax.set_ylabel("Actual")

plt.tight_layout()
plt.savefig(
    f"{OUTPUT_DIR}/confusion_matrix.png",
    dpi=300
)
plt.close()


# --------------------------------------------------
# 4. Feature Importance
# --------------------------------------------------

importance = model.feature_importances_

fig, ax = plt.subplots(figsize=(8, 5))

ax.bar(features, importance)

ax.set_title("Feature Importance")
ax.set_xlabel("Sensor Feature")
ax.set_ylabel("Importance")

plt.tight_layout()
plt.savefig(
    f"{OUTPUT_DIR}/feature_importance.png",
    dpi=300
)
plt.close()


# --------------------------------------------------
# Finished
# --------------------------------------------------

print("=" * 60)
print("VISUALIZATION COMPLETED")
print("=" * 60)

print("\nGenerated files:")

for filename in sorted(os.listdir(OUTPUT_DIR)):
    if filename.endswith(".png"):
        print(f"✓ outputs/{filename}")
