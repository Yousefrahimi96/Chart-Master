# Photo-Converter

A simple web application built with Streamlit that allows users to upload photos or take pictures with their camera and convert them to grayscale.

## Features

- User authentication system with login and sign-up options
- Two methods for image input:
  - Upload images from computer (supports JPG, JPEG, PNG)
  - Take pictures directly with your device camera
- Real-time image conversion to grayscale
- Side-by-side display of original and converted images

## Installation

1. Clone this repository:
```
git clone https://github.com/yourusername/Photo-Converter.git
cd Photo-Converter
```

2. Install required dependencies:
```
pip install -r requirements.txt
```

## Dependencies

- Streamlit (v1.45.0)
- Pillow (v11.2.1)

## Usage

1. Run the application:
```
streamlit run app.py
```

2. Open your browser and go to the provided URL (typically http://localhost:8501)

3. Using the application:
   - Choose login or sign-up option from the sidebar
   - Select between computer upload or camera input
   - If using computer upload, select an image file (JPG, JPEG, or PNG)
   - If using camera, take a picture with your device camera
   - View the original and grayscale versions side by side

## Project Structure

```
Photo-Converter/
├── app.py              # Main application file
├── requirements.txt    # Required dependencies
├── image/              # Directory containing static images
│   └── pic.webp        # Main header image
└── README.md           # This file
```

## Future Improvements

- Add more image processing options (brightness adjustment, filters, etc.)
- Implement the backend for user authentication
- Add image download functionality
- Implement image sharing features

## License

MIT

## Author

yousefrahimi101@gmail.com
