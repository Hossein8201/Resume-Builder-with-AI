import sqlite3

class UserLoginDatabase:
    def __init__(self):
        self.conn = sqlite3.connect('user_data.db')
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute('''CREATE TABLE IF NOT EXISTS users (
                                    id INTEGER PRIMARY KEY,
                                    username TEXT NOT NULL,
                                    email TEXT NOT NULL,
                                    password TEXT NOT NULL)''')

    def add_user(self, username, email, password):
        with self.conn:
            self.conn.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', (username, email, password))

    def validate_user(self, username, password):
        cursor = self.conn.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
        return cursor.fetchone() is not None

    def user_exists(self, username):
        cursor = self.conn.execute('SELECT * FROM users WHERE username=?', (username,))
        return cursor.fetchone() is not None


class UserInformationDatabase:
    def __init__(self):
        self.conn = sqlite3.connect('resume_builder.db')
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

    def add_user_info(self, info):
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