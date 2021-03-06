import os, os.path
import cherrypy
import operator

from index import *
from functools import reduce
from sqlalchemy import *


class MakerStats():
	exposed = True

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
			
			pagina += tableStartTag + "<td>" + bairro + "</td><td>" + dictValores[conhecEletr] + "</td><td>" + dictValores[conhecProg] + "</td><td>" + dictValores[platArd] + "</td><td>" + dictValores[platRpi] + "</td><td>"+ "<a href=pagDeletar?riD=" + idRow + ">Deletar</a>" + tableEndTag
		pagina += rodape
		return pagina
	@cherrypy.expose
	def pagDeletar(self, riD):
		db = create_engine("mysql://root:root@127.0.0.1:3306/mydb")
		db.echo = True
		connection = db.connect()
		trans = connection.begin()
		connection.execute("DELETE FROM user WHERE iD = %d" % (int(riD)))
		trans.commit()
		connection.close()
		return self.pagListar()
	
if __name__ == '__main__':
	cherrypy.config.update({'server.socket_host': '0.0.0.0',
                        'server.socket_port': 8000,
                       })
	cherrypy.quickstart(MakerStats())		
