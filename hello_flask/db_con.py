import psycopg2

<<<<<<< HEAD

def get_db():
    return psycopg2.connect(host="localhost", dbname="books" , user="mayer", password="light")

def get_db_instance():  
    db  = get_db()
    cur  = db.cursor()

    return db, cur 



if __name__ == "__main__":
    db, cur = get_db_instance()

    cur.execute("select * from users")
    for r in cur.fetchall():
        print(r)

    cur.execute("create table music ( song_name varchar(255), rating int);")
    db.commit()




=======
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
>>>>>>> 1e808fdf2545ee096a12772117dff75fdd0c0aaf
