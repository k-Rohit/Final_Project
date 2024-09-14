import os
import subprocess
from ultralytics import YOLO
from azureml.core import Run

# Step 1: Initialize Azure ML Run object
run = Run.get_context()

# Step 2: Pull the data using DVC
# Ensure that DVC is installed in your environment and your remote storage is configured.
try:
    subprocess.run(["dvc", "pull"], check=True)
    print("DVC pull successful. Data is now available.")
except subprocess.CalledProcessError as e:
    print(f"Error during DVC pull: {e}")
    run.fail()

# Step 3: Define the paths to your data and model
data_yaml_path = "../data/dataset.yaml"  # Path to dataset.yaml
trained_model_path = "/Users/kumarrohit/Desktop/MLOPS_LAB/Final_Project/models/yolov8_trained_model.pt"

# Step 4: Load YOLOv8 segmentation model
model = YOLO("yolov8n-seg.pt")

# Step 5: Train the model
results = model.train(
    data=data_yaml_path,   # Path to the dataset.yaml
    epochs=100,            # Number of epochs
    imgsz=1280,            # Image size
    task="segment",        # YOLO task type (segmentation)
    batch=8                # Batch size
)

# Step 6: Log hyperparameters (parameters) to Azure ML
run.log("epochs", 100)
run.log("imgsz", 1280)
run.log("batch", 8)

# Step 7: Log metrics (example metrics; actual metric access may differ)
# Replace 'metrics' with actual access code for your results
run.log("train_loss", results.metrics.get('train_loss', 0))
run.log("val_loss", results.metrics.get('val_loss', 0))
run.log("mAP_50", results.metrics.get('mAP_50', 0))
run.log("mAP_95", results.metrics.get('mAP_50-95', 0))

# Step 8: Save the trained model
model.save(trained_model_path)

# Step 9: Log the trained model as an artifact in Azure ML
run.upload_file(name="/Users/kumarrohit/Desktop/MLOPS_LAB/Final_Project/models/yolov8_trained_model.pt", path_or_stream=trained_model_path)

# Step 10: Complete the Azure ML run
run.complete()
