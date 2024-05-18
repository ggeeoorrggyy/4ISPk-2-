from PySide6 import QtWidgets, QtCore, QtGui
import sys


class MainWin(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.init_ui()
        self.__setting_ui()
        self.show()

    def init_ui(self) -> None:
        self.central_widget = QtWidgets.QWidget()
        self.main_v_layout = QtWidgets.QVBoxLayout()
        self.tools_h_layout = QtWidgets.QHBoxLayout()
        self.time_edit = QtWidgets.QTimeEdit()
        self.text_line_edit = QtWidgets.QLineEdit('Enter your event')
        self.allow_button = QtWidgets.QPushButton('Add event')
        self.calendar = QtWidgets.QCalendarWidget()
        self.list_widget = QtWidgets.QListWidget()

    def __setting_ui(self) -> None:
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(self.main_v_layout)

        self.tools_h_layout.addWidget(self.time_edit)
        self.tools_h_layout.addWidget(self.text_line_edit)
        self.tools_h_layout.addWidget(self.allow_button)

        self.main_v_layout.addWidget(self.calendar)
        self.main_v_layout.addLayout(self.tools_h_layout)
        self.main_v_layout.addWidget(self.list_widget)

        self.load_events()
        self.allow_button.clicked.connect(self.allow_button_clicked)

    def allow_button_clicked(self) -> None:
        event_text = self.text_line_edit.text().strip()
        if not event_text:
            QtWidgets.QMessageBox.critical(
                self,
                'Error',
                'Event entry is empty',
                QtWidgets.QMessageBox.Ok
            )
            return

        event_item = f'{self.calendar.selectedDate().toPython()} {self.time_edit.text()} - {event_text}'
        self.list_widget.addItem(QtWidgets.QListWidgetItem(event_item))

    def load_events(self) -> None:
        try:
            with open('events.txt', 'r') as file:
                for line in file:
                    line = line.strip()
                    if line:
                        self.list_widget.addItem(QtWidgets.QListWidgetItem(line))
        except FileNotFoundError:
            pass  # Ignore if file not found

    def save_events(self) -> None:
        all_items = self.list_widget.findItems("", QtCore.Qt.MatchFlag.MatchContains)
        all_items_text = '\n'.join(item.text() for item in all_items)

        with open('events.txt', 'w') as file:
            file.write(all_items_text)

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.save_events()
        event.accept()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    root = MainWin()
    sys.exit(app.exec())

