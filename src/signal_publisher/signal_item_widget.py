import inspect
from PyQt5.QtWidgets import (QHBoxLayout, QLabel, QWidget, QFrame, 
    QPushButton, QListWidgetItem, QApplication, QLineEdit)
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag, QPixmap
from .signal_eval import *

class SignalItemWidget(QWidget):
    def __init__(self, text, list_item: QListWidgetItem, parent=None):
        super().__init__(parent)
        self.list_item = list_item  # 保存关联的 QListWidgetItem
        # 水平布局
        self.layout = QHBoxLayout(self)
        
        # 添加文本标签
        self.label = QLabel(text, self)
        self.layout.addWidget(self.label)
        
        # # 其他控件可以根据需要添加
        # self.button = QPushButton("Action", self)
        # self.layout.addWidget(self.button)
        
        # 设置布局
        self.setLayout(self.layout)
        self.setAutoFillBackground(True)
        # 启用选择
        self.setStyleSheet("background-color: lightgray;")
        # self.setAcceptDrops(True)

    def load_signal(self, signal: type):
        si = inspect.signature(signal)
        for param in si.parameters:
            # print(param)
            line_edit = QLineEdit(self)
            # 设置占位符文字
            line_edit.setPlaceholderText(param)
            self.layout.addWidget(line_edit)

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
        call_text: str
        try:
            call_text = self.try_eval()
            # print(call_text)
        except Exception as e:
            print(e)
        self.startDrag(event, call_text)
        
    def try_eval(self):
        text_edits: list[QLineEdit] = self.findChildren(QLineEdit)
        param = ''
        for text_edit in text_edits:
            param += text_edit.text() + ','
        param = param[:-1]
        res = f"{self.label.text()}({param})"  # 设置拖拽的数据
        eval(res)
        return res
    
    def startDrag(self, event, call_text_):
        mime_data = QMimeData()
        mime_data.setText(call_text_)
        drag = QDrag(self)
        drag.setMimeData(mime_data)
        # drag.setHotSpot(event.pos())  # 设置拖拽的热点位置

        pixmap = QPixmap(self.size())
        self.render(pixmap)
        drag.setPixmap(pixmap)
            
        drag.exec_(Qt.MoveAction)  # 执行拖拽
