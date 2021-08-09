"""
*** Coursera Python 3 Programming Specialization - final project  ***
"""

import zipfile
import math
from PIL import Image
import pytesseract
import cv2 as cv
import numpy as np

# Tesseract installation path   --   check if your path is the same
# pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'


# loading the face detection classifier
face_cascade = cv.CascadeClassifier('need/haarcascade_frontalface_default.xml')

# the rest is up to you!
serch_for = input("Serch for specific word in paper ")


with zipfile.ZipFile('need/images.zip', 'r') as zfile:
    for file in zfile.namelist():
        data = zfile.open(file)
        pic = Image.open(data)

        # array image
        pic_arr = np.array(pic)

        # pillow image
        pil_img = Image.fromarray(pic_arr)

        # Convert to grey collor
        gray = cv.cvtColor(pic_arr, cv.COLOR_BGR2GRAY)

        # serch text in image using tesseract
        text = pytesseract.image_to_string(gray)
        # text = "and"
        if serch_for in text:
            print("Results found in file {} ".format(file))

            # serch human faces in image using openCV
            faces = face_cascade.detectMultiScale(gray, 1.30)

            if len(faces) == 0:
                print("But ther were no faces in file!")
                continue

            # size of every image in the contac sheet
            size = (110, 110)

            img_faces = []

            for rec in faces.tolist():
                # Setup drawing context
                # drawing=ImageDraw.Draw(pil_img)
                # And draw the new box
                # drawing.rectangle((rec[0],rec[1],rec[0]+rec[2],rec[1]+rec[3]), outline="black")

                # crop the face image
                recorte = pil_img.crop((rec[0], rec[1], rec[0] + rec[2], rec[1] + rec[3]))

                # resize the image
                recorte.thumbnail(size)

                img_faces.append(recorte)

            first_image = img_faces[0]

            contact_sheet = Image.new(first_image.mode, (size[0] * 5, size[0] * (math.ceil(len(faces) / 5))))
            x = 0
            y = 0
            for img in img_faces:
                # paste the current image into the contact sheet
                contact_sheet.paste(img, (x, y))
                # update our X position. If it is going to be the width of the image, then we set it to 0
                # and update Y as well to point to the next "line" of the contact sheet.
                if x + size[0] == contact_sheet.width:
                    x = 0
                    y = y + size[0]
                else:
                    x = x + size[0]

            # display(contact_sheet)
            contact_sheet.show()
