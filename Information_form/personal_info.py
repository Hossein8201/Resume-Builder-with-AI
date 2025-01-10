from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QPixmap, QCursor

class PersonalInfoWidget(QWidget):
    def __init__(self, switch_to_next):
        super().__init__()
        self.switch_to_next = switch_to_next
        self.initUI()

    def initUI(self):
        self.setFixedSize(1200, 800)
        self.setAutoFillBackground(True)
        palete = self.palette()
        palete.setColor(QPalette.Window, QColor("white"))
        self.setPalette(palete)

        main_layout = QHBoxLayout()

        left_layout = QVBoxLayout()

        cover1 = QWidget()
        cover1.setFixedSize(300, 500)
        cover1.setStyleSheet("background-color: white; border-radius: 10px;")
        
        cover1_layout = QVBoxLayout()
        modules = ["Personal Information", "Education", "Work Experience", "Skills and Certifications"]
        flag = 0
        for module in modules:
            label = QLabel(module)
            if module == "Personal Information":
                label.setStyleSheet("""
                    font-weight: bold; 
                    font-size: 20px; 
                    color: blue; 
                    border: 1px solid #d3d3d3; 
                    padding: 5px; 
                    background-color: #f0f0f0; 
                    border-radius: 10px;
                """)
                flag = 1
            elif flag == 1:
                label.setStyleSheet("font-size: 18px; margin-bottom: 10px; color: gray;") 
            else:
                label.setStyleSheet("font-size: 18px; margin-bottom: 10px; color: black;") 
            cover1_layout.addWidget(label)
        cover1_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        cover1.setLayout(cover1_layout)

        left_layout.addWidget(cover1)

        cover2 = QWidget()
        cover2.setFixedSize(300, 300)
        logo = QLabel()
        pixmap = QPixmap(".images/FullLogo.png").copy(120, 100, 300, 300)
        logo.setPixmap(pixmap)
        cover2_layout = QVBoxLayout()
        cover2_layout.addWidget(logo, alignment=Qt.AlignCenter)
        cover2.setLayout(cover2_layout)

        left_layout.addWidget(cover2)
        
        left_layout_widget = QWidget()
        left_layout_widget.setFixedSize(300, 800)
        left_layout_widget.setLayout(left_layout)
        left_layout_widget.setStyleSheet("background-color: white;")
        
        main_layout.addWidget(left_layout_widget)

        right_layout = QVBoxLayout()

        self.name_input = QLineEdit()
        self.contact_input = QLineEdit()
        self.email_input = QLineEdit()
        self.address_input = QLineEdit()

        fields = [("Name", self.name_input), ("Contact", self.contact_input), ("Email", self.email_input), ("Address", self.address_input)]
        
        for field_name, field_input in fields:
            field_label = QLabel(field_name)
            field_label.setStyleSheet("font-size: 16px;")
            field_input.setStyleSheet("""
                QLineEdit { 
                    font-size: 16px; 
                    border-radius: 10px; 
                    background-color: #ADD8E6; 
                } 
                QLineEdit:focus { 
                    border: 2px solid yellow; 
                }
            """)
            field_layout = QVBoxLayout()
            field_layout.addWidget(field_label)
            field_layout.addWidget(field_input)
            right_layout.addLayout(field_layout)
        right_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.next_button = QPushButton(' Next >> ')
        self.next_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.next_button.setStyleSheet("""
            font-size: 16px;
            border-radius: 10px;
            background-color: lightgray;
            border: 2px solid lightgray;
        """)
        self.next_button.setEnabled(False)
        
        self.next_button.clicked.connect(self.switch_to_next)
        
        self.name_input.textChanged.connect(self.check_fields)
        self.contact_input.textChanged.connect(self.check_fields)
        self.email_input.textChanged.connect(self.check_fields)
        self.address_input.textChanged.connect(self.check_fields)

        nav_layout = QHBoxLayout()
        nav_layout.addStretch()
        nav_layout.addWidget(self.next_button)
        
        right_layout.addLayout(nav_layout)

        right_layout_widget = QWidget()
        right_layout_widget.setFixedSize(850, 750)
        right_layout_widget.setStyleSheet("background-color: #f0f0f0; padding: 10px; border-radius: 10px;")
        right_layout_widget.setLayout(right_layout)
        main_layout.addWidget(right_layout_widget)

        self.setLayout(main_layout)

    def check_fields(self):
        if self.name_input.text() and self.contact_input.text() and self.email_input.text() and self.address_input.text():
            self.next_button.setEnabled(True)
            self.next_button.setStyleSheet("""
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
        else:
            self.next_button.setEnabled(False)
            self.next_button.setStyleSheet("""
                font-size: 16px;    
                border-radius: 10px;
                background-color: lightgray;
                border: 2px solid lightgray;
            """)