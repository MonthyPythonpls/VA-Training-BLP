from PIL import Image
import os

def resize_images(input_path, output_path, target_size=(1280, 720)):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Loop through all files in the input directory
    for filename in os.listdir(input_path):
        input_file_path = os.path.join(input_path, filename)

        # Check if the file is an image
        if os.path.isfile(input_file_path) and any(input_file_path.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png']):
            # Open the image
            image = Image.open(input_file_path)

            # Resize the image
            resized_image = image.resize(target_size)

            # Save the resized image to the output directory
            output_file_path = os.path.join(output_path, filename)
            resized_image.save(output_file_path)

    print('success')

if __name__ == "__main__":
    # Set your input and output paths
    input_directory = "c:/Users/admin/Downloads/annotations/p/"
    output_directory = "c:/Users/admin/Downloads/annotations/p_labeled/"

    # Specify the target size
    target_size = (1280, 720)

    # Resize images and save them
    resize_images(input_directory, output_directory, target_size)
