import sqlite3

class Database:
    def __init__(self, file_path: str):
        try:
            self.connection = sqlite3.connect(file_path)
        except Exception as ex:
            print(f'EXCEPTION: {ex}')
    
    def create_tables(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS notifications (user_id INTEGER UNIQUE);')

            self.connection.commit()
        except Exception as ex:
            print(f'EXCEPTION: {ex}')
    
    def opt_in(self, user_id: int):
        cursor = self.connection.cursor()
        cursor.execute(f'INSERT INTO notifications (user_id) VALUES ({user_id});')
        self.connection.commit()
    
    def opt_out(self, user_id: int):
        cursor = self.connection.cursor()
        cursor.execute(f'DELETE FROM notifications WHERE user_id={user_id};')
        self.connection.commit()

    def get_user(self, user_id):
        cursor = self.connection.cursor()
        return cursor.execute(f'SELECT user_id FROM notifications WHERE user_id={user_id}').fetchone()
    
    def get_users(self):
        cursor = self.connection.cursor()
        return cursor.execute('SELECT user_id FROM notifications').fetchall()
