from PySide6 import QtWidgets, QtCore, QtGui
import sys


class MainWin(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.init_ui()
        self.setting_ui()
        self.show()

    def init_ui(self) -> None:
        self.central_widget = QtWidgets.QWidget()

        self.main_h_layout = QtWidgets.QHBoxLayout()

        # Using a list to store layouts and button groups for better organization
        self.group_layouts = [QtWidgets.QVBoxLayout() for _ in range(3)]
        self.button_groups = [QtWidgets.QButtonGroup() for _ in range(3)]

    def setting_ui(self) -> None:
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(self.main_h_layout)

        # Looping through layouts and button groups to create the UI
        for i in range(3):
            label = QtWidgets.QLabel('Null')
            for color in ['Red', 'Green', 'Yellow']:
                radio_button = QtWidgets.QRadioButton(color)
                self.button_groups[i].addButton(radio_button)
                self.group_layouts[i].addWidget(radio_button)

            self.group_layouts[i].addWidget(label)
            self.main_h_layout.addLayout(self.group_layouts[i])
            # Connecting buttonClicked signal with a lambda function to pass the layout index
            self.button_groups[i].buttonClicked.connect(lambda button, index=i: self.on_button_clicked(button, index))

    def on_button_clicked(self, button, layout_index):
        layout = self.group_layouts[layout_index]
        # Searching for the QLabel within the layout
        for i in range(layout.count()):
            widget = layout.itemAt(i).widget()
            if isinstance(widget, QtWidgets.QLabel):
                widget.setStyleSheet(f'background: {button.text()}')
                widget.setText(button.text())
                break  # Stop searching after finding the QLabel


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    root = MainWin()
    app.exec()
