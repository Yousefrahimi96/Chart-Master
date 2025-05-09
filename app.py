import streamlit as st
from PIL import Image

# Display main image
st.image('./image/pic.webp')

# Login options in sidebar
login_option = st.sidebar.radio(
    "login/signup",
    ("login", "sign up")
)

if login_option == "login":
    with st.sidebar.form('login'):
        st.write('login here')
        username = st.text_input('Username')
        password = st.text_input('Password', type='password')
        submitted = st.form_submit_button('login')
        if submitted:
            pass
else:
    with st.sidebar.form('Sign up'):
        st.write('sign up here')
        username = st.text_input('Username')
        email = st.text_input('Email')
        password = st.text_input('Password', type='password')
        submitted = st.form_submit_button('Sign up')
        if submitted:
            pass

# Select image input method
choice = st.radio('please select an item', ['computer', 'camera'])

# Get image based on user selection
if choice == 'camera':
    picture = st.camera_input("Take a picture")
else:
    picture = st.file_uploader(
        "please upload your image",
        type=["jpg", "jpeg", "png"]
    )
    
# Process image if it exists
if picture is not None:
    image = Image.open(picture)
    
    # Convert to grayscale
    gray_image = image.convert("L")
    
    # Display images in two columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.image(image, caption="main photo", use_container_width=True)
    
    with col2:
        st.image(gray_image, caption="black and white photo", use_container_width=True)