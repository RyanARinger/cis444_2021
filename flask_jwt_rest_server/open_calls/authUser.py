def handle_request():
     cur = global_db_con.cursor()
    username = request.form['uname']
    validUser = False
    isLind = "False" #I promised my friend a birthday message

    cur.execute("select password from users where username = '{}'".format(username))
    for item in cur.fetchall():
        if bcrypt.checkpw(  bytes(request.form['pword'],'utf-8' )  , bytes(item[0], 'utf-8')):
            validUser = True

    if validUser:
        if username == "Lindsey":
            isLind = "True"
            #print(isLind)
        jwt_str = jwt.encode({"username" : username}, JWT_SECRET, algorithm="HS256")
        return json_response(jwt=jwt_str, lind=isLind)
    else:
        return json_response(jwt='BadRequest')
