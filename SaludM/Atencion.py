from tkinter import *
from tkinter import ttk

class Atenciones(object):
	
	def __init__(self):
		self.letra=('Ebrima',14,'bold')
		self.righLetra=('Gabriola',14,'bold')
	def widget_NewAtencion(self,base,ancho):
		iconoCrear=PhotoImage(file=('image/subir.png'))
		iconoCancelar=PhotoImage(file=('image/cancelar.png'))
		self.etiquetacrear=Label(base,text='crear',image=iconoCrear,cursor='hand2')
		self.etiquetacrear.image=iconoCrear
		self.etiquetacrear.place(x=int(ancho*0.39),y=700)

		self.etiquetaCancelar=Label(base,text='cancelar',image=iconoCancelar,cursor='hand2')
		self.etiquetaCancelar.place(x=int(ancho*0.44),y=700)
		self.etiquetaCancelar.image=iconoCancelar

		etiquetaP=Label(base,text="DNI:",font=self.righLetra)
		etiquetaP.place(x=int(ancho*0.015),y=50)
		self.entry_ProgramaName=ttk.Entry(base,width=53)
		self.entry_ProgramaName.place(x=int(ancho*0.1),y=55)

		etiquetaE=Label(base,text="EDAD:",font=self.righLetra)
		etiquetaE.place(x=int(ancho*0.3),y=50)
		self.entry_ProgramaEdad=ttk.Entry(base,width=53)
		self.entry_ProgramaEdad.place(x=int(ancho*0.35),y=55)

		etiquetaP=Label(base,text="NOMBRES",font=self.righLetra)
		etiquetaP.place(x=int(ancho*0.015),y=80)
		self.entry_ProgramaName=ttk.Entry(base,width=53)
		self.entry_ProgramaName.place(x=int(ancho*0.1),y=85)

		etiquetaD=Label(base,text="DIRECCION:",font=self.righLetra)
		etiquetaD.place(x=int(ancho*0.3),y=80)
		self.entry_ProgramaDireccion=ttk.Entry(base,width=53)
		self.entry_ProgramaDireccion.place(x=int(ancho*0.35),y=85)

		etiquetaP=Label(base,text="APELLIDO PATERNO",font=self.righLetra)
		etiquetaP.place(x=int(ancho*0.015),y=110)
		self.entry_ProgramaName=ttk.Entry(base,width=53)
		self.entry_ProgramaName.place(x=int(ancho*0.1),y=115)

		etiquetaD=Label(base,text="CELULAR:",font=self.righLetra)
		etiquetaD.place(x=int(ancho*0.3),y=110)
		self.entry_ProgramaDireccion=ttk.Entry(base,width=53)
		self.entry_ProgramaDireccion.place(x=int(ancho*0.35),y=115)

		etiquetaP=Label(base,text="APELLIDO MATERNO",font=self.righLetra)
		etiquetaP.place(x=int(ancho*0.015),y=140)
		self.entry_ProgramaName=Entry(base,width=53)
		self.entry_ProgramaName.place(x=int(ancho*0.1),y=150)		

		etiquetaP=Label(base,bg='#143427',width=int(ancho*0.15))
		etiquetaP.place(x=0,y=200)

		#etiqueta...
		etiquetaP=Label(base,text='PROGRAMAS')
		etiquetaP.place(x=int(ancho*0.37),y=230)

		self.ListaProgramas=Listbox(base)
		self.ListaProgramas.place(x=int(ancho*0.35),y=250,width=400,height=250)


		

		