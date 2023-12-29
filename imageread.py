

import pytesseract
from pytesseract import Output
from PIL import Image
import cv2

from deep_translator import GoogleTranslator
from deep_translator import PonsTranslator

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img_path1 = 'ifuw77.jpg'
text = pytesseract.image_to_string(img_path1,lang='eng')

translated = GoogleTranslator(source='en', target='sv').translate(text)
#translated = PonsTranslator(source='english', target='swedish').translate(text[0:40], return_all=False)

print(translated)
