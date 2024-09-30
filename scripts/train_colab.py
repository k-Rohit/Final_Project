import os
import subprocess
from ultralytics import YOLO
import mlflow
import mlflow.pyfunc
from ultralytics import settings

# Update a setting
settings.update({"mlflow": True})

# Reset settings to default values
settings.reset()

# Step 1: Initialize MLflow Run
mlflow.start_run()

# Step 2: Pull the data using DVC
# Ensure that DVC is installed in your environment and your remote storage is configured.
try:
    subprocess.run(["dvc", "pull"], check=True)
    print("DVC pull successful. Data is now available.")
except subprocess.CalledProcessError as e:
    print(f"Error during DVC pull: {e}")
    mlflow.end_run(status='FAILED')
    raise e

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

# Step 6: Log hyperparameters (parameters) to MLflow
mlflow.log_param("epochs", 100)
mlflow.log_param("imgsz", 1280)
mlflow.log_param("batch", 8)

# Step 7: Log metrics (example metrics; actual metric access may differ)
# Replace 'metrics' with actual access code for your results
mlflow.log_metric("train_loss", trainer.metrics.get('train_loss', 0))
mlflow.log_metric("val_loss", trainer.metrics.get('val_loss', 0))
mlflow.log_metric("mAP_50", trainer.metrics.get('mAP_50', 0))
mlflow.log_metric("mAP_95", trainer.metrics.get('mAP_50-95', 0))

# Step 8: Save the trained model
model.save(trained_model_path)

# Step 9: Log the trained model as an artifact in MLflow
mlflow.log_artifact(trained_model_path, artifact_path="models")

# Step 10: End the MLflow run
mlflow.end_run()

