import conect

class queryGeneral(object):
	def __init__(self):
		obj_conectar=conect.Conexion_Programas()
		obj_conectar.ejecutar_conn()
		self.cursor=obj_conectar.get_cursor()
	def query_Dx(self):
		rows=[]
		sql="SELECT * FROM DX"
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows
	def query_DxLike(self,valor):
		rows=[]
		sql=f"""SELECT * FROM DX WHERE codi_DX LIKE '%{valor}%'"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows

	def insert_Paquete(self,codigo,nombre,descripcion,estado):
		sql=f"""INSERT INTO PAQUETE VALUES('{codigo}','{nombre}','{descripcion}','{estado}')"""
		self.cursor.execute(sql)
		self.cursor.commit()	

	def insert_DetaPaquete(self,codigoPaquete,idDX):
		sql=f"""INSERT INTO DETA_PAQUETE VALUES('{codigoPaquete}','{idDX}')"""
		self.cursor.execute(sql)
		self.cursor.commit()
		
	def consulta_Codigo(self,codigo):
		sql=f"""SELECT codPaquete FROM PAQUETE WHERE codPaquete='{codigo}'"""
		self.cursor.execute(sql)
		rows=[]
		rows=self.cursor.fetchall()
		return rows


