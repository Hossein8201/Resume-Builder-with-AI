import sqlite3

class UserLoginDatabase:
    def __init__(self):
        self.conn = sqlite3.connect('user_login_data.db')
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute('''CREATE TABLE IF NOT EXISTS users (
                                    id INTEGER PRIMARY KEY,
                                    username TEXT NOT NULL,
                                    email TEXT NOT NULL,
                                    password TEXT NOT NULL
                                )''')

    def add_user(self, username, email, password):
        with self.conn:
            self.conn.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', (username, email, password))

    def validate_user(self, username, password):
        cursor = self.conn.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
        return cursor.fetchone() is not None

    def user_exists(self, username):
        cursor = self.conn.execute('SELECT * FROM users WHERE username=?', (username,))
        return cursor.fetchone() is not None