import sqlite3
       
        
class UserResumeAddressDatabase:
    def __init__(self):
        self.conn = sqlite3.connect('user_resumeAddress_data.db')
        self.create_tables()
        
    def create_tables(self):
        with self.conn:
            self.conn.execute('''CREATE TABLE IF NOT EXISTS user_resumeAddress (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    username TEXT,
                                    resume_path TEXT
                                )''')
            
    def delete_existing_resume_path(self, username):
        with self.conn:
            self.conn.execute('DELETE FROM user_resumeAddress WHERE username = ?', (username,))
            
    def save_resume_path(self, username, resume_path):
        self.delete_existing_resume_path(username)
        with self.conn:
            self.conn.execute('INSERT INTO user_resumeAddress (username, resume_path) VALUES (?, ?)', (username, resume_path))