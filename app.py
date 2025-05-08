import streamlit as st
from PIL import Image

st.title('Convert photo to black and white')

choise = st.radio('please select an item', ['camera', 'computer'])
if choise == 'camera':
    picture = st.camera_input("Take a picture")
else :
    picture = st.file_uploader(
        "please upload your image",
        type=["jpg", "jpeg", "png"]
    )
    
if picture is not None:
    image = Image.open(picture)
    
    gray_image = image.convert("L")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.image(image, caption="main photo", use_container_width=True)
    
    with col2:
        st.image(gray_image, caption="black and white photo", use_container_width=True)