import sys
import os
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image


class Interface(QWidget):
    def __init__(self):
        super().__init__()

        self.OF = QTextEdit(self)
        self.OF.move(300, 50)
        self.OF.resize(450, 450)

        self.Filename = QLineEdit(self)
        self.Filename.setPlaceholderText("Filename")
        self.Filename.move(300, 500)

        self.EncodeButton = QPushButton("Encode", self)
        self.EncodeButton.move(50, 50)
        self.EncodeButton.setToolTip("Click to encode your source")
        self.EncodeButton.clicked.connect(self.Encode)

        self.DecodeButton = QPushButton("Decode", self)
        self.DecodeButton.move(50, 150)
        self.DecodeButton.setToolTip("Click to decode your source")
        self.DecodeButton.clicked.connect(self.Decode)

        self.CancelButton = QPushButton("Cancel", self)
        self.CancelButton.move(50, 250)
        self.CancelButton.setToolTip("Click to cancel the Process")
        self.CancelButton.clicked.connect(self.close)

        self.InitUI()

    def InitUI(self):
        self.setGeometry(400, 400, 800, 550)
        self.setWindowTitle("QR Code De- and Encoder")
        self.setWindowIcon(QIcon("GUI Icon QR Code.png"))
        self.show()

    def Encode(self):
        qrcode = pyqrcode.create(self.OF.toPlainText(), error="H")
        qrcode.png(str(self.Filename.text()) + ".png", scale=10)
        self.close()

    def Decode(self):
        self.file = QFileDialog.getOpenFileName(self, "Open File", os.getenv("Desktop"))
        self.qrcode = str(decode(Image.open(self.file[0])))
        self.OF.setText(self.qrcode)
        


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = Interface()

    sys.exit(app.exec())
