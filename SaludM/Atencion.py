from tkinter import *
from tkinter import ttk

class Atenciones(object):
	
	def __init__(self):
		pass
	def widget_NewAtencion(self,base,ancho):
		iconoCrear=PhotoImage(file=('image/subir.png'))
		iconoCancelar=PhotoImage(file=('image/cancelar.png'))
		self.etiquetacrear=Label(base,text='crear',image=iconoCrear)
		self.etiquetacrear.place(x=800,y=30)

		self.etiquetacrear=Label(base,text='cancelar',image=iconoCancelar)
		self.etiquetacrear.place(x=ancho-60,y=30)


		etiquetaP=Label(base,text="DNI:")
		etiquetaP.place(x=30,y=50)
		self.entry_ProgramaName=ttk.Entry(base,width=53)
		self.entry_ProgramaName.place(x=150,y=50)

		etiquetaP=Label(base,text="NOMBRES")
		etiquetaP.place(x=30,y=80)
		self.entry_ProgramaName=ttk.Entry(base,width=53)
		self.entry_ProgramaName.place(x=150,y=80)

		etiquetaP=Label(base,text="APELLIDO PATERNO")
		etiquetaP.place(x=30,y=110)
		self.entry_ProgramaName=ttk.Entry(base,width=53)
		self.entry_ProgramaName.place(x=150,y=110)

		#etiquetaP=Label(base,text="APELLIDO MATERNO")
		#etiquetaP.place(x=30,y=90)
		#self.entry_ProgramaName=Entry(base)
		#self.entry_ProgramaName.place(x=150,y=90)

		#

		#etiquetaP=Label(base,text='SELECCIONAR PAQUETES')
		#etiquetaP.place(x=40,y=200)

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
	