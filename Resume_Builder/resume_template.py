from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox, QFileDialog
from PyQt5.QtCore import Qt
from Database.user_info_database import UserInformationDatabase
from Database.user_resumeAddress_database import UserResumeAddressDatabase
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

class ResumeTemplateWidget(QWidget):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()
        
        self.label = QLabel('Select a Resume Template')
        self.label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.label)

        self.template1_button = QPushButton('Template 1')
        self.template1_button.clicked.connect(lambda: self.generate_resume('template1'))
        main_layout.addWidget(self.template1_button)

        self.template2_button = QPushButton('Template 2')
        self.template2_button.clicked.connect(lambda: self.generate_resume('template2'))
        main_layout.addWidget(self.template2_button)

        self.template3_button = QPushButton('Template 3')
        self.template3_button.clicked.connect(lambda: self.generate_resume('template3'))
        main_layout.addWidget(self.template3_button)

        self.setLayout(main_layout)

    def generate_resume(self, template):
        user_info = UserInformationDatabase().get_user_info(self.username)
        if not user_info:
            QMessageBox.warning(self, 'Error', 'User information not found.')
            return

        file_dialog = QFileDialog()
        save_path, _ = file_dialog.getSaveFileName(self, "Save Resume", "", "PDF Files (*.pdf)")

        if save_path:
            self.create_pdf(template, user_info, save_path)
            UserResumeAddressDatabase().save_resume_path(self.username, save_path)
            QMessageBox.information(self, 'Success', 'Resume generated and saved successfully!')

    def create_pdf(self, template, user_info, save_path):
        c = canvas.Canvas(save_path, pagesize=letter)
        width, height = letter

        if template == 'template1':
            self.fill_template1(c, user_info, width, height)
        elif template == 'template2':
            self.fill_template2(c, user_info, width, height)
        elif template == 'template3':
            self.fill_template3(c, user_info, width, height)

        c.showPage()
        c.save()

    def fill_template1(self, c, user_info, width, height):
        c.drawString(100, height - 80, "Personal Information:")
        c.drawString(120, height - 100, f"Name: {user_info[2]}")
        c.drawString(120, height - 120, f"Contact: {user_info[3]}")
        c.drawString(120, height - 140, f"Email: {user_info[4]}")
        c.drawString(120, height - 160, f"Address: {user_info[5]}")
        c.drawString(100, height - 200, "Education:")
        c.drawString(120, height - 220, f"University: {user_info[6]}")
        c.drawString(120, height - 240, f"Degree: {user_info[7]}")
        c.drawString(120, height - 260, f"Graduation Year: {user_info[8]}")
        c.drawString(100, height - 300, "Work Experience:")
        c.drawString(120, height - 320, f"Job Title: {user_info[9]}")
        c.drawString(120, height - 340, f"Company: {user_info[10]}")
        c.drawString(120, height - 360, f"Start Date: {user_info[11]}")
        c.drawString(120, height - 380, f"End Date: {user_info[12]}")
        c.drawString(120, height - 400, f"Job Description: {user_info[13]}")
        c.drawString(100, height - 440, "Skills:")
        c.drawString(120, height - 460, f"{user_info[14]}")
        c.drawString(100, height - 500, "Certifications:")
        c.drawString(120, height - 520, f"{user_info[15]}")

    def fill_template2(self, c, user_info, width, height):
        # Similar to fill_template1 but with different layout
        pass

    def fill_template3(self, c, user_info, width, height):
        # Similar to fill_template1 but with different layout
        pass