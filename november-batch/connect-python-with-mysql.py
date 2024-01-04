import mysql.connector

con = mysql.connector.connect(host = "localhost", username = "root", password = "1234", database = "amazon")

if con.is_connected():
    print("Datbase connetced sucessfully")

cusere = con.cursor()

# cusere.execute("insert into savemydataa values('moris', 'moris@gmail.com', '453454345435', 'this is a message', 'this sis iamge page')")

# cusere.execute("insert into savemydataa values('hlo', 'hlo@gmail.com', '957575646', 'this is a message', 'this sis iamge page')")

# cusere.execute("insert into savemydataa values('hey', 'hey@gmail.com', '957575646', 'this is a message', 'this sis iamge page')")

# con.commit()

cusere.execute("select * from savemydataa")

data = cusere.fetchall()

print(data)