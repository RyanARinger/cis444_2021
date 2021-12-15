def handle_request():
    cur = global_db_con.cursor()

    cur.execute("select title, price from book")

    return json_response(bookList=cur.fetchall())
