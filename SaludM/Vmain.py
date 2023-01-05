from tkinter import *
import datetime
from tkinter import ttk
from tkinter import messagebox
import Frame_Paquete
import diagnostico
from tkcalendar import Calendar
import Atencion

class Ventana_Principal(object):

	def __init__(self,usuario,nivel):
		self.Usuario=usuario
		self.nivel=nivel		
		self.letra_leyenda=('Candara',16,'bold italic')	
		height=0		
		self.ventana=Tk()
		self.ventana.title('Sistema de Registro y codificacion de Actividades en la Atencion de Salud Mental')		
		#self.ventana.iconbitmap('img/doctor.ico')
		
		#self.ventana.grab_set()
		self.height=self.ventana.winfo_screenheight()-100
		self.width=self.ventana.winfo_screenwidth()-50		
		self.ventana.geometry("%dx%d" % (self.width,self.height))

		#frame principal
		self.Frame_Principal=Frame(self.ventana,bg='black',width=self.width,height=self.height)
		self.Frame_Principal.pack()
		#agregando menu
		self.Barra_Menu=Menu(self.ventana)
		self.ventana['menu']=self.Barra_Menu

		#creando menu
		self.M_Archivo=Menu(self.Barra_Menu,tearoff=False)
		self.M_Archivo.add_command(label='Minimizar',command=self.ventana.iconify)
		self.M_Archivo.add_command(label='Cerrar',command=self.ventana.destroy)
		self.M_Archivo.add_separator()		
		self.Barra_Menu.add_cascade(label='Archivo',menu=self.M_Archivo)

		#menu configuracion				
		self.M_Configuracion=Menu(self.Barra_Menu,tearoff=False)
		self.M_Configuracion.add_command(label='Configurar Paquete',command=self.Frame_Paquete)
		self.M_Configuracion.add_command(label='Generar Programas',command=self.Frame_Programas)
		self.Barra_Menu.add_cascade(label='Configuracion', menu=self.M_Configuracion)		

		#menu Atenciones
		self.M_Atenciones=Menu(self.Barra_Menu,tearoff=False)
		self.M_Atenciones.add_command(label='Aperturar',command=self.Frame_NewAtencion)
		self.M_Atenciones.add_command(label='Realizar Atencion')
		self.Barra_Menu.add_cascade(label='Atenciones',menu=self.M_Atenciones)

		#menu Diagnosticos		
		self.M_Diagnosticos=Menu(self.Barra_Menu,tearoff=False)
		self.M_Diagnosticos.add_command(label='Agendar Diagnosticos',command=self.Diagnostico_Insert)		
		self.Barra_Menu.add_cascade(label='Diagnostico',menu=self.M_Diagnosticos)

		#menu Diagnosticos		
		self.M_Reportes=Menu(self.Barra_Menu,tearoff=False)
		self.M_Reportes.add_command(label='Generar Reporte')		
		self.Barra_Menu.add_cascade(label='Reporte',menu=self.M_Reportes)		
		
		#menu ayuda
		self.M_Usuario=Menu(self.Barra_Menu,tearoff=False)
		self.M_Usuario.add_command(label='Acerca de...',command=lambda:self.mensaje_Info('INFORMACION'))
		self.M_Usuario.add_command(label='Version',command=lambda:self.mensaje_Info('VERSION'))
		self.Barra_Menu.add_cascade(label='Ayuda',menu=self.M_Usuario)

		self.ventana.mainloop()
	def mensaje_Info(self,iden):
		if iden=='INFORMACION':
			messagebox.showinfo('Notificación',f"""Programa de Registro y codificacion de Actividades en la\n atencion de Salud Mental, Desarrollado\npor la Unidad de Estadística e Informática, a traves de la oficina\nde Desarrollo y Programacion del HOSPITAL SUB REGIONAL DE ANDAHUAYLAS...\nTodos los derechos resevados© Andahuaylas 2022\nby Jaime Navarro Crúz""")
		elif iden=='VERSION':
			messagebox.showinfo('Notificación',f"""SISTEMA REGISTRO Y CODIFICACION DE ACTIVIDADES EN LA ATENCION DE SALUD MENTAL\nversion 1.0""")	
	
	def Frame_Paquete(self):
		letra=('Helvetica',12,'bold')
		self.Frame_PackGeneral=Frame(self.Frame_Principal, bg='white',width=self.width,height=self.height)
		self.Frame_PackGeneral.place(x=0,y=0)

		self.Frame_PackLeft=Frame(self.Frame_PackGeneral,highlightbackground="blue", highlightthickness=1,width=int(self.width*0.19),height=self.height)
		self.Frame_PackLeft.grid_propagate(False)
		self.Frame_PackLeft.place(x=0,y=0)
		

		etiqueta_paquetes=Label(self.Frame_PackLeft,text='Paquetes Disponibles',bg='gray',fg='white',width=int(self.width*0.019),font=letra)
		etiqueta_paquetes.grid(row=0,column=0,columnspan=3)

		self.Frame_PackRight=Frame(self.Frame_PackGeneral,bg='white',width=int(self.width*0.79),height=self.height)
		self.Frame_PackRight.place(x=int(self.width*0.2),y=0)
		#agregando particiones 
		self.Frame_PackNew=Frame(self.Frame_PackRight,highlightbackground="blue", highlightthickness=1,width=int(self.width*0.79),height=int(self.height*0.6))
		self.Frame_PackNew.place(x=0,y=0)
		etiqueta_paquetes=Label(self.Frame_PackNew,text='Generar un Nuevo paquete',font=letra,bg='gray',fg='white',width=int(self.width*0.08),anchor='center')
		etiqueta_paquetes.place(x=0,y=0)
		self.Frame_NewPaquete()

		self.Frame_PackDeta=Frame(self.Frame_PackRight,highlightbackground="blue", highlightthickness=1,width=int(self.width*0.79),height=int(self.height*0.39))
		self.Frame_PackDeta.place(x=0,y=int(self.height*0.61))

		etiqueta_paquetes=Label(self.Frame_PackDeta,text='Detalle de los paquetes',font=letra,bg='gray',fg='white',width=int(self.width*0.08),anchor='center')
		etiqueta_paquetes.place(x=0,y=0)
		self.Paquetes()

	def Frame_NewAtencion(self):
		letra=('Helvetica',12,'bold')
		self.Frame_AtencionNew=Frame(self.Frame_Principal,width=self.width,height=self.height)
		self.Frame_AtencionNew.place(x=0,y=0)
		etiqueta=Label(self.Frame_AtencionNew,text='AGREGAR AL PACIENTE PARA UNA NUEVA ATENCION',fg='white',bg='#1F0C3E',width=int(self.width*0.10),font=letra)
		etiqueta.place(x=0,y=0)
		obj_Atencion=Atencion.Atenciones()
		obj_Atencion.widget_NewAtencion(self.Frame_AtencionNew,self.width)

	def Frame_Programas(self):
		letra=('Helvetica',12,'bold')
		self.Frame_PackProgramas=Frame(self.Frame_Principal,width=self.width,height=self.height)
		self.Frame_PackProgramas.place(x=0,y=0)

		self.Frame_ProgramasLeft=Frame(self.Frame_PackProgramas,highlightbackground="blue", highlightthickness=1,width=int(self.width*0.19),height=self.height)
		self.Frame_ProgramasLeft.grid_propagate(False)
		self.Frame_ProgramasLeft.place(x=0,y=0)
		obj_framProgramas=Frame_Paquete.Paquetes()		
		obj_framProgramas.Programas(self.Frame_ProgramasLeft,int(self.width*0.03))

		etiqueta_paquetes=Label(self.Frame_ProgramasLeft,text='Pogramas',bg='#1F0C3E',fg='white',width=int(self.width*0.019),font=letra)
		etiqueta_paquetes.grid(row=0,column=0)

		self.Frame_ProgramasRight=Frame(self.Frame_PackProgramas,bg='white',width=int(self.width*0.79),height=self.height)
		self.Frame_ProgramasRight.place(x=int(self.width*0.2),y=0)
		#agregando particiones 
		self.Frame_ProgramasNew=Frame(self.Frame_ProgramasRight,highlightbackground="blue", highlightthickness=1,width=int(self.width*0.79),height=int(self.height*0.5))
		self.Frame_ProgramasNew.place(x=0,y=0)
		etiqueta_paquetes=Label(self.Frame_ProgramasNew,text='Agregar Nuevo Programa',font=letra,bg='#1F0C3E',fg='white',width=int(self.width*0.08),anchor='center')
		etiqueta_paquetes.place(x=0,y=0)
		self.Frame_NewPrograma()
		
		self.Frame_ProgramasDeta=Frame(self.Frame_ProgramasRight,highlightbackground="blue", highlightthickness=1,width=int(self.width*0.79),height=int(self.height*0.49))
		self.Frame_ProgramasDeta.place(x=0,y=int(self.height*0.51))

		etiqueta_paquetes=Label(self.Frame_ProgramasDeta,text='Detalle del Programa',font=letra,bg='#1F0C3E',fg='white',width=int(self.width*0.08),anchor='center')
		etiqueta_paquetes.place(x=0,y=0)		


	def Frame_NewPaquete(self):		
		obj_framePaquete=Frame_Paquete.Paquetes()
		obj_framePaquete.NuevoPaquete(self.Frame_PackNew)

	def Frame_DetaPaquete(self):
		obj_framePaquete=Frame_Paquete.Paquetes()
		obj_framePaquete.DetallePaquete(self.Frame_PackDeta)

	def Frame_NewPrograma(self):		
		obj_framePaquete=Frame_Paquete.Paquetes()
		obj_framePaquete.NuevoPrograma(self.Frame_ProgramasNew,int(self.width*0.79))
	def Diagnostico_Insert(self):
		obj_Dx=diagnostico.Dx()
		obj_Dx.Top_Dx()	

	def llenar_Menu(self):
		try:
			self.Lista_Menu.delete(0,'end')
			rows=self.obj_QueryGalen.query_Programacion(self.calendario.selection_get())
			for val in rows:
				self.Lista_Menu.insert(0,str(val.IdTurno)+'-'+str(val.IdMedico)+'_'+val.Nombre)
		except Exceptions as e:
			messagebox.showinfo('Alerta',f'Error {e}')
	def calendar_event(self,event):		
		self.llenar_Menu()

	def Paquetes(self):
		self.MenuProgramas=Listbox(self.Frame_PackLeft,width=int(self.width*0.030))
		self.MenuProgramas.grid(row=1,column=0,columnspan=3,rowspan=20)
		
		btn=ttk.Button(self.Frame_PackLeft,text='Boton')
		btn['command']=self.Frame_DetaPaquete
		btn.grid(row=21,column=0)	

	
	
obj=Ventana_Principal('usuario','jaime')
