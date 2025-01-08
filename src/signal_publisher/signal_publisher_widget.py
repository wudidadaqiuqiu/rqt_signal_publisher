import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QHBoxLayout, QListWidgetItem
from .draggable_list_widget import DraggableListWidget
from .signal_item_widget import SignalItemWidget
from .signal_eval import *
class SignalPublisherWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数
        # 布局
        self.layout = QVBoxLayout()

        self.list_widget = DraggableListWidget()
        self.layout.addWidget(self.list_widget)

        # 设置窗口的布局
        self.setLayout(self.layout)
        global custom_globals
        for k, v in custom_globals.items():
            widget = self.add_item(k)
            widget.load_signal(v)

    def add_item(self, label: str = None):
        item_count = self.list_widget.count()  # 获取当前列表项的数量
        # self.list_widget.addItem(f"Item {item_count + 1}")  # 添加新项
        list_item = QListWidgetItem(self.list_widget)
        item_widget = SignalItemWidget(f"Item {item_count}" if label is None else label, list_item, self)
        item_widget.setFixedHeight(50)
        list_item.setSizeHint(item_widget.sizeHint())  # 设置项的大小
        self.list_widget.setItemWidget(list_item, item_widget)
        return item_widget

    def remove_item(self):
        # 删除选中的项
        selected_items = self.list_widget.selectedItems()  # 获取选中的项
        print("Selected items:", selected_items)  # 打印选中的项
        if selected_items:
            print("Deleting items")
            for item in selected_items:
                widget = self.list_widget.itemWidget(item)
                if widget:
                    print("Deleting widget")
                    widget.deleteLater()
                print("Deleting item")
                self.list_widget.removeItemWidget(item)  # 从列表中移除该 widget
                self.list_widget.takeItem(self.list_widget.row(item))  # 删除 QListWidgetItem

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # 创建自定义控件窗口并显示
    window = SignalPublisherWidget()
    window.show()
    
    sys.exit(app.exec_())
