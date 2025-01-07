from PyQt5.QtWidgets import QHBoxLayout, QLabel, QWidget, QFrame, QPushButton, QListWidgetItem
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag

class SignalItemWidget(QWidget):
    def __init__(self, text, list_item: QListWidgetItem, parent=None):
        super().__init__(parent)
        # self.setFrameShape(QFrame.StyledPanel)

        self.list_item = list_item  # 保存关联的 QListWidgetItem
        # 水平布局
        self.layout = QHBoxLayout(self)
        
        # 添加文本标签
        self.label = QLabel(text, self)
        self.layout.addWidget(self.label)
        
        # 其他控件可以根据需要添加
        self.button = QPushButton("Action", self)
        self.layout.addWidget(self.button)
        
        # 设置布局
        self.setLayout(self.layout)
        self.setAutoFillBackground(True)
        # 启用选择
        self.setStyleSheet("background-color: lightgray;")
        self.setAcceptDrops(True)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # 在这里处理点击事件
            # print(f"Item clicked: {self.label.text()}")
            self.list_item.setSelected(True)  # 手动将 QListWidgetItem 设置为选中

    def startDrag(self, event):
        #@创建 QDrag 对象并设置数据
        drag = QDrag(self)
        mime_data = QMimeData()
        mime_data.setText(self.label.text())  # 使用文本作为拖动数据
        drag.setMimeData(mime_data)

        print("startDrag")
        # 启动拖动操作
        drag.exec_(Qt.CopyAction | Qt.MoveAction)