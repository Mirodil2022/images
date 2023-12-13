from PIL import Image #Install pillow on your project --> pip install pillow
import os

def resize_image_with_lowered_quality(original_image_path, output_directory):
    # Check if the output directory exists; if not, create it
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Open the original image
    im = Image.open(original_image_path)

    # Get the file name without extension
    filename, file_extension = os.path.splitext(os.path.basename(original_image_path))

    # Define the new file path for saving the processed image in the output directory
    processed_image_path = os.path.join(output_directory, f"{filename}_xajm_kichraytirilgan.jpg")

    # Save the image with reduced quality (adjust the quality level as needed)
    im.save(processed_image_path, quality=80)  # Change the quality level (0-100) as required. (Hint: 80-85 is optimal quality for most images)

    return processed_image_path

# Example usage:
original_image_path = "rasmlar/photo.jpg"  # Replace this with your original image path
output_path = "processed_images"  # Replace this with the desired output directory

resulting_path = resize_image_with_lowered_quality(original_image_path, output_path)
print("Processed image saved at:", resulting_path)  # This will print the path of the processed image
