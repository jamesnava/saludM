from  tkinter import *
from tkinter import ttk
from tkinter import messagebox
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

		self.table_General=ttk.Treeview(base,columns=('#1','#2'),show='headings')		
		self.table_General.heading("#1",text="CODIGO")
		self.table_General.column("#1",width=60,anchor="center")
		self.table_General.heading("#2",text="DESCRIPCION")
		self.table_General.column("#2",width=340,anchor="center")
		self.table_General.place(x=30,y=220,width=400,height=290)

		btn_Seleccion=ttk.Button(base,text='>>')
		btn_Seleccion.place(x=450,y=350) 

		etiquetaP=Label(base,text='DIAGNOSTICOS SELECCIONADOS')
		etiquetaP.place(x=600,y=200)


		self.table_General=ttk.Treeview(base,columns=('#1','#2'),show='headings')		
		self.table_General.heading("#1",text="CODIGO")
		self.table_General.column("#1",width=60,anchor="center")
		self.table_General.heading("#2",text="DESCRIPCION")
		self.table_General.column("#2",width=340,anchor="center")
		self.table_General.place(x=550,y=220,width=400,height=290)

		btn_Grabar=ttk.Button(base,text='Guardar')
		btn_Grabar.place(x=400,y=550)

		btn_Grabar=ttk.Button(base,text='Cancelar')
		btn_Grabar.place(x=550,y=550)

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
		#messagebox.showinfo('alerta',base.winfo_width())
		
		self.ListaProgramas=Listbox(base,width=ancho)		
		self.ListaProgramas.place(x=0,y=0)