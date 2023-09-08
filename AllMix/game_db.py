import psycopg2


class game_db:
    conn = psycopg2.connect(host='localhost',dbname='postgres', user='ganesh', password='password', port=5432)
    def __init__(self) -> None:
        

        self.cur = self.conn.cursor()

    #player_name = input('Enter name:')
    #game_score=30
    def save_player(self,player_name,game_score):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS game_data(
            id SERIAL PRIMARY KEY,
            name VARCHAR(255),
            score INT
        )
        """)
        self.cur.execute(f"""INSERT INTO game_data(name,score) VALUES (
            '{player_name}',
            '{game_score}'
        )
        """)
        self.conn.commit()

    def player_list(self):
        self.cur.execute("""SELECT * FROM game_data""")
        players=self.cur.fetchall()
        print(players)
        print(type(players))
        self.conn.commit()

        return players
    
    def close_db(self):
        print('db closed')
        self.cur.close()
        self.conn.close()
        