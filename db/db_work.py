import sqlite3



class DB_Work:
    def __init__(self):
        self.db = sqlite3.connect('db/db.db')
        self.curs = self.db.cursor()
    
    def add_user(self, user_name, user_path_to_icon, user_time):
        query = f"insert into users(name, icon, user_time, game_date) values({user_name}, {user_path_to_icon}, {user_time}, datetime('now'))"
    
    def get_users(self, id):
        ...
    
    def change_user_name(self, id, new_name):
        ...
    
    def change_user_icon(self, id, new_path_to_icon):
        ...
    
    def delete_user(self, id):
        ...

