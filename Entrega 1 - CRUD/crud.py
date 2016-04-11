import os, os.path
import cherrypy
import operator

from index import *
from functools import reduce
from sqlalchemy import *


class MakerStats():
	exposed = True
	#listaB = {}

	@cherrypy.expose
	def index(self):
		global cab, cadastro, listar, atualizar, rodape
		pagina = cab + cadastro + listar + atualizar + rodape
		return pagina

	@cherrypy.expose
	def pagCadastro(self, bairro, conhec1=0, conhec2=0, plataforma1=0, plataforma2=0):
		global cab, cadastro, listar, atualizar, rodape
		db = create_engine("mysql://root:root@127.0.0.1:3306/mydb")
		db.echo = True
		metadata = MetaData(db)
		users = Table('user', metadata, autoload=True)
		i = users.insert()
		i.execute(bairro=bairro, eletronica=conhec1, programacao=conhec2, arduino=plataforma1, raspberrypi=plataforma2)
		pagina = cab + cadastro + listar + atualizar + rodape
		return pagina

	@cherrypy.expose
	def pagAtualizar(self):
		global cab, cadastro, listar, atualizar, rodape
		db = create_engine("mysql://root:root@127.0.0.1:3306/mydb")
		db.echo = True
		metadata = MetaData(db)
		users = Table('user', metadata, autoload=True)
		i = users.select()
		rs = i.execute()
		nomeColunas = ['eletrônica', 'programação', 'arduino', 'raspberry pi']
		listaBairros = {}
		for row in rs:
			if (row[1] in listaBairros):
				listaBairros[row[1]].append(row[2:])
			else:
				listaBairros[row[1]] = [row[2:]]
		#global listaB
		#listaB = listaBairros
		#print(listaBairros)
		listaConhecimentosPlataformas = []
		for key in listaBairros:
			parametros = listaBairros[key]
			for dado in parametros:
				listaConhecimentosPlataformas.append(dado)
		result = map(sum, zip(*listaConhecimentosPlataformas))
		listaResultados = list(result)
		selectDB = select([func.count(users.c.iD)])
		runSelectDB = selectDB.execute()
		quantidadeRegistros = []
		for row in runSelectDB:
			quantidadeRegistros = list(row)
		quantidadeRegistrosInt = int(''.join(map(str, quantidadeRegistros)))# Converte lista em um inteiro concatenado.
		frequenciaRelativa = []
		for dado in listaResultados:
			valorRelativo = int(dado)/quantidadeRegistrosInt
			frequenciaRelativa.append(valorRelativo*100)
		pagina = cab + cadastro + listar + atualizar
		for indice in range(len(frequenciaRelativa)-2):
			pagina += "No Recife, há %.2f%% de conhecimentos em %s <br>" % (frequenciaRelativa[indice], nomeColunas[indice])
		for indice in range(2, len(frequenciaRelativa)):
			pagina += "No Recife, %.2f%% usam a plataforma %s <br>" % (frequenciaRelativa[indice], nomeColunas[indice])
		pagina += rodape
		return pagina

	@cherrypy.expose
	def pagListar(self):
		global cab, cadastro, listar, atualizar, rodape
		db = create_engine("mysql://root:root@127.0.0.1:3306/mydb")
		db.echo = True
		metadata = MetaData(db)
		users = Table('user', metadata, autoload=True)
		i = users.select()
		rs = i.execute()
#		l = []
		dictValores = {'1': 'Sim', '0': 'Não'} 
		listaBairros = {}
		pagina = cab + cadastro + listar + atualizar + tableHead
		for row in rs:
			idRow = str(row[0])
			bairro = str(row[1])
			conhecEletr = str(row[2])
			conhecProg = str(row[3])
			platArd = str(row[4])
			platRpi = str(row[5])
			
			pagina += tableStartTag + "<td>" + idRow + "</td><td>" +  bairro + "</td><td>" + dictValores[conhecEletr] + "</td><td>" + dictValores[conhecProg] + "</td><td>" + dictValores[platArd] + "</td><td>" + dictValores[platRpi] + "</td><td>"+ "<a href=pagDeletar?riD=" + idRow + ">Deletar</a>" + tableEndTag
#			conhecEletr = str(key[1])
#			conhecProg = str(key[2])
#			platArd = str(key[3])n rs:
			
#			pagina += str(row) + "<br>"
#			if (row[1] in listaBairros):
#				listaBairros[row[1]].append(row[2:])
#			else:
#				listaBairros[row[1]] = [row[2:]]
#		for key in listaBairros:
#			bairro = str(key[0])
#			conhecEletr = str(key[1])
#			conhecProg = str(key[2])
#			platArd = str(key[3])
			
#			pagina += str(key) + "Eletrônica: " + listaBairros[key][0]
#			x = listaBairros[key]
#			for i in x:
#				l.append(i)
#		print(l)
		#result = map(sum, l)
		#print(result)
#		pagina = cab + cadastro + listar + remover + atualizar 
#		for i in range(len(l)):
#			pagina += "%s <br>" % (str(l[i]))
		pagina += rodape
		return pagina
	@cherrypy.expose
	def pagDeletar(self, riD):
		db = create_engine("mysql://root:root@127.0.0.1:3306/mydb")
		db.echo = True
#		metadata = MetaData(db)
		connection = db.connect()
		trans = connection.begin()
		connection.execute("DELETE FROM user WHERE iD = %d" % (int(riD)))
		trans.commit()
#		users = Table('user', metadata, autoload=True)
#		users.delete().where(users.c.iD==riD)
		connection.close()
		return self.pagListar()
#		rs = i.execute()
#		print(type(riD))
#		print(riD)
#		userSelect = rs.query.get(iD=int(riD))
#		db.delete(userSelect)
	
if __name__ == '__main__':
	cherrypy.config.update({'server.socket_host': '0.0.0.0',
                        'server.socket_port': 8000,
                       })
	cherrypy.quickstart(MakerStats())		
