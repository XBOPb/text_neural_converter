import sys
import os
import pytesseract
import PIL.Image
from pdf2image import convert_from_path

def convert_to_text(image, config):
    name, extension = os.path.splitext(image)
    
    if extension == '.pdf':
        poppler_path = r"C:/Program Files/Poppler/poppler-23.08.0/Library/bin"
        image = convert_from_path(image_path, poppler_path=poppler_path)
        text = ''
        for page in image:
            page = pytesseract.image_to_string(page, config=config)
            text += page
    else:
        pil_image = PIL.Image.open(image)
        text = pytesseract.image_to_string(pil_image, config=config)
    return text

def write_to_file(text):
    with open('converted.docx', 'w') as file:
        file.write(text)

if __name__ == '__main__':
    image_path = sys.argv[1]        
    tesseract_mode = 6                  # Default mode
    if len(sys.argv) == 3:
        tesseract_mode = sys.argv[2]    # Change default recognition mode
    config = f'--psm {tesseract_mode} --oem 3'
    converted = convert_to_text(image_path, config)
    write_to_file(converted)
