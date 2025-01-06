import sqlite3


class UserInformationDatabase:
    def __init__(self):
        self.conn = sqlite3.connect('user_information_data.db')
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute('''CREATE TABLE IF NOT EXISTS user_information (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    username TEXT,
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
            
    def delete_existing_user_info(self, username):
        with self.conn:
            self.conn.execute('DELETE FROM user_information WHERE username = ?', (username,))

    def add_user_info(self, info):
        self.delete_existing_user_info(info[0])
        with self.conn:
            self.conn.execute('''INSERT INTO user_information (
                                    username, name, contact, email, address,
                                    university, degree, graduation_year,
                                    job_title, company, start_date, end_date,
                                    job_description, skills, certifications
                                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', info)
    
    def get_user_info(self, username):
        with self.conn:
            return self.conn.execute('SELECT * FROM user_information WHERE username = ?', (username,)).fetchone()