import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QFileDialog
)
from PyQt5.QtGui import QPixmap, QImage, QColor
from PyQt5.QtCore import Qt


class ImageViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.original_pixmap = None
        self.inverted_pixmap = None
        self.current_pixmap = None
        self.is_inverted = False  # Track if the image is currently inverted
        self.initUI()

    def initUI(self):
        # Set window title
        self.setWindowTitle('Image Viewer')

        # Create a main vertical layout
        main_layout = QVBoxLayout()

        # Create a horizontal layout for buttons
        button_layout = QHBoxLayout()

        # Create a button to open file dialog
        self.open_button = QPushButton('Choose Image', self)
        self.open_button.clicked.connect(self.open_image)

        # Create an invert button
        self.invert_button = QPushButton('Invert Image', self)
        self.invert_button.clicked.connect(self.invert_image)
        self.invert_button.setEnabled(False)  # Disabled until an image is loaded

        # Add buttons to button layout
        button_layout.addWidget(self.open_button)
        button_layout.addWidget(self.invert_button)

        # Create a label to display the image
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setMinimumSize(400, 300)  # Set minimum size for the label

        # Add layouts and label to main layout
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.image_label)

        # Set the layout for the window
        self.setLayout(main_layout)

        # Set initial window size
        self.resize(600, 500)

    def resizeEvent(self, event):
        """Handle window resize events"""
        super().resizeEvent(event)
        # Update the image when window is resized
        self.update_display()

    def update_display(self):
        """Update the displayed image based on current window size"""
        if self.original_pixmap:
            # Determine which pixmap to use (original or inverted)
            source_pixmap = self.inverted_pixmap if self.is_inverted and self.inverted_pixmap else self.original_pixmap

            # Get available size (accounting for layout margins)
            available_width = self.image_label.width() - 10  # Subtract some margin
            available_height = self.image_label.height() - 10  # Subtract some margin

            # Scale the image to fit the available space while maintaining aspect ratio
            self.current_pixmap = source_pixmap.scaled(
                available_width,
                available_height,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )

            # Set the scaled image to the label
            self.image_label.setPixmap(self.current_pixmap)

    def open_image(self):
        # Open file dialog to choose an image
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            'Open Image File',
            '',
            'Images (*.png *.xpm *.jpg *.bmp *.gif)'
        )

        # Check if a file was selected
        if file_name:
            # Load the image
            self.original_pixmap = QPixmap(file_name)

            # Enable the invert button
            self.invert_button.setEnabled(True)

            # Reset inversion state
            self.is_inverted = False
            self.inverted_pixmap = None

            # Update the display with the new image
            self.update_display()

            # Optionally, set window title to show filename
            self.setWindowTitle(f'Image Viewer - {file_name.split("/")[-1]}')

    def invert_image(self):
        # Check if an image is loaded
        if self.original_pixmap is None:
            return

        # Toggle the inversion state
        self.is_inverted = not self.is_inverted

        if self.is_inverted and self.inverted_pixmap is None:
            # Convert pixmap to QImage for pixel-level manipulation
            image = self.original_pixmap.toImage()

            # Invert the image
            for x in range(image.width()):
                for y in range(image.height()):
                    # Get the pixel color
                    pixel_color = QColor(image.pixel(x, y))

                    # Invert the RGB values
                    inverted_color = QColor(
                        255 - pixel_color.red(),
                        255 - pixel_color.green(),
                        255 - pixel_color.blue()
                    )

                    # Set the inverted pixel
                    image.setPixel(x, y, inverted_color.rgb())

            # Convert back to pixmap and cache the inverted version
            self.inverted_pixmap = QPixmap.fromImage(image)

        # Update the display
        self.update_display()


def main():
    app = QApplication(sys.argv)
    viewer = ImageViewer()
    viewer.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()