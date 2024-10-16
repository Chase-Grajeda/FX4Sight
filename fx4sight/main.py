import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import quant


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test Window")
        self.setGeometry(100, 100, 600, 400)  # x, y, width, height
        self.show()


if __name__ == "__main__":
    print("Running application")
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec())
