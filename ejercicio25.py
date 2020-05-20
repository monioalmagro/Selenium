import cv2
import pytesseract

imagen = cv2.imread("ejemplo_pytesseract.png")
pytesseract.pytesseract.cmd = "C://program files//Tesseract-ORC//tesseract.exe"
texto  = pytesseract.image_to_string(imagen)
print(texto)