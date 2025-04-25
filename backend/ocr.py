import easyocr
import cv2
import numpy as np

reader = easyocr.Reader(['en'], gpu=False)

def extract_text_from_image(image_bytes):
    file_bytes = np.asarray(bytearray(image_bytes), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    filtered = cv2.bilateralFilter(gray, 11, 17, 17)
    _, thresh = cv2.threshold(filtered, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    result = reader.readtext(thresh, detail=0)
    return "\n".join(result)
