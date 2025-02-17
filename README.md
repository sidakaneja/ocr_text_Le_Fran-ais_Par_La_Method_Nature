
    python3 -m venv virtualenv ( virtualenv is just a name that I setup for the enviroment)
    source virtualenv/bin/activate
    python3 -m pip install pdf2image pillow pytesseract


    brew install poppler

    To setup pytesseract used: https://pyimagesearch.com/2020/08/03/tesseract-ocr-for-non-english-languages/
     which says to clone https://github.com/tesseract-ocr/tessdata


    export TESSDATA_PREFIX=/Users/sidakaneja/Developer/tesseract/tessdata
    

    python3 extract.py ch_10 right                                                         
    python3 ocr.py ch_10 "--oem 1"                                                         