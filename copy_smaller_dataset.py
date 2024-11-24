import os
import random
import shutil

def select_random_images(source_folder, destination_folder, num_images):
    # Get all image files from the source folder
    image_files = [f for f in os.listdir(source_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    
    # Randomly select the specified number of images
    selected_images = random.sample(image_files, min(num_images, len(image_files)))
    
    # Create the destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)
    
    # Copy selected images to the destination folder
    for image in selected_images:
        shutil.copy2(os.path.join(source_folder, image), destination_folder)

# Example usage
source_folder1 = "/mnt/c/large_datasets/archive/cell_images/Parasitized"
source_folder2 = "/mnt/c/large_datasets/archive/cell_images/Uninfected"
destination_folder1 = "/mnt/c/large_datasets/archive/cell_images/Parasitized_3000"
destination_folder2 = "/mnt/c/large_datasets/archive/cell_images/Uninfected_3000"

select_random_images(source_folder1, destination_folder1, 3000)
select_random_images(source_folder2, destination_folder2, 3000)