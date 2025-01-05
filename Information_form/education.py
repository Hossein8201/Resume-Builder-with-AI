from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QLineEdit, QSpinBox, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt, QDate

class EducationWidget(QWidget):
    def __init__(self, switch_to_next, switch_to_prev):
        super().__init__()
        self.switch_to_next = switch_to_next
        self.switch_to_prev = switch_to_prev
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()
        
        title = QLabel('Education')
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title)

        form_layout = QFormLayout()
        self.university_input = QLineEdit()
        self.degree_input = QLineEdit()
        self.graduation_year_input = QSpinBox()
        self.graduation_year_input.setRange(1900, 2100)
        self.graduation_year_input.setValue(QDate.currentDate().year())
        form_layout.addRow("University:", self.university_input)
        form_layout.addRow("Degree:", self.degree_input)
        form_layout.addRow("Graduation Year:", self.graduation_year_input)

        main_layout.addLayout(form_layout)

        self.next_button = QPushButton('Next')
        self.next_button.clicked.connect(self.switch_to_next)
        self.next_button.setEnabled(False)

        self.prev_button = QPushButton('Previous')
        self.prev_button.clicked.connect(self.switch_to_prev)

        self.university_input.textChanged.connect(self.check_fields)
        self.degree_input.textChanged.connect(self.check_fields)

        nav_layout = QHBoxLayout()
        nav_layout.addWidget(self.prev_button)
        nav_layout.addStretch()
        nav_layout.addWidget(self.next_button)
        main_layout.addLayout(nav_layout)

        self.setLayout(main_layout)

    def check_fields(self):
        if self.university_input.text() and self.degree_input.text():
            self.next_button.setEnabled(True)
        else:
            self.next_button.setEnabled(False)
