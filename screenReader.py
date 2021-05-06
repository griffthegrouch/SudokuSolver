

import numpy as np
from PIL import ImageGrab
from PIL import Image
import pytesseract
import cv2

left = 391
top = 262
right = 671
bottom = 542

screen_width = 1920
screen_height = 105

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
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],

    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],

    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 0],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
    # grabbing image screenshot from coordinates
    printscreen_pil = ImageGrab.grab(bbox=None, include_layered_windows=False, all_screens=True)
    # cropping image to just grab sudoku board
    printscreen_crop = printscreen_pil.crop((left, top, right, bottom))
    # converting image to array
    # printscreen_numpy = np.array(printscreen_crop.getdata(), dtype='uint8') \
    #     .reshape((printscreen_crop.size[1], printscreen_crop.size[0], 3))
    # img = Image.fromarray(printscreen_numpy)
    img = printscreen_crop.convert('L')
    img.show()
    # setting starting image crop positions
    top0 = top - box_width
    left0 = left

    # processing each of the 81 squares
    for x in range(81):

        # setting the individual square's position
        if x % 9 == 0:
            # if currently processing a far left square, specifically set left and top valuess
            top0 += box_offset
            left0 = left
        else:
            left0 += box_offset
        right0 = left0 + box_width
        bottom0 = top0 + box_width

        # cropping the image to the size/position of the current square
        img = img.crop((left0+5, top0+3, right0-5, bottom0-5))

        # cv2.imshow('window', printscreen_numpy)
        #printscreen_numpy = cv2.cvtColor(printscreen_numpy, cv2.COLOR_BGR2GRAY)

        # converting screenshot to image and pulling text from it

        # if x > 40:
        img.show()
        img_text = pytesseract.image_to_string(img)
        num = 0
        for char in img_text:
            if char.isdigit():
                num = int(char)
        # print(str(x) + "= " + str(num))

        row = (x // 9)
        col = x % 9
        grid[row][col] = num

    return grid
        # input()
    # if cv2.waitKey(25) & 0xff == ord('q'):
    #     cv2.destroyAllWindows()
    #     break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    getBoard()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
