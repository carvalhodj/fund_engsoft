cab = """<html>
<head></head>
<body><h1>População Maker no Recife!</h1><br><br>"""
cadastro = 	"""<form method="post" action="pagCadastro">
		Bairro: <!-- input type="text" list="bairros" name="bairro" />-->
		<select name="bairro" >
			<option value="Aflitos">Aflitos</option>
			<option value="Afogados">Afogados</option>
			<option value="Água Fria">Água Fria</option>
			<option value="Alto José Bonifácio">Alto José Bonifácio</option>
			<option value="Alto José do Pinho">Alto José do Pinho</option>
			<option value="Alto do Mandu">Alto do Mandu</option>
			<option value="Alto do Pascoal">Alto do Pascoal</option>
			<option value="Alto Santa Teresinha">Alto Santa Teresinha</option>
			<option value="Apipucos">Apipucos</option>
			<option value="Areias">Areias</option>
			<option value="Arruda">Arruda</option>
			<option value="Barro">Barro</option>
			<option value="Beberibe">Beberibe</option>
			<option value="Benfica">Benfica</option>
			<option value="Boa Viagem">Boa Viagem</option>
			<option value="Boa Vista">Boa Vista</option>
			<option value="Bomba do Hemetério">Bomba do Hemetério</option>
			<option value="Bongi">Bongi</option>
			<option value="Brasília Teimosa">Brasília Teimosa</option>
			<option value="Brejo do Beberibe">Brejo do Beberibe</option>
			<option value="Brejo da Guabiraba">Brejo da Guabiraba</option>
			<option value="Cabanga">Cabanga</option>
			<option value="Caçote">Caçote</option>
			<option value="Cajueiro">Cajueiro</option>
			<option value="Campina do Barreto">Campina do Barreto</option>
			<option value="Campo Grande">Campo Grande</option>
			<option value="Casa Amarela">Casa Amarela</option>
			<option value="Casa Forte">Casa Forte</option>
			<option value="Caxangá">Caxangá</option>
			<option value="Cidade Universitária">Cidade Universitária</option>
			<option value="Coelhos">Coelhos</option>
			<option value="Cohab">Cohab</option>
			<option value="Comunidade do Pilar">Comunidade do Pilar</option>
			<option value="Coque">Coque</option>
			<option value="Coqueiral">Coqueiral</option>
			<option value="Cordeiro">Cordeiro</option>
			<option value="Córrego do Jenipapo">Córrego do Jenipapo</option>
			<option value="Curado">Curado</option>
			<option value="Derby">Derby</option>
			<option value="Dois Irmãos">Dois Irmãos</option>
			<option value="Dois Unidos">Dois Unidos</option>
			<option value="Encruzilhada">Encruzilhada</option>
			<option value="Engenho do Meio">Engenho do Meio</option>
			<option value="Entra Apulso">Entra Apulso</option>
			<option value="Espinheiro">Espinheiro</option>
			<option value="Estância">Estância</option>
			<option value="Fundão">Fundão</option>
			<option value="Graças">Graças</option>
			<option value="Guabiraba">Guabiraba</option>
			<option value="Hipódromo">Hipódromo</option>
			<option value="Ibura">Ibura</option>
			<option value="Ilha Joana Bezerra">Ilha Joana Bezerra</option>
			<option value="Ilha do Leite">Ilha do Leite</option>
			<option value="Ilha do Retiro">Ilha do Retiro</option>
			<option value="Imbiribeira">Imbiribeira</option>
			<option value="Ipsep">Ipsep</option>
			<option value="Iputinga">Iputinga</option>
			<option value="Jaqueira">Jaqueira</option>
			<option value="Jardim São Paulo">Jardim São Paulo</option>
			<option value="Jiquiá">Jiquiá</option>
			<option value="Jordão">Jordão</option>
			<option value="Linha do Tiro">Linha do Tiro</option>
			<option value="Macaxeira">Macaxeira</option>
			<option value="Madalena">Madalena</option>
			<option value="Mangabeira">Mangabeira</option>
			<option value="Mangueira">Mangueira</option>
			<option value="Monteiro">Monteiro</option>
			<option value="Morro da Conceição">Morro da Conceição</option>
			<option value="Mustardinha">Mustardinha</option>
			<option value="Nova Descoberta">Nova Descoberta</option>
			<option value="Paissandu">Paissandu</option>
			<option value="Parnamirim">Parnamirim</option>
			<option value="Passarinho">Passarinho</option>
			<option value="Pau Ferro">Pau Ferro</option>
			<option value="Peixinhos">Peixinhos</option>
			<option value="Pina">Pina</option>
			<option value="Poço da Panela">Poço da Panela</option>
			<option value="Ponte d'Uchoa">Ponte d'Uchoa</option>
			<option value="Ponto de Parada">Ponto de Parada</option>
			<option value="Porto da Madeira">Porto da Madeira</option>
			<option value="Prado">Prado</option>
			<option value="Recife (bairro)">Recife (bairro)</option>
			<option value="Rosarinho">Rosarinho</option>
			<option value="San Martin">San Martin</option>
			<option value="Sancho">Sancho</option>
			<option value="Santana">Santana</option>
			<option value="Santo Amaro">Santo Amaro</option>
			<option value="Santo Antônio">Santo Antônio</option>
			<option value="São José ">São José </option>
			<option value="Setúbal">Setúbal</option>
			<option value="Sítio dos Pintos">Sítio dos Pintos</option>
			<option value="Soledade">Soledade</option>
			<option value="Tamarineira">Tamarineira</option>
			<option value="Tejipió">Tejipió</option>
			<option value="Torre">Torre</option>
			<option value="Torreão ">Torreão </option>
			<option value="Torrões">Torrões</option>
			<option value="Totó">Totó</option>
			<option value="Várzea">Várzea</option>
			<option value="Vasco da Gama">Vasco da Gama</option>
			<option value="Vila Tamandaré">Vila Tamandaré</option>
			<option value="Zumbi">Zumbi</option>
			</select><br><br>
	Conhecimentos:<br>
		<input type="checkbox" name="conhec1" value="1">Eletrônica<br>
		<input type="checkbox" name="conhec2" value="1">Programação<br><br>
	Plataformas:<br>
		<input type="checkbox" name="plataforma1" value="1">Arduino<br>
		<input type="checkbox" name="plataforma2" value="1">Raspberry Pi<br><br>
		<button type="submit">Cadastrar</button>
	</form>"""
atualizar  = 	"""<form method="get" action="pagAtualizar">
	<button type="submit">Atualizar</button>
	</form>"""
listar = 	"""<form action="pagListar">
	<button type="submit">Listar</button>
	</form>"""
tableHead = """<table style="width:100%">
<tr><td><h3>Id</h3></td>
<td><h3>Bairro</h3></td>
<td><h3>Eletrônica</h3></td>
<td><h3>Programação</h3></td>
<td><h3>Arduino</h3></td>
<td><h3>Raspberry Pi</h3></td>
<td><h3>Deletar</h3></td></tr>"""
tableStartTag = """<tr>"""
tableEndTag = """</tr>"""
tableFoot = """</table>""" 
rodape = """</body>
</html>"""
