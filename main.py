import subprocess
import sys


def run_step(description, command):
    print("\n" + "=" * 60)
    print(description)
    print("=" * 60)

    result = subprocess.run(command)

    if result.returncode != 0:
        print(f"\n❌ Failed: {description}")
        sys.exit(result.returncode)

    print(f"\n✅ Completed: {description}")


def main():
    print("\n" + "=" * 60)
    print("AI-POWERED PREDICTIVE MAINTENANCE FOR IoT DEVICES")
    print("=" * 60)

    run_step(
        "STEP 1: Generating simulated IoT sensor data",
        [sys.executable, "src/generate_data.py"]
    )

    run_step(
        "STEP 2: Training predictive-maintenance model",
        [sys.executable, "src/train_model.py"]
    )

    run_step(
        "STEP 3: Generating visualizations",
        [sys.executable, "src/visualize.py"]
    )

    print("\n" + "=" * 60)
    print("🎉 COMPLETE PROJECT PIPELINE FINISHED")
    print("=" * 60)

    print("\nGenerated project outputs:")
    print("✓ data/iot_sensor_data.csv")
    print("✓ models/predictive_maintenance_model.pkl")
    print("✓ outputs/*.png")

    print("\nTo test a new sensor reading:")
    print("python3 src/predict.py")


if __name__ == "__main__":
    main()
