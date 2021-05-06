

import numpy as np
from PIL import ImageGrab
from PIL import Image
import pytesseract
import cv2

left = 390
top = 265
right = 670
bottom = 545

screen_width = 1920
screen_height = 102

left += screen_width
right += screen_width
top += screen_height
bottom += screen_height

box_width = 30
box_offset = 31


def getBoard():
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # function takes a screencapture of sudoku board, then processes each 81 squares and pulls the number from it if
    # exists, adding it to an array to use as a sudoku grid
    grid =  [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],

    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],

    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]
    # grabbing image screenshot from coordinates, cropped image to just grab sudoku board
    box = [left, top, right, bottom]
    printscreen_pil = ImageGrab.grab( bbox=box, include_layered_windows=False, all_screens=True)
    printscreen_pil.show()

    # storing image as image format
    img = Image.Image.convert(printscreen_pil, 'L')
    img.show()
    box_size = img.height / 9
    L = 0
    T = - box_size
    R = 0
    B = 0

    # processing each of the 81 squares
    for x in range(81):
        # setting the individual square's positions, according to the number of square
        if x % 9 == 0:
            # if currently processing a far left square, specifically set left and top values
            T += box_size
            B = T + box_size
            L = 0
        else:
            L += box_size
        R = L + box_size

        # cropping the image to the size/position of the current square
        box = [left, top, right, bottom]
        imgCrop = img.crop((L+5, T+5, R-2, B-2))

        # converting screenshot to image and pulling text from it
        img_text = pytesseract.image_to_string(imgCrop, lang='eng', config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
        num = 0
        for char in img_text:
            if char.isdigit():
                num = int(char)
        # if image thinks its a 4 -> cut top bit off of image and recheck, because '1's get mistaken for '4's
        if num == 4:
            #imgCrop.show()
            imgCrop = imgCrop.crop((0, 4, imgCrop.width-5, imgCrop.height))
            #imgCrop.show()
            img_text = pytesseract.image_to_string(imgCrop, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
            found4 = False
            for char in img_text:
                if char.isdigit():
                    if int(char) == 4:
                        found4 = True
            if found4 == False:
                num = 1
            print(num)
        row = (x // 9)
        col = x % 9
        grid[row][col] = num

    return grid


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    getBoard()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
