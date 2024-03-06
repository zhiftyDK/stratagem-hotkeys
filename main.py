import keyboard
import pyautogui
import requests
import difflib
import json

stratagemKeybind = "CTRL"
ocr_api_key = "K88953223088957"

def ocr(imagePath):
    payload = {'isOverlayRequired': False, "apikey": ocr_api_key, "language": "eng", "OCREngine": 2, "scale": True}
    with open(imagePath, 'rb') as f:
        response = requests.post('https://api.ocr.space/parse/image', files={imagePath: f}, data=payload)
        words = json.loads(response.content.decode())["ParsedResults"][0]["ParsedText"]
        result = [word for word in words.splitlines() if word.isupper()]
    return result[1:]

while True:
    if keyboard.is_pressed(stratagemKeybind):
        for i in range(1, 9):
            if keyboard.is_pressed(f"{i}"):
                print(f"Pressed: {stratagemKeybind} + {i}")
                refImage = pyautogui.screenshot()
                pyautogui.screenshot("temp.jpg", region=(0, 0, int(refImage.width / 5), int(refImage.height / 2)))
                stratagems = [word.strip() for word in open("stratagems.txt", "r").readlines()]
                for word in ocr("test.png"):
                    res = difflib.get_close_matches(word.lower(), stratagems)[0]
                    print(res)
                    
