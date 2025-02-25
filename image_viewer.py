import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class ImageViewer(QWidget):
    def __init__(self, image_path):
        super().__init__()
        self.initUI(image_path)

    def initUI(self, image_path):
        # Set window title
        self.setWindowTitle('Image Viewer')

        # Create a QLabel to display the image
        label = QLabel(self)

        # Load the image
        pixmap = QPixmap(image_path)

        # Scale the image to fit the window while maintaining aspect ratio
        scaled_pixmap = pixmap.scaled(600, 400, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # Set the scaled image to the label
        label.setPixmap(scaled_pixmap)

        # Resize the window to fit the image
        self.resize(scaled_pixmap.width(), scaled_pixmap.height())


def main():
    app = QApplication(sys.argv)

    # Replace 'path/to/your/image.jpg' with the actual path to your image
    viewer = ImageViewer('path/to/your/image.jpg')
    viewer.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
