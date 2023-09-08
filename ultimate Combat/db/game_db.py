import psycopg2

conn = psycopg2.connect(host='localhost',dbname='postgres', user='ganesh', password='password', port=5432)

cur = conn.cursor()

#player_name = input('Enter name:')
#game_score=30

cur.execute("""CREATE TABLE IF NOT EXISTS game_data(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    score INT
)
""")
'''cur.execute(f"""INSERT INTO game_data(name,score) VALUES (
    '{player_name}',
    '{game_score}'
)
""")
'''
cur.execute("""SELECT * FROM game_data""")
players=cur.fetchall()
print(players)
print(type(players))

conn.commit()

cur.close()
conn.close()