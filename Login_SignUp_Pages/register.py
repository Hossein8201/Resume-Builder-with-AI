from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QFrame
from PyQt5.QtGui import QPalette, QColor, QPixmap
from PyQt5.QtCore import QTimer
from Database.user_login_database import UserLoginDatabase

class RegisterWidget(QWidget):
    def __init__(self, switch_to_login, switch_to_info_form):
        super().__init__()
        self.switch_to_login = switch_to_login
        self.switch_to_info_form = switch_to_info_form
        self.initUI()

    def initUI(self):
        self.setFixedSize(1200, 800)

        # Set background color
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("white"))
        self.setPalette(palette)

        main_layout = QHBoxLayout()

        # Image slider
        self.image_label = QLabel(self)
        self.image_label.setFixedSize(700, 467)
        main_layout.addWidget(self.image_label)

        self.image_index = 1
        self.update_image()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_image)
        self.timer.start(8000)  # Change image every 8 seconds

        # Right side layout
        right_frame = QFrame()
        right_frame.setFixedSize(450, 350)
        right_frame.setStyleSheet("background-color: transparent;")
        right_layout = QVBoxLayout(right_frame)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText('Username')
        self.username_input.setStyleSheet("QLineEdit { background-color: lightblue; border-radius: 10px; font-size: 20px; } QLineEdit:focus { border: 2px solid green; }")
        right_layout.addWidget(self.username_input)

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText('Email')
        self.email_input.setStyleSheet("QLineEdit { background-color: lightblue; border-radius: 10px; font-size: 20px; } QLineEdit:focus { border: 2px solid green; }")
        right_layout.addWidget(self.email_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText('Password')
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet("QLineEdit { background-color: lightblue; border-radius: 10px; font-size: 20px; } QLineEdit:focus { border: 2px solid green; }")
        right_layout.addWidget(self.password_input)

        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setPlaceholderText('Confirm Password')
        self.confirm_password_input.setEchoMode(QLineEdit.Password)
        self.confirm_password_input.setStyleSheet("QLineEdit { background-color: lightblue; border-radius: 10px; font-size: 20px; } QLineEdit:focus { border: 2px solid green; }")
        right_layout.addWidget(self.confirm_password_input)

        self.register_button = QPushButton('Sign Up')
        self.register_button.setStyleSheet("background-color: green; color: white; border-radius: 10px; font-size: 20px;")
        self.register_button.clicked.connect(self.register)
        right_layout.addWidget(self.register_button)

        self.login_button = QPushButton('Back to Login')
        self.login_button.setStyleSheet("background-color: green; color: white; border-radius: 10px; font-size: 20px;")
        self.login_button.clicked.connect(self.switch_to_login)
        right_layout.addWidget(self.login_button)

        main_layout.addWidget(right_frame)
        self.setLayout(main_layout)

    def update_image(self):
        pixmap = QPixmap(f'.images/{self.image_index}.png')
        self.image_label.setPixmap(pixmap)
        self.image_index = (self.image_index % 5) + 1

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
        self.switch_to_info_form(username)