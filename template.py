import os

def create_folder_structure():
    # Define the base project structure
    project_root = "."  # Root folder of your project

    # Folders to create
    folders = [
        "data/raw_images",             # Raw images folder for annotation
        "data/processed_images",       # Preprocessed images
        "data/annotations/labelme_json",  # LabelMe JSON annotation files
        "data/annotations/yolov8_txt",    # Converted YOLOv8 TXT files
        "data/train/images",           # Training images
        "data/train/labels",           # Training YOLOv8 TXT labels
        "data/val/images",             # Validation images
        "data/val/labels",             # Validation YOLOv8 TXT labels
        "data/test/images",            # Test images
        "data/test/labels",            # Test YOLOv8 TXT labels
        "models",                      # Models folder
        "predictions",                 # Predictions folder (for inference results)
        "scripts",                     # Scripts folder
    ]

    # Files to create with placeholders
    files = {
        "scripts/convert_labelme_to_yolo.py": "# Script to convert LabelMe JSON to YOLOv8 TXT\n",
        "scripts/data_preprocessing.py": "# Script to preprocess images (e.g., resize)\n",
        "scripts/train.py": "# YOLOv8 training script\n",
        "scripts/inference.py": "# Inference script for generating predictions\n",
        "README.md": "# Project description and instructions\n",  # This might already exist
        "score.py": "# Inference script for Azure deployment\n",
        "env.yml": "# Conda environment file for Azure deployment\n"
    }

    # Create folders
    for folder in folders:
        folder_path = os.path.join(project_root, folder)
        os.makedirs(folder_path, exist_ok=True)
        print(f"Created folder: {folder_path}")

    # Create files with placeholder content
    for file, content in files.items():
        file_path = os.path.join(project_root, file)
        if not os.path.exists(file_path):  # Only create if file doesn't already exist
            with open(file_path, 'w') as f:
                f.write(content)
            print(f"Created file: {file_path}")
        else:
            print(f"File already exists: {file_path}")

    print("\nProject structure created successfully!")

if __name__ == "__main__":
    create_folder_structure()
