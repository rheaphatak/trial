#from PIL import Image
#from pytesseract import pytesseract

import cv2
import re
import pytesseract
from pytesseract import Output


import streamlit as st

st.title('Hi pls work!')



uploaded_file = st.file_uploader("Choose a file")


if uploaded_file is not None:
    st.image(uploaded_file.name)
'''
if uploaded_file is not None:
    img = cv2.imread(uploaded_file.name)

    d = pytesseract.image_to_data(img, output_type=Output.DICT)


    conversation =''
    n_boxes = len(d['level'])
    for i in range(n_boxes):
        conversation += d['text'][i] + " "
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    st.write("conversation:" + conversation)
    cv2.imshow(img)
    cv2.waitKey(0)
'''
