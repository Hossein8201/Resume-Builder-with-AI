from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox, QFileDialog, QHBoxLayout, QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QCursor, QPalette, QColor
import os
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
from Database.user_info_database import UserInformationDatabase
from Database.user_resumeAddress_database import UserResumeAddressDatabase

class ResumeBuilderWidget(QWidget):
    def __init__(self, username, switch_to_info_form):
        super().__init__()
        self.username = username
        self.switch_to_info_form = switch_to_info_form
        self.initUI()

    def initUI(self):
        self.setFixedSize(1200, 800)
        palete = self.palette()
        palete.setColor(QPalette.Window, QColor("white"))
        self.setPalette(palete)
        
        main_layout = QVBoxLayout()

        self.change_info_button = QPushButton(' << Change Information')
        self.style_button(self.change_info_button)
        self.change_info_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.change_info_button.clicked.connect(lambda: self.switch_to_info_form(self.username))
        
        layout = QVBoxLayout() 
        layout.addStretch()
        layout.addWidget(self.change_info_button, alignment=Qt.AlignCenter)
        layout.addStretch()
        main_layout.addLayout(layout)
        
        self.label = QLabel('Select a Resume Template')
        self.label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.label)

        pdf_preview_layout = QHBoxLayout()
        
        template1_preview = QLabel(self)
        template1_preview.setPixmap(QPixmap('.images/template1.png'))
        template1_preview.setScaledContents(True)
        pdf_preview_layout.addWidget(template1_preview)
        
        template2_preview = QLabel(self)
        template2_preview.setPixmap(QPixmap('.images/template2.png'))
        template2_preview.setScaledContents(True)
        pdf_preview_layout.addWidget(template2_preview)
        
        template3_preview = QLabel(self)
        template3_preview.setPixmap(QPixmap('.images/template3.png'))
        template3_preview.setScaledContents(True)
        pdf_preview_layout.addWidget(template3_preview)
        
        for widget in [template1_preview, template2_preview, template3_preview]:
            widget.setFrameShape(QFrame.Box)
            widget.setFrameShadow(QFrame.Sunken)
            widget.setStyleSheet("border: 1px solid black;")
        
        main_layout.addLayout(pdf_preview_layout)

        self.template1_button = QPushButton('Template 1')
        self.style_button(self.template1_button)
        self.template1_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.template1_button.clicked.connect(lambda: self.generate_resume('template1'))
        
        self.template2_button = QPushButton('Template 2')
        self.style_button(self.template2_button)
        self.template2_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.template2_button.clicked.connect(lambda: self.generate_resume('template2'))
        
        self.template3_button = QPushButton('Template 3')
        self.style_button(self.template3_button)
        self.template3_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.template3_button.clicked.connect(lambda: self.generate_resume('template3'))
        
        template_button_layout = QHBoxLayout()
        template_button_layout.addWidget(self.template1_button)
        template_button_layout.addWidget(self.template2_button)
        template_button_layout.addWidget(self.template3_button)
        main_layout.addLayout(template_button_layout)

        self.setLayout(main_layout)

    def style_button(self, button):
        button.setStyleSheet("""
            QPushButton {
                font-size: 16px;
                border-radius: 10px;
                background-color: white;
                border: 2px solid green;
            }
            QPushButton:hover { 
                background-color: green; 
                color: white; 
            }
        """)

    def get_user_info(self):
        user_info = UserInformationDatabase().get_user_info(self.username)
        if not user_info:
            QMessageBox.warning(self, 'Error', 'User information not found')
            return
        info = {
            'username': user_info[1],
            'name': user_info[2],
            'title': "Software Developer",
            'phone': user_info[3],
            'email': user_info[4],
            'address': user_info[5],
            'professional_summary': "I am a software developer with 5 years of experience in developing web applications.\n" +
                "I have a strong understanding of web technologies and have worked with various frameworks and libraries.",
            "education": {
                'university': user_info[6],
                'degree': user_info[7],
                'graduation_year': user_info[8]
            },
            'work_experience': {
                'job_title': user_info[9],
                'company': user_info[10],
                'start_date': user_info[11],
                'end_date': user_info[12],
                'job_description': user_info[13]
            },
            'skills': user_info[14].split('\n'),
            'certifications': user_info[15].split('\n')
        }
        return info

    def generate_resume(self, template):
        user_info = self.get_user_info()

        file_dialog = QFileDialog()
        options = "PDF Files (*.pdf)"
        save_path, file_type = file_dialog.getSaveFileName(self, "Save Resume", "", options)

        if save_path:
            if file_type == "PDF Files (*.pdf)":
                self.create_pdf(template, user_info, save_path)

            UserResumeAddressDatabase().save_resume_path(self.username, save_path)
            QMessageBox.information(self, 'Success', 'Resume generated and saved successfully!')

    def create_pdf(self, template, user_info, save_path):
        environment = Environment(loader=FileSystemLoader(os.getcwd()))

        if template == 'template1':
            template = environment.get_template('Resume_Builder/template1.html')
        elif template == 'template2':
            template = environment.get_template('Resume_Builder/template2.html')
        elif template == 'template3':
            template = environment.get_template('Resume_Builder/template3.html')

        html = template.render(user_info)
        HTML(string=html).write_pdf(save_path)