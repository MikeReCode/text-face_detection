# Text & Face Detection

### Description:

This program takes a zip folder with images from newspapers (other images that contain text and human faces).
The user enters a word he wants to search for in the text present in the image and if the word is found in the text, the program will detect all the human faces in the image and will create a new contact-sheet with all the faces.

### Necessary libraries:

- Pillow
- pytesseract
- opencv-python
- numpy

### Exemple:

If we were to use the image `a-0.png` in `images.zip` file and search for "Mark" wee should see the following image:

![](need/a-0_output.png)

Sometimes the word we are looking for is in the text but no face is found.