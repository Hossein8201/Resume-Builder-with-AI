import sqlite3

class UserStorage:
    def __init__(self):
        self.conn = sqlite3.connect('resume_builder.db')
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute('''CREATE TABLE IF NOT EXISTS user_info (
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
                                    skills TEXT,
                                    certifications TEXT
                                )''')

    def add_user_info(self, info):
        with self.conn:
            self.conn.execute('''INSERT INTO user_info (
                                    name, contact, email, address,
                                    university, degree, graduation_year,
                                    job_title, company, start_date, end_date,
                                    job_description, skills, certifications
                                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', info)