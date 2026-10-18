
from pathlib import Path

# Main project folder
project_name = "AI-Predictive-Maintenance-IoT"
root = Path(project_name)

# Folders to create
folders = [
    "data",
    "notebooks",
    "src",
    "models",
    "outputs",
    "images",
    "docs",
]

# Files to create with starter content
files = {
    "main.py": '''"""Main entry point for the predictive maintenance project."""

def main():
    print("AI-Powered Predictive Maintenance System")
    print("Project setup completed successfully!")

if __name__ == "__main__":
    main()
''',

    "requirements.txt": '''pandas
numpy
scikit-learn
matplotlib
seaborn
joblib
flask
requests
''',

    "README.md": '''# AI-Predictive-Maintenance-IoT

An AI-powered predictive maintenance project using
simulated IoT sensor data and machine learning.

## Features
- Simulated sensor data
- Machine failure prediction
- Random Forest classification
- Data visualization
- Flask prediction API

## Installation

```bash
python -m venv .venv
```

Activate the environment, then install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run

```bash
python main.py
```

## Dataset
The project will use simulated temperature, vibration,
and current readings.

## Disclaimer
This is an educational simulation, not a validated
industrial safety or maintenance system.
''',

    ".gitignore": '''# Virtual environments
venv/
.venv/
env/

# Python cache
__pycache__/
*.py[cod]

# Secrets
.env

# Editor settings
.vscode/

# Jupyter
.ipynb_checkpoints/

# Operating system
.DS_Store
Thumbs.db
''',
}

# Create folders
for folder in folders:
    (root / folder).mkdir(parents=True, exist_ok=True)

# Add .gitkeep so empty folders appear in Git
for folder in folders:
    (root / folder / ".gitkeep").touch(exist_ok=True)

# Create files without overwriting existing files
for filename, content in files.items():
    file_path = root / filename

    if not file_path.exists():
        file_path.write_text(content, encoding="utf-8")
        print(f"Created: {file_path}")
    else:
        print(f"Already exists, skipped: {file_path}")

print("\nProject structure created successfully!")
print(f"Location: {root.resolve()}")
