import os

# List of directories to create
directories = [
    "data",
    "models",
    "notebooks",
    "results",
    "src",
    "src/tests",
]

# List of files to create
files = [
    "results/roc_curve.png",
    "results/metrics.json",
    "src/evaluate.py",
    "src/model.py",
    "src/preprocess_data.py",
    "src/train.py",
    "credentials.yaml.gpg",
    "dvc.yaml",
    "metadata.yaml",
    "requirements.txt",
]

# Create directories
for directory in directories:
    os.makedirs(directory, exist_ok=True)

# Create empty files
for file in files:
    with open(file, 'w') as f:
        pass

print("Directory structure created successfully.")
