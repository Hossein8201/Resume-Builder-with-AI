from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QMessageBox
from Login_SignUp_Pages.login import LoginWidget
from Login_SignUp_Pages.register import RegisterWidget
from Information_Form.personal_info import PersonalInfoWidget
from Information_Form.education import EducationWidget
from Information_Form.work_experience import WorkExperienceWidget
from Information_Form.skills import SkillsWidget
from Database.user_info_database import UserInformationDatabase
from Resume_Builder.resume_builder import ResumeBuilderWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Resume Builder Application")
        self.setGeometry(100, 100, 1200, 800)
        self.setFixedSize(1200, 800)
        self.initUI()
        self.storage = UserInformationDatabase()
        self.user_info = {}

    def initUI(self):
        self.stacked_widget = QStackedWidget()

        self.login_widget = LoginWidget(self.switch_to_register, self.switch_to_resume)
        self.register_widget = RegisterWidget(self.switch_to_login, self.switch_to_personal_info)
        self.personal_info_widget = PersonalInfoWidget(self.switch_to_education)
        self.education_widget = EducationWidget(self.switch_to_work_experience, self.switch_to_personal_info)
        self.work_experience_widget = WorkExperienceWidget(self.switch_to_skills, self.switch_to_education)
        self.skills_widget = SkillsWidget(self.save_information, self.switch_to_work_experience)

        self.stacked_widget.addWidget(self.login_widget)
        self.stacked_widget.addWidget(self.register_widget)
        self.stacked_widget.addWidget(self.personal_info_widget)
        self.stacked_widget.addWidget(self.education_widget)
        self.stacked_widget.addWidget(self.work_experience_widget)
        self.stacked_widget.addWidget(self.skills_widget)

        self.setCentralWidget(self.stacked_widget)
        self.show()

    def switch_to_register(self):
        self.stacked_widget.setCurrentWidget(self.register_widget)

    def switch_to_login(self):
        self.stacked_widget.setCurrentWidget(self.login_widget)

    def switch_to_personal_info(self, username):
        self.user_info['username'] = username
        self.stacked_widget.setCurrentWidget(self.personal_info_widget)

    def switch_to_education(self):
        self.user_info['personal_info'] = {
            'name': self.personal_info_widget.name_input.text(),
            'contact': self.personal_info_widget.contact_input.text(),
            'email': self.personal_info_widget.email_input.text(),
            'address': self.personal_info_widget.address_input.text()
        }
        self.stacked_widget.setCurrentWidget(self.education_widget)

    def switch_to_work_experience(self):
        self.user_info['education'] = {
            'university': self.education_widget.university_input.text(),
            'degree': self.education_widget.degree_input.text(),
            'graduation_year': self.education_widget.graduation_year_input.text()
        }
        self.stacked_widget.setCurrentWidget(self.work_experience_widget)

    def switch_to_skills(self):
        self.user_info['work_experience'] = {
            'job_title': self.work_experience_widget.job_title_input.text(),
            'company': self.work_experience_widget.company_input.text(),
            'start_date': self.work_experience_widget.start_date_input.text(),
            'end_date': self.work_experience_widget.end_date_input.text(),
            'job_description': self.work_experience_widget.job_description_input.toPlainText()
        }
        self.stacked_widget.setCurrentWidget(self.skills_widget)

    def switch_to_resume(self, username):
        self.resume_template_widget = ResumeBuilderWidget(username, self.switch_to_personal_info)
        self.stacked_widget.addWidget(self.resume_template_widget)
        self.stacked_widget.setCurrentWidget(self.resume_template_widget)

    def save_information(self):
        self.user_info['skills'] = {
            'skills': self.skills_widget.skills_input.toPlainText(), 
            'certifications': self.skills_widget.certifications_input.toPlainText()
        }
        
        if self.is_data_complete():
            info = (
                self.user_info['username'],
                self.user_info['personal_info']['name'],
                self.user_info['personal_info']['contact'],
                self.user_info['personal_info']['email'],
                self.user_info['personal_info']['address'],
                self.user_info['education']['university'],
                self.user_info['education']['degree'],
                self.user_info['education']['graduation_year'],
                self.user_info['work_experience']['job_title'],
                self.user_info['work_experience']['company'],
                self.user_info['work_experience']['start_date'],
                self.user_info['work_experience']['end_date'],
                self.user_info['work_experience']['job_description'],
                self.user_info['skills']['skills'],
                self.user_info['skills']['certifications']
            )
            self.storage.add_user_info(info)
            QMessageBox.information(self, 'Success', 'Information saved successfully!')
            self.switch_to_resume(self.user_info['username'])
        else:
            QMessageBox.warning(self, 'Error', 'Please complete all fields before saving.')

    def is_data_complete(self):
        for section in self.user_info.values():
            if isinstance(section, dict):
                for value in section.values():
                    if not value:
                        return False
            elif not section:
                return False
        return True

def main():
    import sys
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
