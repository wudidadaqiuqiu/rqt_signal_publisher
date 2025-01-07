import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QHBoxLayout, QListWidgetItem


class SignalPublisherWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数
        # 布局
        self.layout = QVBoxLayout()
        
        # 创建 QListWidget
        self.list_widget = QListWidget()
        self.layout.addWidget(self.list_widget)

        # 创建按钮布局
        self.button_layout = QHBoxLayout()
        
        # 添加按钮
        self.add_button = QPushButton("Add Widget Item")
        self.add_button.clicked.connect(self.add_item)
        self.button_layout.addWidget(self.add_button)
        
        # 删除按钮
        self.remove_button = QPushButton("Remove Item")
        self.remove_button.clicked.connect(self.remove_item)
        self.button_layout.addWidget(self.remove_button)

        # 将按钮布局添加到主布局中
        self.layout.addLayout(self.button_layout)

        # 设置窗口的布局
        self.setLayout(self.layout)

    def add_item(self):
        # 创建一个自定义的 QWidget，可以是一个按钮、标签等
        custom_widget = QPushButton("Custom Button")
        
        # 创建一个 QListWidgetItem
        list_item = QListWidgetItem(self.list_widget)
        
        # 将自定义 widget 设置为该 item 的 widget
        list_item.setSizeHint(custom_widget.sizeHint())  # 设置大小
        self.list_widget.setItemWidget(list_item, custom_widget)  # 设置 widget

    def remove_item(self):
        # 删除选中的项
        selected_items = self.list_widget.selectedItems()  # 获取选中的项
        if selected_items:
            for item in selected_items:
                self.list_widget.takeItem(self.list_widget.row(item))  # 删除该项

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # 创建自定义控件窗口并显示
    window = SignalPublisherWidget()
    window.show()
    
    sys.exit(app.exec_())
