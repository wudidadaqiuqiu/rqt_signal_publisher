import sys
import subprocess
import time
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QWindow
from .get_window_id import get_window_id

class ParentWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Parent Window')
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout(self)
        self.button = QPushButton("Load Child Window", self)
        self.button.clicked.connect(self.load_child_window)
        self.layout.addWidget(self.button)
        
        self.child_process = None
        self.show()

    def load_child_window(self):
        # Launch the child window in a new process
        self.child_process = subprocess.Popen(['python3', './test/child_window.py'])

        # Give the child window a moment to launch
        time.sleep(1)

        # Get the X11 display and the window ID of the child process's window
        # display = Display()
        window_id = get_window_id(self.child_process.pid)
        print(f"Window ID: {window_id}")  # Debugging output

        # Try creating the window container
        try:
            window = QWindow.fromWinId(window_id)
            # window.setGeometry(100, 100, 400, 300)  # 设置合适的大小和位置
            widget = QWidget.createWindowContainer(window)
            
            widget.setWindowFlags(Qt.FramelessWindowHint)
            widget.setAttribute(Qt.WA_NoSystemBackground)
            widget.setParent(self)  # 设置父窗口
            
            self.layout.addWidget(widget)
        except Exception as e:
            print(f"Error while creating window container: {e}")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ParentWindow()
    sys.exit(app.exec_())
