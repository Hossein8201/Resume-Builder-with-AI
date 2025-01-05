from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QLineEdit, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt

class PersonalInfoWidget(QWidget):
    def __init__(self, switch_to_next):
        super().__init__()
        self.switch_to_next = switch_to_next
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()
        
        title = QLabel('Personal Information')
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title)

        form_layout = QFormLayout()
        self.name_input = QLineEdit()
        self.contact_input = QLineEdit()
        self.email_input = QLineEdit()
        self.address_input = QLineEdit()
        form_layout.addRow("Name:", self.name_input)
        form_layout.addRow("Contact:", self.contact_input)
        form_layout.addRow("Email:", self.email_input)
        form_layout.addRow("Address:", self.address_input)

        main_layout.addLayout(form_layout)

        self.next_button = QPushButton('Next')
        self.next_button.clicked.connect(self.switch_to_next)
        self.next_button.setEnabled(False)

        self.name_input.textChanged.connect(self.check_fields)
        self.contact_input.textChanged.connect(self.check_fields)
        self.email_input.textChanged.connect(self.check_fields)
        self.address_input.textChanged.connect(self.check_fields)

        nav_layout = QHBoxLayout()
        nav_layout.addStretch()
        nav_layout.addWidget(self.next_button)
        main_layout.addLayout(nav_layout)

        self.setLayout(main_layout)

    def check_fields(self):
        if self.name_input.text() and self.contact_input.text() and self.email_input.text() and self.address_input.text():
            self.next_button.setEnabled(True)
        else:
            self.next_button.setEnabled(False)
