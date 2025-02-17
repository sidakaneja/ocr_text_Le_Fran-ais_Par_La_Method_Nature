from pdf2image import convert_from_path
from PIL import Image
import os
import pytesseract
import argparse
import sys
import os
import re

# Function to extract numerical values from filenames


def extract_page_number(filename):
    # Find first number in filename
    match = re.search(r'ch_(\d+)_page_(\d+)', filename)
    # Convert to int for correct sorting
    print(filename, int(match.group(2)) if match else float('inf'))
    return int(match.group(2)) if match else float('inf')


output_folder = "cropped_images"
parser = argparse.ArgumentParser(
    prog='ocr.py',
    description='Extract text from images')

parser.add_argument("file_name", action="store", help="Name of file to ocr")
parser.add_argument("parser_arg", action="store", help="pytesseract arg")

args = parser.parse_args()
output_text_file = "./extracted_text/" + args.file_name

# Ensure the folder exists
if not os.path.exists(output_folder):
    print(f"Error: Folder '{output_folder}' not found.")
    exit()

# Get a list of all image files in the folder
image_files = [f for f in os.listdir(output_folder)
               if f.endswith(('.png', '.jpg', '.jpeg'))
               and f.startswith(args.file_name)]

image_files = sorted(image_files, key=extract_page_number)


print(f"Extracting text from {image_files}")
# Extract text from each image and store in a list
extracted_texts = []
for image_file in image_files:
    image_path = os.path.join(output_folder, image_file)
    img = Image.open(image_path)

    # Extract text using Tesseract OCR
    # Set language to French ('fra')
    text = pytesseract.image_to_string(img, lang="fra", config=args.parser_arg)

    # Store extracted text
    # extracted_texts.append(f"--- Extracted from {image_file} ---\n{text}\n")
    extracted_texts.append(f"{text}\n")

# Combine all extracted text
full_extracted_text = "\n".join(extracted_texts)

# Save extracted text to a file
with open(output_text_file, "w", encoding="utf-8") as f:
    f.write(full_extracted_text)

print(
    f"Text extraction complete! Extracted text saved to '{output_text_file}'")

processed_text = [text for text in full_extracted_text.split('\n') if text]

for index, line in enumerate(processed_text):
    print(index, line)
