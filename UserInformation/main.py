from tkinter import messagebox
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QMessageBox
from login import LoginWidget
from register import RegisterWidget
from information_form import InfoFormWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Resume Builder")
        self.setGeometry(100, 100, 1200, 800)
        self.initUI()

    def initUI(self):
        self.stacked_widget = QStackedWidget()

        self.login_widget = LoginWidget(self.switch_to_register)
        self.register_widget = RegisterWidget(self.switch_to_login, self.switch_to_info_form)
        self.info_form_widget = InfoFormWidget(self.switch_to_next)

        self.stacked_widget.addWidget(self.login_widget)
        self.stacked_widget.addWidget(self.register_widget)
        self.stacked_widget.addWidget(self.info_form_widget)

        self.setCentralWidget(self.stacked_widget)
        self.show()

    def switch_to_register(self):
        self.stacked_widget.setCurrentWidget(self.register_widget)

    def switch_to_login(self):
        self.stacked_widget.setCurrentWidget(self.login_widget)

    def switch_to_info_form(self):
        self.stacked_widget.setCurrentWidget(self.info_form_widget)

    def switch_to_next(self):
        QMessageBox.information(self, 'Success', 'Information saved and moving to next step!')
        # Add logic to switch to next section if needed

def main():
    import sys
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
