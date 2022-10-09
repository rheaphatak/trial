from PIL import Image
#from pytesseract import pytesseract


import numpy as np
import cv2
import re
import pytesseract
from pytesseract import Output


import streamlit as st

st.title('Hi pls work!')



uploaded_file = st.file_uploader("Choose a file")


if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image)
    st.write('HEYY:')
    st.write(uploaded_file.name)
    #img = cv2.imread(uploaded_file)
    img = np.array(image)
    d = pytesseract.image_to_data(img, output_type=Output.DICT)


    conversation =''
    n_boxes = len(d['level'])
    for i in range(n_boxes):
        st.write('i \n')
        conversation += d['text'][i] + " "
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    st.write("conversation:" + conversation)
    st.image(img)
    #cv2.imshow(img)
    cv2.waitKey(0)
