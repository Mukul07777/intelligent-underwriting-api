from PIL import Image
import pytesseract
import io

def analyze_image(file):
    image = Image.open(io.BytesIO(file.read()))
    text = pytesseract.image_to_string(image)
    return text
