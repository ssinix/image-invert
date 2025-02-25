# Image Viewer & Inverter

A simple desktop application built with PyQt5 that allows users to view and invert images.

## Features

- Open and display common image formats (PNG, JPG, BMP, GIF, XPM)
- View images at a scaled size while maintaining aspect ratio
- Invert image colors with a single click
- Toggle between original and inverted views

## Screenshot

*[Add a screenshot of your application here]*

## Requirements

- Python 3.6+
- PyQt5

## Installation

1. Ensure you have Python installed on your system.
2. Install the required dependencies:

```bash
pip install PyQt5
```

## Usage

Run the application by executing the main script:

```bash
python image_viewer.py
```

### Instructions:

1. Click the "Choose Image" button to open a file dialog.
2. Select an image file (supported formats: PNG, JPG, BMP, GIF, XPM).
3. Once the image is loaded, click the "Invert Image" button to toggle between the original and inverted views.

## Development History

This project was developed in two phases:
1. Initial implementation of a basic image viewer (image_viewer.py) to test image loading functionality.
2. Extended implementation (in paste.txt) to add image inversion capabilities.

## How It Works

The application uses PyQt5 to create a simple GUI with the following components:

- QWidget as the main window
- QLabel to display the image
- QPushButton widgets for interaction
- QFileDialog for opening image files

The image inversion works by:
1. Converting the QPixmap to a QImage
2. Accessing each pixel in the image
3. Inverting the RGB values (subtracting each value from 255)
4. Converting back to a QPixmap for display

## Future Improvements

Potential enhancements to consider:
- Add more image manipulation options (brightness, contrast, etc.)
- Implement zoom functionality
- Add ability to save modified images
- Create a more sophisticated UI with menus and shortcuts

## License

*This project is licensed under the MIT license - see the LICENSE file for details.*

## Acknowledgements
This project was developed as part of the **PROJ201 Undergraduate Project Course** at **Sabancı University**. The implementation follows the requirements specified in the homework assignment.
