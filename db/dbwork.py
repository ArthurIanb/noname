import sqlite3


class DbWork:
    def __init__(self):
        self.db = sqlite3.connect('db/db.db')
        self.curs = self.db.cursor()
    
    def add_user(self, user_name, user_path_to_icon, user_time):
        query = f"insert into users(name, icon, user_time, game_date) values('{user_name}', " \
                f"'{user_path_to_icon}', {user_time}, datetime('now'))"
        self.curs.execute(query)
    
    def get_users(self):
        return self.curs.execute("select * from users").fetchall()

    def save(self):
        self.db.commit()
