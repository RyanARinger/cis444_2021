def handle_request():
    cur = global_db_con.cursor()

    salted = bcrypt.hashpw( bytes(request.form['pword'],  'utf-8' ) , bcrypt.gensalt(12))
    username = request.form['uname']
    cur.execute("insert into users (username, password) values ('{}','{}')".format(username, salted.decode("utf-8")))

    global_db_con.commit()

    cur.execute("select password from users where username = '{}'".format(username))
    #for item in cur.fetchall():
        #print(item[0])
        #print(  bcrypt.checkpw(  bytes(request.form['pword'],  'utf-8' )  , bytes(item[0], 'utf-8') ))
    return "User Added"
