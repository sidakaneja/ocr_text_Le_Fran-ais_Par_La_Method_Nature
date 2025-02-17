from pdf2image import convert_from_path
from PIL import Image
import os
import pytesseract
import argparse

# export TESSDATA_PREFIX=/Users/sidakaneja/Developer/tesseract/tessdata
parser = argparse.ArgumentParser(
    prog='ocr.py',
    description='Extract text from images')

parser.add_argument("file_name", action="store", help="Name of file to ocr")
parser.add_argument("sidebar_placement", choices=[
                    "left", "right"], help="Name of file to ocr")

args = parser.parse_args()

# Define the PDF file path
pdf_path = args.file_name
output_folder = "cropped_images"  # Folder to save cropped images

# Ensure the output directory exists
os.makedirs(output_folder, exist_ok=True)

# Convert the PDF to images
images = convert_from_path("./chapters/" + pdf_path + ".pdf")

# Loop through each page, apply cropping, and save as PNG
for i, img in enumerate(images):
    width, height = img.size  # Get page dimensions

    # Define alternating crop settings
    start_index = 0 if args.sidebar_placement == "right" else 1
    if (start_index + i) % 2 == 0:  # Odd-numbered pages (0-based index) - Sidebar on the right
        crop_box = (0, 160, width - 325, height - 135)  # Keep left, crop right
    else:  # Even-numbered pages - Sidebar on the left
        crop_box = (350, 160, width, height - 135)  # Crop left, keep right

    # Apply cropping
    cropped_img = img.crop(crop_box)

    # Save cropped image as PNG
    cropped_img.save(os.path.join(output_folder, f"{pdf_path}_page_{i+1}.png"))

print(f"All {len(images)} pages have been cropped and saved as PNG files in '{output_folder}'")
