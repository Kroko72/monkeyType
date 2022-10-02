import pyautogui as pt
import time
import os
import easyocr


def make_screenshot() -> None:
    pt.screenshot("screenshot.png", region=(195, 440, 1700, 140))


def text_recognition(file_path: str) -> None:
    reader = easyocr.Reader(["ru", "en"])
    result = reader.readtext(file_path, detail=0, paragraph=True)
    print(result)
    for line in result:
        for sym in line:
            pt.keyDown(sym)
            pt.keyUp(sym)


def main() -> None:
    file_path = "C:/Users/User/PycharmProjects/pythonProject/monkeytype/screenshot.png"
    time.sleep(3)
    pt.PAUSE = 0.001
    make_screenshot()
    text_recognition(file_path=file_path)
    os.remove(file_path)


if __name__ == "__main__":
    main()
