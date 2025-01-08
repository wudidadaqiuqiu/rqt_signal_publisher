from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton

class DynamicForm(QWidget):
    def __init__(self, num_fields):
        super().__init__()
        self.num_fields = num_fields  # 外部传入的字段数量
        
        # 初始化UI
        self.init_ui()
    
    def init_ui(self):
        # 主布局
        self.layout = QVBoxLayout()

        # 创建一行，每行的文本框数量由 num_fields 决定
        self.create_row(self.num_fields)

        # 添加按钮来模拟动态增加行
        self.add_button = QPushButton("Add Row", self)
        self.add_button.clicked.connect(self.add_row)
        self.layout.addWidget(self.add_button)

        # 设置窗口布局
        self.setLayout(self.layout)
        self.setWindowTitle('Dynamic Form')
        self.show()

    def create_row(self, num_fields):
        """根据 num_fields 创建一行"""
        row_layout = QHBoxLayout()
        
        for _ in range(num_fields):
            line_edit = QLineEdit(self)
            row_layout.addWidget(line_edit)
        
        self.layout.addLayout(row_layout)

    def add_row(self):
        """动态添加一行"""
        self.create_row(self.num_fields)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    # 创建一个包含3个文本框的行
    form = DynamicForm(num_fields=3)
    sys.exit(app.exec_())
