from tkinter import *
from tkinter import ttk
class Dx(object):
	def __init__(self):
		self.font_text=('Candara',12,'bold')
	def Top_Dx(self):
		self.ventana_Dx=Toplevel()
		self.ventana_Dx.geometry('500x350')		
		self.ventana_Dx.title('Ingresar el Diagnostico')
		#self.ventana_Dx.iconbitmap('img/paciente.ico')
		etiqueta_nombre=Label(self.ventana_Dx,text='Identificador: ',font=self.font_text,fg='#105B79')
		etiqueta_nombre.grid(row=1,column=0,pady=10)
		self.Entry_Identificador=ttk.Entry(self.ventana_Dx,width=50)			
		self.Entry_Identificador.grid(row=1,column=1,pady=10)

		etiqueta_codigoDx=Label(self.ventana_Dx,text='Codigo: ',font=self.font_text,fg='#105B79')
		etiqueta_codigoDx.grid(row=2,column=0,pady=10)
		self.Entry_codigoDx=ttk.Entry(self.ventana_Dx,width=50)
		self.Entry_codigoDx.grid(row=2,column=1,pady=10)

		etiqueta_DenominacionDx=Label(self.ventana_Dx,text='Denominacion: ',font=self.font_text,fg='#105B79')
		etiqueta_DenominacionDx.grid(row=3,column=0)
		self.Entry_DenominacionDx=ttk.Entry(self.ventana_Dx,width=50)
		self.Entry_DenominacionDx.grid(row=3,column=1,pady=6)

		etiqueta_DescripcionDx=Label(self.ventana_Dx,text='Descripcion: ',font=self.font_text,fg='#105B79')
		etiqueta_DescripcionDx.grid(row=4,column=0)
		self.Text_DescripcionDx=Text(self.ventana_Dx,width=40,height=5)
		self.Text_DescripcionDx.grid(row=4,column=1,pady=6)
			

		self.btn_Guardar=ttk.Button(self.ventana_Dx,text='GUARDAR')
		#self.btn_Guardar['command']=self.Insert_Paciente
		self.btn_Guardar.grid(row=10,column=0,padx=10,sticky='e')	

		self.btn_Cancelar=ttk.Button(self.ventana_Dx,text='CANCELAR')
		#self.btn_Cancelar['command']=self.ventana_Dx.destroy
		self.btn_Cancelar.grid(row=10,column=0,columnspan=2)
		self.ventana_Dx.focus()
		self.ventana_Dx.grab_set()