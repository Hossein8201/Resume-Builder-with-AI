from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QFrame
from PyQt5.QtGui import QPalette, QColor, QPixmap, QCursor
from PyQt5.QtCore import QTimer, Qt
from Database.user_login_database import UserLoginDatabase

class LoginWidget(QWidget):
    def __init__(self, switch_to_register, switch_to_resume):
        super().__init__()
        self.switch_to_register = switch_to_register
        self.switch_to_resume = switch_to_resume
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
        right_frame.setFixedSize(450, 250)
        right_frame.setStyleSheet("background-color: transparent;")
        right_layout = QVBoxLayout(right_frame)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText('Username')
        self.QLineEdit_style(self.username_input)     
        right_layout.addWidget(self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText('Password')
        self.password_input.setEchoMode(QLineEdit.Password)
        self.QLineEdit_style(self.password_input)
        right_layout.addWidget(self.password_input)

        self.login_button = QPushButton('Login')
        self.login_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.style_button(self.login_button)
        self.login_button.clicked.connect(self.login)
        right_layout.addWidget(self.login_button)

        self.register_button = QPushButton('Go to Sign Up')
        self.register_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.style_button(self.register_button)
        self.register_button.clicked.connect(self.switch_to_register)
        right_layout.addWidget(self.register_button)

        main_layout.addWidget(right_frame)
        self.setLayout(main_layout)

    def update_image(self):
        pixmap = QPixmap(f'.images/{self.image_index}.png')
        self.image_label.setPixmap(pixmap)
        self.image_index = (self.image_index % 5) + 1
        
    def QLineEdit_style(self, lineEdit):
        lineEdit.setStyleSheet("""
            QLineEdit { 
                background-color: lightblue; 
                border-radius: 10px; 
                font-size: 20px; 
            } 
            QLineEdit:focus { 
                border: 2px solid green;   
            }
        """)
        
    def style_button(self, button):
        button.setStyleSheet("""
            QPushButton {
                background-color: lightgreen;
                color: black;
                border-radius: 10px;
                font-size: 20px;
            }
            QPushButton:hover {
                background-color: green;
                color: white;
            }
        """)

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
