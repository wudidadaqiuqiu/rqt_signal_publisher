
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt
class ChildWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Child Window')
        # 必须设置为无边框窗口才能嵌入
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(100, 100, 400, 300)
        self.layout = QVBoxLayout(self)
        self.button = QPushButton("Child Window", self)
        # self.button.clicked.connect(self.load_child_window)
        self.layout.addWidget(self.button)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChildWindow()
    sys.exit(app.exec_())
