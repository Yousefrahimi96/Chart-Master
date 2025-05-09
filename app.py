import streamlit as st
from PIL import Image

st.image('./image/pic.webp')

login_option = st.sidebar.radio(
    "login/signup",
    ("login", "signup")
)

if login_option == "login":
    pass
    

choise = st.radio('please select an item', ['computer', 'camera'])
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