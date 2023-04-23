import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QLabel, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Tạo TabWidget
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # Tạo các tab
        self.tab1 = QWidget()
        self.tab2 = QWidget()

        # Thêm các tab vào TabWidget
        self.tabs.addTab(self.tab1, "Tab 1")
        self.tabs.addTab(self.tab2, "Tab 2")

        # Thiết kế giao diện của Tab 1
        self.label1 = QLabel("This is Tab 1")
        layout1 = QVBoxLayout()
        layout1.addWidget(self.label1)
        self.tab1.setLayout(layout1)

        # Thiết kế giao diện của Tab 2
        self.label2 = QLabel("This is Tab 2")
        layout2 = QVBoxLayout()
        layout2.addWidget(self.label2)
        self.tab2.setLayout(layout2)

        # Đặt tiêu đề và kích thước cho cửa sổ
        self.setWindowTitle("Two Forms Example")
        self.setGeometry(100, 100, 400, 300)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
