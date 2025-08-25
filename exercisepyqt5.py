import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(700, 300, 250, 250)
        label = QLabel(self)
        label.setGeometry(0,0,250,250)
        #label = QLabel("Hello",self)
        #label.setAlignment(Qt.AlignCenter)
        pixmap = QPixmap("image1.png")
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        label.setGeometry(0, 0, label.width(), label.height())

def main():
    app = QApplication(sys.argv)
    window = MainWindow()   
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()