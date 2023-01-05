from  tkinter import *
from tkinter import ttk
from tkinter import messagebox
import queryPrograma
import random
class Paquetes(object):

	def __init__(self):
		pass
	def NuevoPaquete(self,base):
		etiquetaP=Label(base,text="DENOMINACION:")
		etiquetaP.place(x=30,y=50)
		self.entry_Deno=Entry(base,width=53)
		self.entry_Deno.place(x=150,y=50)

		etiquetaP=Label(base,text='DESCRIPCION:')
		etiquetaP.place(x=30,y=80)
		self.Text_Descrip=Text(base,width=40,height=5)
		self.Text_Descrip.place(x=150,y=80)

		etiquetaP=Label(base,text='SELECCIONAR DIAGNOSTICOS')
		etiquetaP.place(x=150,y=200)

		etiquetaP=Label(base,text='Buscar')
		etiquetaP.place(x=30,y=220)
		self.entry_searchDX=Entry(base,width=40)
		self.entry_searchDX.place(x=120,y=220)
		self.entry_searchDX.bind('<KeyRelease>',self.event_searchDX)

		self.table_Dx1=ttk.Treeview(base,columns=('#1','#2','#3'),show='headings')
		self.table_Dx1.heading("#1",text=".")
		self.table_Dx1.column("#1",width=1,anchor="w")		
		self.table_Dx1.heading("#2",text="CODIGO")
		self.table_Dx1.column("#2",width=60,anchor="w")
		self.table_Dx1.heading("#3",text="DESCRIPCION")
		self.table_Dx1.column("#3",width=320,anchor="w")
		self.table_Dx1.place(x=30,y=270,width=380,height=220)
		self.llenar_TableDXPaquete()
		btn_Seleccion=ttk.Button(base,text='>>')
		btn_Seleccion['command']=self.event_Selected
		btn_Seleccion.place(x=450,y=350) 

		btn_quitarSeleccion=ttk.Button(base,text='<<')
		btn_quitarSeleccion['command']=self.eliminarItemTable
		btn_quitarSeleccion.place(x=450,y=400) 

		etiquetaP=Label(base,text='DIAGNOSTICOS SELECCIONADOS')
		etiquetaP.place(x=600,y=200)

		self.table_DX2=ttk.Treeview(base,columns=('#1','#2','#3'),show='headings')
		self.table_DX2.heading("#1",text=".")
		self.table_DX2.column("#1",width=0,anchor="w")		
		self.table_DX2.heading("#2",text="CODIGO")
		self.table_DX2.column("#2",width=60,anchor="w")
		self.table_DX2.heading("#3",text="DESCRIPCION")
		self.table_DX2.column("#3",width=340,anchor="center")
		self.table_DX2.place(x=550,y=220,width=400,height=290)

		btn_Grabar=ttk.Button(base,text='Guardar')
		btn_Grabar.place(x=400,y=550)
		btn_Grabar['command']=self.insert_Paquete
		btn_Grabar=ttk.Button(base,text='Cancelar')
		btn_Grabar.place(x=550,y=550)

	def llenar_TableDXPaquete(self):
		obj_queryPrograma=queryPrograma.queryGeneral()
		rows=obj_queryPrograma.query_Dx()
		for valores in rows:
			self.table_Dx1.insert('','end',values=(valores.idDX,valores.codi_DX,valores.nombreDX))
	def event_searchDX(self,event):
		self.delete_Table(self.table_Dx1)
		valor=self.entry_searchDX.get()			
		obj_queryPrograma=queryPrograma.queryGeneral()
		rows=obj_queryPrograma.query_DxLike(valor)
		for valores in rows:
			self.table_Dx1.insert('','end',values=(valores.idDX,valores.codi_DX,valores.nombreDX))

	def delete_Table(self,table):
		for item in table.get_children():
			table.delete(item)
	def event_Selected(self):

		control=False
		for item in self.table_DX2.get_children():			
			valor=self.table_DX2.item(item)['values'][0]
			valor1=self.table_Dx1.item(self.table_Dx1.selection()[0],option='values')[0]			
			if int(valor)==int(valor1):
				control=True
				break		
		try:
			valor=[self.table_Dx1.item(self.table_Dx1.selection()[0],option='values')[0],self.table_Dx1.item(self.table_Dx1.selection()[0],option='values')[1],self.table_Dx1.item(self.table_Dx1.selection()[0],option='values')[2]]
			if control==False:
				self.table_DX2.insert('','end',values=(valor[0],valor[1],valor[2]))
			else:
				messagebox.showinfo('Alerta','El valor seleccionado ya se encuentra agregado')
		except Exception as e:
			messagebox.showinfo('Alerta','Seleccione un Item')
	def eliminarItemTable(self):		
		self.table_DX2.delete(self.table_DX2.selection())
	def insert_Paquete(self):
		denominacion=self.entry_Deno.get()
		descripcion=self.Text_Descrip.get('1.0','end-1c')
		#obteniendo diagnosticos.
		valores=[]
		for item in self.table_DX2.get_children():			
			valores.append(self.table_DX2.item(item)['values'][1])
		#insertando a la bd
		obj_queryPrograma=queryPrograma.queryGeneral()
		try:
			if len(valores)!=0:
				controlador=True				
				while controlador:
					codigo=self.Generar_Letras()
					resul=codigo in valores
					if resul!=True:
						break
				
				obj_queryPrograma.insert_Paquete(codigo,denominacion,descripcion,'ACTIVO')				
				for valor in len(valores):
					obj_queryPrograma.insert_DetaPaquete(codigo,valor)
		except Exception as e:
			raise e
	def Generar_Letras(self):
		letras=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','Y','Z']
		letra=''
		for i in range(0,9):
			letra+=letras[random.randint(0,len(letras)-1)]
		return letra
	def DetallePaquete(self,base):

		etiquetaP=Label(base,text="DENOMINACION:")
		etiquetaP.place(x=30,y=50)
		self.entry_DenoDeta=Entry(base,width=53)
		self.entry_DenoDeta.place(x=150,y=50)

		etiquetaP=Label(base,text='DESCRIPCION:')
		etiquetaP.place(x=500,y=50)
		self.Text_DescripDeta=Text(base,width=40,height=5)
		self.Text_DescripDeta.place(x=600,y=50)

		etiquetaP=Label(base,text='DIAGNOSTICO')
		etiquetaP.place(x=30,y=80)

		self.entry_Dx=Entry(base,width=25)
		self.entry_Dx.place(x=150,y=80)
		btn_Search=ttk.Button(base,text='...')
		btn_Search.place(x=310,y=80) 

		btn_Add=ttk.Button(base,text='AGREGAR')
		btn_Add.place(x=390,y=80) 

		etiquetaP=Label(base,text='DIAGNOSTICOS')
		etiquetaP.place(x=30,y=110)


		self.table_General=ttk.Treeview(base,columns=('#1','#2'),show='headings')		
		self.table_General.heading("#1",text="CODIGO")
		self.table_General.column("#1",width=60,anchor="center")
		self.table_General.heading("#2",text="DESCRIPCION")
		self.table_General.column("#2",width=340,anchor="center")
		self.table_General.place(x=30,y=180,width=400,height=150)

		btn_Grabar=ttk.Button(base,text='Editar')
		btn_Grabar.place(x=500,y=200)

		btn_Grabar=ttk.Button(base,text='Guardar')
		btn_Grabar.place(x=500,y=230)

	def NuevoPrograma(self,base,ancho):
		self.etiquetacrear=Label(base,text='crear')
		self.etiquetacrear.place(x=ancho-100,y=30)
		self.etiquetacrear=Label(base,text='cancelar')
		self.etiquetacrear.place(x=ancho-60,y=30)

		etiquetaP=Label(base,text="DENOMINACION:")
		etiquetaP.place(x=30,y=50)
		self.entry_ProgramaName=Entry(base,width=53)
		self.entry_ProgramaName.place(x=150,y=50)

		etiquetaP=Label(base,text="INTERVENCIONES")
		etiquetaP.place(x=500,y=50)
		self.entry_ProgramaName=Spinbox(base,from_=1,to=10)
		self.entry_ProgramaName.place(x=600,y=50)

		etiquetaP=Label(base,text='DESCRIPCION:')
		etiquetaP.place(x=30,y=80)
		self.Text_ProgramaDescip=Text(base,width=40,height=5)
		self.Text_ProgramaDescip.place(x=150,y=80)

		etiquetaP=Label(base,text='SELECCIONAR PAQUETES')
		etiquetaP.place(x=40,y=200)

		self.Lista1=Listbox(base)
		self.Lista1.place(x=30,y=220,width=200,height=250)

		btn_SeleccionPrograma=ttk.Button(base,text='>>')
		btn_SeleccionPrograma.place(x=250,y=350) 

		etiquetaP=Label(base,text='PAQUETES SELECCIONADOS')
		etiquetaP.place(x=370,y=200)

		self.Lista2=Listbox(base)
		self.Lista2.place(x=350,y=220,width=200,height=250)

		btn_GrabarPrograma=ttk.Button(base,text='Guardar')
		btn_GrabarPrograma.place(x=400,y=550)

		btn_GrabarPrograma=ttk.Button(base,text='Cancelar')
		btn_GrabarPrograma.place(x=550,y=550)

	def Programas(self,base,ancho):		
		self.ListaProgramas=Listbox(base,width=ancho)		
		self.ListaProgramas.place(x=0,y=0)