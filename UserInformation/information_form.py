from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QFormLayout, QLineEdit, QTextEdit,
    QSpinBox, QPushButton, QWidget, QDateEdit, QHBoxLayout, QLabel, QMessageBox
)
from PyQt5.QtCore import QDate
import sqlite3

class InfoFormWidget(QWidget):
    def __init__(self, switch_to_next):
        super().__init__()
        self.switch_to_next = switch_to_next
        self.initUI()
        self.setup_database()

    def initUI(self):
        self.main_layout = QVBoxLayout()

        # Personal Information
        self.personal_info_layout = QFormLayout()
        self.name_input = QLineEdit()
        self.contact_input = QLineEdit()
        self.email_input = QLineEdit()
        self.address_input = QLineEdit()
        self.personal_info_layout.addRow("Name:", self.name_input)
        self.personal_info_layout.addRow("Contact:", self.contact_input)
        self.personal_info_layout.addRow("Email:", self.email_input)
        self.personal_info_layout.addRow("Address:", self.address_input)

        # Education
        self.education_layout = QFormLayout()
        self.university_input = QLineEdit()
        self.degree_input = QLineEdit()
        self.graduation_year_input = QSpinBox()
        self.graduation_year_input.setRange(1900, 2100)
        self.graduation_year_input.setValue(QDate.currentDate().year())
        self.education_layout.addRow("University:", self.university_input)
        self.education_layout.addRow("Degree:", self.degree_input)
        self.education_layout.addRow("Graduation Year:", self.graduation_year_input)

        # Work Experience
        self.work_experience_layout = QFormLayout()
        self.job_title_input = QLineEdit()
        self.company_input = QLineEdit()
        self.start_date_input = QDateEdit()
        self.start_date_input.setCalendarPopup(True)
        self.end_date_input = QDateEdit()
        self.end_date_input.setCalendarPopup(True)
        self.job_description_input = QTextEdit()
        self.work_experience_layout.addRow("Job Title:", self.job_title_input)
        self.work_experience_layout.addRow("Company:", self.company_input)
        self.work_experience_layout.addRow("Start Date:", self.start_date_input)
        self.work_experience_layout.addRow("End Date:", self.end_date_input)
        self.work_experience_layout.addRow("Job Description:", self.job_description_input)

        # Skills and Certifications
        self.skills_layout = QFormLayout()
        self.skills_input = QTextEdit()
        self.skills_layout.addRow("Skills & Certifications:", self.skills_input)

        self.stacked_layout = QVBoxLayout()
        self.pages = [self.personal_info_layout, self.education_layout, self.work_experience_layout, self.skills_layout]
        self.current_page_index = 0

        # Navigation Buttons
        self.prev_button = QPushButton("Previous")
        self.prev_button.clicked.connect(self.prev_page)
        self.next_button = QPushButton("Next")
        self.next_button.clicked.connect(self.next_page)
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_information)
        self.save_button.setEnabled(False)

        self.nav_layout = QHBoxLayout()
        self.nav_layout.addWidget(self.prev_button)
        self.nav_layout.addWidget(self.next_button)
        self.nav_layout.addWidget(self.save_button)

        self.main_layout.addLayout(self.stacked_layout)
        self.main_layout.addLayout(self.nav_layout)

        self.update_layout()
        self.setLayout(self.main_layout)

    def update_layout(self):
        for i in reversed(range(self.stacked_layout.count())):
            widget = self.stacked_layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)
        self.stacked_layout.addLayout(self.pages[self.current_page_index])

        self.prev_button.setEnabled(self.current_page_index > 0)
        self.next_button.setEnabled(self.current_page_index < len(self.pages) - 1)
        self.save_button.setEnabled(self.current_page_index == len(self.pages) - 1)

    def prev_page(self):
        if self.current_page_index > 0:
            self.current_page_index -= 1
        self.update_layout()

    def next_page(self):
        if self.current_page_index < len(self.pages) - 1:
            self.current_page_index += 1
        self.update_layout()

    def setup_database(self):
        self.conn = sqlite3.connect("resume_builder.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_info (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                contact TEXT,
                email TEXT,
                address TEXT,
                university TEXT,
                degree TEXT,
                graduation_year INTEGER,
                job_title TEXT,
                company TEXT,
                start_date TEXT,
                end_date TEXT,
                job_description TEXT,
                skills TEXT
            )
        """)
        self.conn.commit()

    def save_information(self):
        name = self.name_input.text()
        contact = self.contact_input.text()
        email = self.email_input.text()
        address = self.address_input.text()
        university = self.university_input.text()
        degree = self.degree_input.text()
        graduation_year = self.graduation_year_input.value()
        job_title = self.job_title_input.text()
        company = self.company_input.text()
        start_date = self.start_date_input.date().toString("yyyy-MM-dd")
        end_date = self.end_date_input.date().toString("yyyy-MM-dd")
        job_description = self.job_description_input.toPlainText()
        skills = self.skills_input.toPlainText()

        if not all([name, contact, email, address, university, degree, job_title, company, start_date, end_date, job_description, skills]):
            QMessageBox.warning(self, 'Error', 'All fields must be completed.')
            return

        if start_date >= end_date:
            QMessageBox.warning(self, 'Error', 'End date must be after start date.')
            return

        self.cursor.execute("""
            INSERT INTO user_info (
                name, contact, email, address,
                university, degree, graduation_year,
                job_title, company, start_date, end_date,
                job_description, skills
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (name, contact, email, address, university, degree, graduation_year,
              job_title, company, start_date, end_date, job_description, skills))
        self.conn.commit()
        QMessageBox.information(self, 'Success', 'Information saved successfully!')
        self.switch_to_next()
