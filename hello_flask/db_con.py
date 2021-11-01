import psycopg2

def get_db():
    return psycopg2.connect(host="localhost", dbname="authme", user="clapton", password="ists")

def get_db_instance():
    db = get_db()
    cur = db.cursor()

    return db, cur


db,cur = get_db_instance()

cur.execute("select * from users")

r = cur.fetchone()

#print(r)
