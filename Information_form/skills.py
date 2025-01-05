from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QTextEdit, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt

class SkillsWidget(QWidget):
    def __init__(self, save_info, switch_to_prev):
        super().__init__()
        self.save_info = save_info
        self.switch_to_prev = switch_to_prev
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()
        
        title = QLabel('Skills and Certifications')
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title)

        form_layout = QFormLayout()
        self.skills_input = QTextEdit()
        form_layout.addRow("Skills:", self.skills_input)
        self.certifications_input = QTextEdit()
        form_layout.addRow("Certifications:", self.certifications_input)

        main_layout.addLayout(form_layout)

        self.save_button = QPushButton('Save')
        self.save_button.clicked.connect(self.save_info)
        self.save_button.setEnabled(False)

        self.prev_button = QPushButton('Previous')
        self.prev_button.clicked.connect(self.switch_to_prev)

        self.skills_input.textChanged.connect(self.check_fields)
        self.certifications_input.textChanged.connect(self.check_fields)

        nav_layout = QHBoxLayout()
        nav_layout.addWidget(self.prev_button)
        nav_layout.addStretch()
        nav_layout.addWidget(self.save_button)
        main_layout.addLayout(nav_layout)

        self.setLayout(main_layout)

    def check_fields(self):
        if self.skills_input.toPlainText() and self.certifications_input.toPlainText():
            self.save_button.setEnabled(True)
        else:
            self.save_button.setEnabled(False)
