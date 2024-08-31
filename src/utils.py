import os
import time
from datetime import datetime
from fileinput import filename

import pyautogui
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"D:\Tesseract\tesseract.exe"

def create_folder(diretorio_base):
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    folder_path = os.path.join(diretorio_base, timestamp)
    os.makedirs(folder_path, exist_ok=True)
    return folder_path

def action(folder_path):
    screenshot = pyautogui.screenshot()
    filename = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.png'
    file_path = os.path.join(folder_path, filename)
    screenshot.save(file_path)
    print(f"Screenshot saved")
    OCR(file_path, folder_path)

def OCR(img_path, folder_path):
    text = pytesseract.image_to_string(img_path, lang='por')
    print(f"{img_path}: {text}")

    txt_filename = os.path.splitext(os.path.basename(img_path))[0] +'.txt'
    txt_path = os.path.join(folder_path, txt_filename)

    with open(txt_path, 'w', encoding='utf-8') as file:
        file.write(text)

if __name__ == "__main__":
    diretorio_base = 'screenshots'
    interval = 1800 # in sec

    while True:
        folder_path = create_folder(diretorio_base)
        action(folder_path)
        time.sleep(interval)