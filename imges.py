from PIL import Image
from pytesseract import *

pytesseract.tesseract_cmd = r'D:\Tesseract\tesseract.exe'

img = Image.open(r"C:\Users\ramon\OneDrive\Desktop\Tesseract\image3.jpg")

resultado = pytesseract.image_to_string(img)

print(resultado)