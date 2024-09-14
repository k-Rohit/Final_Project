import os
import shutil
import subprocess

def convert_and_move(json_dir, val_size, test_size, output_format="polygon"):
    try:
        # Define the command to run labelme2yolo
        command = [
            "labelme2yolo",
            "--json_dir", json_dir,
            "--val_size", str(val_size),
            "--test_size", str(test_size),
            "--output_format", output_format  # Use polygon format
        ]
        
        # Run the command
        subprocess.run(command, check=True)
        print("Conversion completed successfully.")
        
        # Define source directories for the generated data
        yolo_labels_train = os.path.join(json_dir, "YOLODataset", "labels", "train")
        yolo_labels_val = os.path.join(json_dir, "YOLODataset", "labels", "val")
        yolo_labels_test = os.path.join(json_dir, "YOLODataset", "labels", "test")
        yolo_images_train = os.path.join(json_dir, "YOLODataset", "images", "train")
        yolo_images_val = os.path.join(json_dir, "YOLODataset", "images", "val")
        yolo_images_test = os.path.join(json_dir, "YOLODataset", "images", "test")
        
        # Define destination directories (your pre-defined structure)
        dest_labels_train = "/Users/kumarrohit/Desktop/MLOPS_LAB/Final_Project/data/train/labels"
        dest_labels_val = "/Users/kumarrohit/Desktop/MLOPS_LAB/Final_Project/data/val/labels"
        dest_labels_test = "/Users/kumarrohit/Desktop/MLOPS_LAB/Final_Project/data/test/labels"
        dest_images_train = "/Users/kumarrohit/Desktop/MLOPS_LAB/Final_Project/data/train/images"
        dest_images_val = "/Users/kumarrohit/Desktop/MLOPS_LAB/Final_Project/data/val/images"
        dest_images_test = "/Users/kumarrohit/Desktop/MLOPS_LAB/Final_Project/data/test/images"
        
        # Ensure destination directories exist
        os.makedirs(dest_labels_train, exist_ok=True)
        os.makedirs(dest_labels_val, exist_ok=True)
        os.makedirs(dest_labels_test, exist_ok=True)
        os.makedirs(dest_images_train, exist_ok=True)
        os.makedirs(dest_images_val, exist_ok=True)
        os.makedirs(dest_images_test, exist_ok=True)

        # Move labels and images to your custom structure
        move_files(yolo_labels_train, dest_labels_train)
        move_files(yolo_labels_val, dest_labels_val)
        move_files(yolo_labels_test, dest_labels_test)
        move_files(yolo_images_train, dest_images_train)
        move_files(yolo_images_val, dest_images_val)
        move_files(yolo_images_test, dest_images_test)

        print("Files moved to the custom directory structure successfully.")

    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running labelme2yolo: {e}")

def move_files(source_dir, dest_dir):
    # Move all files from source_dir to dest_dir
    for file_name in os.listdir(source_dir):
        source_file = os.path.join(source_dir, file_name)
        dest_file = os.path.join(dest_dir, file_name)
        shutil.move(source_file, dest_file)
        print(f"Moved {source_file} to {dest_file}")

# Example usage
if __name__ == "__main__":
    # Modify these paths and values as per your requirement
    json_dir = "/Users/kumarrohit/Desktop/MLOPS_LAB/Final_Project/data/raw_data"
    val_size = 0.10
    test_size = 0.10
    output_format = "polygon"  # Specify 'polygon' for the output format

    # Call the function to run the command and move the files
    convert_and_move(json_dir, val_size, test_size, output_format)
