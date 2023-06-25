import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import cv2
import openai
from dotenv import load_dotenv
import urllib

import os
load_dotenv(".env")
openai.api_key = os.environ["OPENAI_API_KEY"]

st.title('How Would You Look?')

with st.container():
    col1, col2 = st.columns((1,3))
    with col1:
        style = st.radio(
            "What would you like to try?",
            ('Locs', 'Curly', 'Manbun', 'Mohawk', 'Spiky', 'Sauve'))
        if style == 'Locs':
            prompt_str = "jamaican locs men's hairstyle "
        elif style == 'Curly':
            prompt_str = "brazilian curly men's hairstyle "
        elif style == 'Manbun':
            prompt_str = "french manbun men's hairstyle "
        elif style == 'Mohawk':
            prompt_str = "American mohawk men's hairstyle "
        elif style == 'Spiky':
            prompt_str = "footballer spiky men's hairstyle "
        elif style == 'Sauve':
            prompt_str = "Uptight New York investment banker hairstyle "

        value = st.slider(
            'Mask depth',
            4, 0, 4)
        st.markdown('Default depth of mask for the image is 4, which means that the top 1/4th of the \
                image is masked and the hair style is placed in this region. If your image has more\
                room on the top, decrease this number')

    with col2:
        image_list = ['locs.png', 'curly.png', 'manbun.png', 'mohawk.png', 'spiky.png', 'suave.png']
        resizedImages = []
        for image in image_list:
            img = Image.open(image)
            resizedImg = img.resize((120, 120), Image.ANTIALIAS)
            resizedImages.append(resizedImg)

        with st.container():
            col1, col2, col3 = st.columns(3)
            with col1:
                st.image(resizedImages[0])
                st.write('locs')
            with col2:
                st.image(resizedImages[1])
                st.write('curly')
            with col3:
                st.image(resizedImages[2])
                st.write('manbun')

        with st.container():
            col1, col2, col3 = st.columns(3)
            with col1:
                st.image(resizedImages[3])
                st.write('mohawk')
            with col2:
                st.image(resizedImages[4])
                st.write('spiky')
            with col3:
                st.image(resizedImages[5])
                st.write('sauve')


        st.caption('Upload your image ')
        uploaded_file = st.file_uploader("", type=['png'])


        if uploaded_file is not None:

            st.image(uploaded_file, width=512)
            # img = Image.open(uploaded_file.getvalue())
            img = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)
            dim = (1024, 1024)
            resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
            cv2.imwrite("pro_pic.png", resized)

            # create a mask
            from PIL import Image

            width = 1024
            height = 1024
            mask = Image.new("RGBA", (width, height), (0, 0, 0, 1))  # create an opaque image mask

            # set the bottom half to be transparent
            for x in range(width):
                for y in range(0, height // value):  # only loop over the top 1/4th of the mask
                    # set alpha (A) to zero to turn pixel transparent
                    alpha = 0
                    mask.putpixel((x, y), (0, 0, 0, alpha))

            # save the mask
            mask_name = "mask.png"
            mask.save(mask_name)

            if st.button('Bring it on'):
                with st.spinner(text="In progress..."):
                    edit_response = openai.Image.create_edit(
                        image=open("pro_pic.png", "rb"),  # from the generation section
                        mask=open("mask.png", "rb"),  # from right above
                        prompt=prompt_str,  # from the generation section
                        n=1,
                        size="1024x1024",
                        response_format="url",
                    )

                    st.image(edit_response['data'][0]['url'], width=512)





