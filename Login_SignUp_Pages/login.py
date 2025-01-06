from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from Database.user_login_database import UserLoginDatabase

class LoginWidget(QWidget):
    def __init__(self, switch_to_register, switch_to_resume):
        super().__init__()
        self.switch_to_register = switch_to_register
        self.switch_to_resume = switch_to_resume
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.username_label = QLabel('Username:')
        self.username_input = QLineEdit()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)

        self.password_label = QLabel('Password:')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)

        self.login_button = QPushButton('Login')
        self.login_button.clicked.connect(self.login)
        layout.addWidget(self.login_button)

        self.register_button = QPushButton('Go to Sign Up')
        self.register_button.clicked.connect(self.switch_to_register)
        layout.addWidget(self.register_button)

        self.setLayout(layout)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if UserLoginDatabase().validate_user(username, password):
            QMessageBox.information(self, 'Success', 'Login successful!')
            self.switch_to_resume(username)
        else:
            QMessageBox.warning(self, 'Error', 'Invalid username or password.')
            self.username_input.clear()
            self.password_input.clear()