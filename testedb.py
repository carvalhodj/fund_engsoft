from sqlalchemy import *

db = create_engine("mysql://root:root@127.0.0.1:3306/mydb")

db.echo = True

metadata = MetaData(db)

users = Table('user', metadata, autoload=True)
e = users.insert()
e.execute(bairro='bairro')
