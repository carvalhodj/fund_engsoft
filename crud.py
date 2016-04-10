import os, os.path
import cherrypy
import operator

from sqlalchemy import *


class MakerStats():
	exposed = True
	listaB = {}


	
	@cherrypy.expose
	def index(self):
		return open('index.html')

	@cherrypy.expose
	def POST(self, bairro, conhec1=0, conhec2=0, plataforma1=0, plataforma2=0):
		db = create_engine("mysql://root:root@127.0.0.1:3306/mydb")
		db.echo = True
		metadata = MetaData(db)
		users = Table('user', metadata, autoload=True)
		i = users.insert()
		i.execute(bairro=bairro, eletronica=conhec1, programacao=conhec2, arduino=plataforma1, raspberrypi=plataforma2)
		return open('index.html')

	@cherrypy.expose
	def GET(self):
		db = create_engine("mysql://root:root@127.0.0.1:3306/mydb")
		db.echo = True
		metadata = MetaData(db)
		users = Table('user', metadata, autoload=True)
		i = users.select()
		rs = i.execute()
		listaBairros = {}
		for row in rs:
			if (row[1] in listaBairros):
				listaBairros[row[1]].append(row[2:])
			else:
				listaBairros[row[1]] = [row[2:]]
		global listaB
		listaB = listaBairros
		print(listaBairros)
		l = []
		for key in listaBairros:
			x = listaBairros[key]
			for i in x:
				l.append(i)
		#print(l)
		result = map(sum, zip(*l))
		print(list(result))
		return open('index.html')

	@cherrypy.expose
	def PUT(self):
		db = create_engine("mysql://root:root@127.0.0.1:3306/mydb")
		db.echo = True
		metadata = MetaData(db)
		users = Table('user', metadata, autoload=True)
		i = users.select()
		rs = i.execute()
		l = []
		listaBairros = {}
		for row in rs:
			if (row[1] in listaBairros):
				listaBairros[row[1]].append(row[2:])
			else:
				listaBairros[row[1]] = [row[2:]]
		for key in listaBairros:
			x = listaBairros[key]
			for i in x:
				l.append(i)
		print(l)
		#result = map(sum, l)
		#print(result)
		return open('index.html')
	
	def DELETE(self, riD):
		db = create_engine("mysql://root:root@127.0.0.1:3306/mydb")
		db.echo = True
		metadata = MetaData(db)
		users = Table('user', metadata, autoload=True)
		i = users.select()
		rs = i.execute()
		userSelect = rs.query.get(iD=riD)
		db.delete(userSelect)
	
if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0',
                        'server.socket_port': 8000,
                       })
    cherrypy.quickstart(MakerStats())		
