import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor

class SignalPublisherWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数
        self.setWindowTitle("QWidget 继承示例")
        # print(self.width(), self.height())
        self.setGeometry(100, 100, 400, 300)  # 设置窗口的位置和大小

    def paintEvent(self, event):
        # 重写 paintEvent 方法，进行自定义绘制
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # 开启抗锯齿
        painter.setBrush(QColor(0, 255, 0))  # 设置填充颜色
        painter.setPen(Qt.black)  # 设置边框颜色
        painter.drawEllipse(50, 50, 100, 100)  # 绘制一个圆形

        painter.setBrush(QColor(255, 0, 0))  # 改变填充颜色
        painter.drawRect(200, 50, 100, 100)  # 绘制一个矩形

    def mousePressEvent(self, event):
        # 重写 mousePressEvent 方法，处理鼠标点击事件
        if event.button() == Qt.LeftButton:
            print("鼠标点击事件：", event.pos())
            self.update()  # 触发重绘

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # 创建自定义控件窗口并显示
    window = SignalPublisherWidget()
    window.show()
    
    sys.exit(app.exec_())
