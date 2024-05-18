from PySide6 import QtWidgets, QtCore, QtGui
import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.init_ui()
        self.__setting_ui()
        self.show()

    def init_ui(self) -> None:
        self.central_widget = QtWidgets.QWidget()
        self.main_h_layout = QtWidgets.QVBoxLayout()
        self.fields_layout = QtWidgets.QVBoxLayout()
        self.name_layout = QtWidgets.QHBoxLayout()
        self.phone_layout = QtWidgets.QHBoxLayout()
        self.list_widget = QtWidgets.QListWidget()
        self.name_label = QtWidgets.QLabel('Name')
        self.phone_label = QtWidgets.QLabel('Phone')
        self.name_line_edit = QtWidgets.QLineEdit('Entry your name')
        self.phone_line_edit = QtWidgets.QLineEdit('Entry your phone number')
        self.confirm_button = QtWidgets.QPushButton('Confirm')

    def __setting_ui(self) -> None:
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(self.main_h_layout)

        self.name_layout.addWidget(self.name_label)
        self.name_layout.addWidget(self.name_line_edit)

        self.phone_layout.addWidget(self.phone_label)
        self.phone_layout.addWidget(self.phone_line_edit)

        self.fields_layout.addLayout(self.name_layout)
        self.fields_layout.addLayout(self.phone_layout)

        self.main_h_layout.addWidget(self.list_widget)
        self.main_h_layout.addLayout(self.fields_layout)
        self.main_h_layout.addWidget(self.confirm_button)

        self.phone_line_edit.setInputMask('+7-000-000-00-00')

        self.load_contacts()

        self.confirm_button.clicked.connect(self.on_confirm_button_click)

    def load_contacts(self):
        try:
            with open('notebook.txt', 'r') as file:
                for line in file:
                    item = line.strip()
                    if item:
                        self.list_widget.addItem(QtWidgets.QListWidgetItem(item))
        except FileNotFoundError:
            pass  # Ignore if file not found

    def on_confirm_button_click(self) -> None:
        name = self.name_line_edit.text()
        phone = self.phone_line_edit.text()
        self.list_widget.addItem(QtWidgets.QListWidgetItem(f'{name} - {phone}'))

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        items = [self.list_widget.item(i).text() for i in range(self.list_widget.count())]
        with open('notebook.txt', 'w') as file:
            file.write('\n'.join(items))


if __name__ == 'main':
    app = QtWidgets.QApplication(sys.argv)
    root = MainWindow()
    app.exec()
