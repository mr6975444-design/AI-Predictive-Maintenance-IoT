import os
import numpy as np
import pandas as pd

np.random.seed(42)

NUM_SAMPLES = 5000

temperature = np.random.normal(loc=65, scale=8, size=NUM_SAMPLES)
vibration = np.random.normal(loc=2.5, scale=0.7, size=NUM_SAMPLES)
current = np.random.normal(loc=5.0, scale=1.0, size=NUM_SAMPLES)

failure = (
    (temperature > 80)
    | (vibration > 4.0)
    | (current > 7.0)
).astype(int)

data = pd.DataFrame({
    "temperature": temperature,
    "vibration": vibration,
    "current": current,
    "failure": failure
})

os.makedirs("data", exist_ok=True)

output_file = "data/iot_sensor_data.csv"
data.to_csv(output_file, index=False)

print("=" * 50)
print("IoT SENSOR DATA GENERATED SUCCESSFULLY")
print("=" * 50)
print(f"Number of records : {len(data)}")
print(f"Output file       : {output_file}")
print(f"Failure cases     : {data['failure'].sum()}")
print(f"Normal cases      : {(data['failure'] == 0).sum()}")

print("\nFirst 5 records:")
print(data.head())

print("\nDataset statistics:")
print(data.describe())
