import sqlite3

def connect():
    sql_connect = sqlite3.connect("personal_info.db")
    mouse_cursor = sql_connect.cursor()
    mouse_cursor.execute("CREATE TABLE IF NOT EXISTS Personal_registry (id INTEGER PRIMARY KEY, name TEXT, gender TEXT, address TEXT, postcode INTEGER, nationality TEXT, mobile INTEGER, dob INTEGER, email TEXT, aadhar INTEGER, education TEXT)")
    sql_connect.commit()
    sql_connect.close()

def insert():

    Fullname= "Sabarish"
    gender = "Male"
    address = "Tamilnadu"
    postcode = "629173"
    nation = "India"
    mobile = 7990260021
    email = "sabarish@gmail.com"
    aadhar = 79889
    c="India"
    d = 1
    m = 2
    y = 1989
    conn = sqlite3.connect('personal_info.db')
    with conn:
        cursor=conn.cursor()
        cursor.execute('INSERT INTO Personal_registry (id,name,gender,address,postcode,nationality,mobile,dob,email,aadhar,education) VALUES (NULL,?,?,?,?,?,?,?,?,?,?)',(Fullname,gender,address,postcode,nation,mobile,d,email,aadhar,c))
        conn.commit()

def view():
    sql_connect = sqlite3.connect("personal_info.db")
    mouse_cursor = sql_connect.cursor()
    mouse_cursor.execute("SELECT * FROM Personal_registry")
    rows = mouse_cursor.fetchall()
    sql_connect.close()
    print (rows)

def search(name = ""):
    sql_connect = sqlite3.connect("personal_info.db")
    mouse_cursor = sql_connect.cursor()
    mouse_cursor.execute("SELECT * FROM Personal_registry WHERE name = ?", (name,))
    rows = mouse_cursor.fetchall()
    sql_connect.close()
    print (rows)

def delete(id):
    sql_connect = sqlite3.connect("personal_info.db")
    mouse_cursor = sql_connect.cursor()
    mouse_cursor.execute("DELETE from Personal_registry WHERE id = ?", (id, ))
    sql_connect.close()
    
connect()
view()