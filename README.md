# Setup Python virtual environment
```
python3 -m venv virtualenv
source virtualenv/bin/activate
python3 -m pip install pdf2image pillow pytesseract
```
For pytesseract, followed the guide at https://pyimagesearch.com/2020/08/03/tesseract-ocr-for-non-english-languages/ and used https://github.com/tesseract-ocr/tessdata for french ocr.
```
export TESSDATA_PREFIX=/Users/sidakaneja/Developer/tesseract/tessdata
```

# Install poppler for pdf2image through brew
```
brew install poppler
```

# Extract images from the pdf files
```
# Command structure python3 extract.py <input_file_name> <Sidebar location: right or left>
>>> python3 extract.py ch_10 right                                                                                                                  
```
# Extract text from images
```
# Command structure python3 ocr.py <input_file_name> <config_to_pytesseract>
python3 ocr.py ch_10 "--oem 1"
```

The output file will be located in `extracted_text` with filename as `input_file_name`
