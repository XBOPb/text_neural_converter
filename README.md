# text_neural_converter

Quick script to convert PDFs or any images to text files.
You must have pytesseract and poppler installed.
Default poppler path provided in script is C:\Program Files\Poppler\poppler-23.08.0\Library\bin.
You might want to change either the poppler path or its location inside the script.
Tesseract: https://github.com/tesseract-ocr/tesseract
Poppler: https://github.com/oschwartz10612/poppler-windows/releases/
Converted text file will be stored in the script folder as 'Converter.txt' after script execution.
For using the script, open command line at the folder of the program and type `python main.py` then provide an image file path.
Example: `python main.py myfile.png`
You can also add up to 2 arguments that will modify the text recognition.
First argument will change the default page segmentation mode(The default one is 6).
For additional information about Page segmentation refer to the list below.
Second argument will change the language of recognized file.
For list of supported languages refer to https://tesseract-ocr.github.io/tessdoc/Data-Files-in-different-versions.html


Page segmentation modes:
  0    Orientation and script detection (OSD) only.
  1    Automatic page segmentation with OSD.
  2    Automatic page segmentation, but no OSD, or OCR.
  3    Fully automatic page segmentation, but no OSD. (Default)
  4    Assume a single column of text of variable sizes.
  5    Assume a single uniform block of vertically aligned text.
  6    Assume a single uniform block of text.
  7    Treat the image as a single text line.
  8    Treat the image as a single word.
  9    Treat the image as a single word in a circle.
 10    Treat the image as a single character.
 11    Sparse text. Find as much text as possible in no particular order.
 12    Sparse text with OSD.
 13    Raw line. Treat the image as a single text line,
                        bypassing hacks that are Tesseract-specific.