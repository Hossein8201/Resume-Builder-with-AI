from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from database import UserLoginDatabase

class RegisterWidget(QWidget):
    def __init__(self, switch_to_login, switch_to_info_form):
        super().__init__()
        self.switch_to_login = switch_to_login
        self.switch_to_info_form = switch_to_info_form
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.username_label = QLabel('Username:')
        self.username_input = QLineEdit()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)

        self.email_label = QLabel('Email:')
        self.email_input = QLineEdit()
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)

        self.password_label = QLabel('Password:')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)

        self.confirm_password_label = QLabel('Confirm Password:')
        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.confirm_password_label)
        layout.addWidget(self.confirm_password_input)

        self.register_button = QPushButton('Sign Up')
        self.register_button.clicked.connect(self.register)
        layout.addWidget(self.register_button)

        self.login_button = QPushButton('Back to Login')
        self.login_button.clicked.connect(self.switch_to_login)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def register(self):
        username = self.username_input.text()
        email = self.email_input.text()
        password = self.password_input.text()
        confirm_password = self.confirm_password_input.text()

        if password != confirm_password:
            QMessageBox.warning(self, 'Error', 'Passwords do not match.')
            self.username_input.clear()
            self.email_input.clear()
            self.password_input.clear()
            self.confirm_password_input.clear()
            return

        if UserLoginDatabase().user_exists(username):
            QMessageBox.warning(self, 'Error', 'username is already signed up.')
            self.username_input.clear()
            self.email_input.clear()
            self.password_input.clear()
            self.confirm_password_input.clear()
            return

        UserLoginDatabase().add_user(username, email, password)
        QMessageBox.information(self, 'Success', 'signing up successful!')
        self.switch_to_info_form()
