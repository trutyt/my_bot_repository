
import pytesseract
from PIL import Image

img = Image.open("phone_number.png")

pytesseract.pytesseract.tesseract_cmd =  "C:\Users\42195\Desktop\English work\pytesseract-0.3.10 (1).tar.gz"

custom_config = "--oem 3 --psm 6"

text = pytesseract.image_to_string(img, config=custom_config)
 
file_name = img.filename

file_name = file_name.split(".")[0]


with open(f"{file_name}.txt", "w") as text_file:
    text_file.write(text)


