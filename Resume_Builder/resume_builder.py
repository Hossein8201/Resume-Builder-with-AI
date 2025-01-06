import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox, QFileDialog, QHBoxLayout
from PyQt5.QtCore import Qt
from Database.user_info_database import UserInformationDatabase
from Database.user_resumeAddress_database import UserResumeAddressDatabase
from Resume_Builder.template1 import fill_template1_pdf, fill_template1_word
from Resume_Builder.template2 import fill_template2_pdf, fill_template2_word    
from Resume_Builder.template3 import fill_template3_pdf, fill_template3_word    
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from docx import Document
from PyQt5.QtGui import QPixmap

class ResumeBuilderWidget(QWidget):
    def __init__(self, username, switch_to_info_form):
        super().__init__()
        self.username = username
        self.switch_to_info_form = switch_to_info_form
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()
        
        self.change_info_button = QPushButton('Change Information') 
        self.change_info_button.clicked.connect(lambda: self.switch_to_info_form(self.username)) 
        main_layout.addWidget(self.change_info_button)
        
        self.label = QLabel('Select a Resume Template')
        self.label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.label)

        template1_preview = QLabel(self) 
        template1_preview.setPixmap(QPixmap('path_to_template1_preview.png')) 
        self.template1_button = QPushButton('Template 1') 
        self.template1_button.clicked.connect(lambda: self.generate_resume('template1')) 
        main_layout.addWidget(template1_preview) 
        main_layout.addWidget(self.template1_button)

        template2_preview = QLabel(self) 
        template2_preview.setPixmap(QPixmap('path_to_template2_preview.png')) 
        self.template2_button = QPushButton('Template 2') 
        self.template2_button.clicked.connect(lambda: self.generate_resume('template2')) 
        main_layout.addWidget(template2_preview) 
        main_layout.addWidget(self.template2_button)

        template3_preview = QLabel(self) 
        template3_preview.setPixmap(QPixmap('path_to_template3_preview.png')) 
        self.template3_button = QPushButton('Template 3') 
        self.template3_button.clicked.connect(lambda: self.generate_resume('template3')) 
        main_layout.addWidget(template3_preview) 
        main_layout.addWidget(self.template3_button)

        self.setLayout(main_layout)

    def generate_resume(self, template):
        user_info = UserInformationDatabase().get_user_info(self.username)
        if not user_info:
            QMessageBox.warning(self, 'Error', 'User information not found')
            return

        file_dialog = QFileDialog()
        options = "PDF Files (*.pdf);;Word Documents (*.docx)" 
        save_path, file_type = file_dialog.getSaveFileName(self, "Save Resume", "", options)

        if save_path:
            if file_type == "PDF Files (*.pdf)": 
                self.create_pdf(template, user_info, save_path) 
            elif file_type == "Word Documents (*.docx)": 
                self.create_word(template, user_info, save_path)
                
            UserResumeAddressDatabase().save_resume_path(self.username, save_path)
            QMessageBox.information(self, 'Success', 'Resume generated and saved successfully!')
            sys.exit(0)

    def create_pdf(self, template, user_info, save_path):
        c = canvas.Canvas(save_path, pagesize=letter)
        width, height = letter

        if template == 'template1':
            fill_template1_pdf(c, user_info, width, height)
        elif template == 'template2':
            fill_template2_pdf(c, user_info, width, height)
        elif template == 'template3':
            fill_template3_pdf(c, user_info, width, height)

        c.showPage()
        c.save()
        
    def create_word(self, template, user_info, save_path):
        doc = Document()
        
        if template == 'template1':
            fill_template1_word(doc, user_info)
        elif template == 'template2':
            fill_template2_word(doc, user_info)
        elif template == 'template3':
            fill_template3_word(doc, user_info)
            
        doc.save(save_path)