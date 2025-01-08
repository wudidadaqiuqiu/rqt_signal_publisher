import sys
from PyQt5.QtWidgets import QApplication, QListWidget

class DraggableListWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数
        # self.setAcceptDrops(False)
        # self.setDragEnabled(False)
        self.setSelectionMode(QListWidget.SingleSelection)  # 启用单选模式


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # 创建自定义控件窗口并显示
    window = DraggableListWidget()
    window.show()
    
    sys.exit(app.exec_())
