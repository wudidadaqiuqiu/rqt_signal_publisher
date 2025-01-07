import sys
from PyQt5.QtWidgets import QApplication, QListWidget

class DraggableListWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数
        # self.setAcceptDrops(False)
        # self.setDragEnabled(False)
        self.setSelectionMode(QListWidget.SingleSelection)  # 启用单选模式

        # self.setDragEnabled(True)  # 启用拖拽
        # self.setDropIndicatorShown(True)  # 显示拖拽指示器
        # self.setAcceptDrops(True)  # 接受拖拽

    # def dragMoveEvent(self, event):
    #     # 允许拖拽移动
    #     event.accept()

    # def dropEvent(self, event):
    #     # 处理拖拽放下事件
    #     print("Dropped on list:", event.pos())
    #     event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # 创建自定义控件窗口并显示
    window = DraggableListWidget()
    window.show()
    
    sys.exit(app.exec_())
