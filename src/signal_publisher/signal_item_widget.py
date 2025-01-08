from PyQt5.QtWidgets import (QHBoxLayout, QLabel, QWidget, QFrame, 
    QPushButton, QListWidgetItem, QApplication)
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag, QPixmap

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
        # self.setAcceptDrops(True)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # 在这里处理点击事件
            # print(f"Item clicked: {self.label.text()}")
            self.list_item.setSelected(True)  # 手动将 QListWidgetItem 设置为选中
            self.dragStartPosition = event.pos()
    
    def mouseMoveEvent(self, event):
        if not (event.buttons() == Qt.LeftButton):
            return
        if ((event.pos() - self.dragStartPosition).manhattanLength()
            < QApplication.startDragDistance()):
            return
        self.startDrag(event)
        
    def startDrag(self, event):
        # print("Start drag")
        # 开始拖拽
        mime_data = QMimeData()
        mime_data.setText(self.label.text())  # 设置拖拽的数据
        
        drag = QDrag(self)
        drag.setMimeData(mime_data)
        # drag.setHotSpot(event.pos())  # 设置拖拽的热点位置

        pixmap = QPixmap(self.size())
        self.render(pixmap)
        drag.setPixmap(pixmap)
            
        drag.exec_(Qt.MoveAction)  # 执行拖拽
