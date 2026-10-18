import joblib
import pandas as pd


MODEL_PATH = "models/predictive_maintenance_model.pkl"


# Load trained model
model = joblib.load(MODEL_PATH)

print("=" * 60)
print("AI-POWERED PREDICTIVE MAINTENANCE")
print("=" * 60)

# Get sensor readings from user
temperature = float(input("\nEnter temperature: "))
vibration = float(input("Enter vibration: "))
current = float(input("Enter current: "))

# Create input DataFrame
input_data = pd.DataFrame({
    "temperature": [temperature],
    "vibration": [vibration],
    "current": [current]
})

# Make prediction
prediction = model.predict(input_data)[0]

# Get probability
probability = model.predict_proba(input_data)[0][1]

print("\n" + "=" * 60)
print("PREDICTION RESULT")
print("=" * 60)

print(f"Temperature : {temperature:.2f}")
print(f"Vibration  : {vibration:.2f}")
print(f"Current    : {current:.2f}")
print(f"Failure probability: {probability * 100:.2f}%")

if prediction == 1:
    print("\n🚨 FAILURE ALERT")
    print("Maintenance inspection is recommended.")
else:
    print("\n✅ NORMAL")
    print("Machine condition appears normal.")

print("=" * 60)
