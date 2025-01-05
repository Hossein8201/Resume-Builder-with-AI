from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QLineEdit, QTextEdit, QDateEdit, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt

class WorkExperienceWidget(QWidget):
    def __init__(self, switch_to_next, switch_to_prev):
        super().__init__()
        self.switch_to_next = switch_to_next
        self.switch_to_prev = switch_to_prev
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()
        
        title = QLabel('Work Experience')
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title)

        form_layout = QFormLayout()
        self.job_title_input = QLineEdit()
        self.company_input = QLineEdit()
        self.start_date_input = QDateEdit()
        self.start_date_input.setCalendarPopup(True)
        self.end_date_input = QDateEdit()
        self.end_date_input.setCalendarPopup(True)
        self.job_description_input = QTextEdit()
        form_layout.addRow("Job Title:", self.job_title_input)
        form_layout.addRow("Company:", self.company_input)
        form_layout.addRow("Start Date:", self.start_date_input)
        form_layout.addRow("End Date:", self.end_date_input)
        form_layout.addRow("Job Description:", self.job_description_input)

        main_layout.addLayout(form_layout)

        self.next_button = QPushButton('Next')
        self.next_button.clicked.connect(self.switch_to_next)
        self.next_button.setEnabled(False)

        self.prev_button = QPushButton('Previous')
        self.prev_button.clicked.connect(self.switch_to_prev)

        self.job_title_input.textChanged.connect(self.check_fields)
        self.company_input.textChanged.connect(self.check_fields)
        self.job_description_input.textChanged.connect(self.check_fields)

        nav_layout = QHBoxLayout()
        nav_layout.addWidget(self.prev_button)
        nav_layout.addStretch()
        nav_layout.addWidget(self.next_button)
        main_layout.addLayout(nav_layout)

        self.setLayout(main_layout)

    def check_fields(self):
        if self.job_title_input.text() and self.company_input.text() and self.job_description_input.toPlainText():
            self.next_button.setEnabled(True)
        else:
            self.next_button.setEnabled(False)
