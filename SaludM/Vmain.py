from tkinter import *
import datetime
from tkinter import ttk
from tkinter import messagebox
import Frame_Paquete
from tkcalendar import Calendar

class Ventana_Principal(object):

	def __init__(self,usuario,nivel):
		self.Usuario=usuario
		self.nivel=nivel		
		self.letra_leyenda=('Candara',16,'bold italic')	
		height=0		
		self.ventana=Tk()
		self.ventana.title('Sistema de Registro y codificacion de Actividades en la Atencion de Salud Mental')
		#self.ventana.attributes('-fullscreen', True) 
		#self.ventana.iconbitmap('img/doctor.ico')
		#self.ventana.focus_set()
		#self.ventana.grab_set()
		self.height=self.ventana.winfo_screenheight()-100
		self.width=self.ventana.winfo_screenwidth()-50		
		self.ventana.geometry("%dx%d" % (self.width,self.height))
		#self.ventana.protocol('WM_DELETE_WINDOW',self.salir)
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
		self.M_Configuracion.add_command(label='Generar Programas')
		self.Barra_Menu.add_cascade(label='Configuracion', menu=self.M_Configuracion)		

		#menu Atenciones
		self.M_Atenciones=Menu(self.Barra_Menu,tearoff=False)
		self.M_Atenciones.add_command(label='Aperturar')
		self.M_Atenciones.add_command(label='Realizar Atencion')
		self.Barra_Menu.add_cascade(label='Atenciones',menu=self.M_Atenciones)

		#menu Diagnosticos		
		self.M_Diagnosticos=Menu(self.Barra_Menu,tearoff=False)
		self.M_Diagnosticos.add_command(label='Agendar Diagnosticos')		
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
		self.Frame_PackGeneral.pack()

		self.Frame_PackLeft=Frame(self.Frame_PackGeneral,highlightbackground="blue", highlightthickness=1,width=int(self.width*0.19),height=self.height)
		self.Frame_PackLeft.grid_propagate(False)
		self.Frame_PackLeft.place(x=0,y=0)
		self.Paquetes()



		etiqueta_paquetes=Label(self.Frame_PackLeft,text='Paquetes Disponibles',bg='gray',fg='white',width=int(self.width*0.019),font=letra)
		etiqueta_paquetes.grid(row=0,column=0)

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

		
	def evento_clickRight(self,event):
		try:
			#print(len(self.Lista_Menu.curselection()))
			if len(self.Lista_Menu.curselection())!=0:
				self.cupo_=event.widget.cget('text')			
				consultorio_Total=self.Lista_Menu.get(self.Lista_Menu.curselection()[0])
				consultorio=consultorio_Total[consultorio_Total.find('_')+1:]
				#consultar si el cupo esta agendado			
				rows=self.obj_QueryTriaje.query_CupoNumber(self.calendario.selection_get(),consultorio,self.cupo_,self.turno,self.Medico_Datos)
			
				if len(rows)==1:
					date=datetime.date.today()
					if self.calendario.selection_get()<date:
						self.menu_FechaAnterior.tk_popup(event.x_root,event.y_root)
					else:
						self.menu_Fechaposterior.tk_popup(event.x_root,event.y_root)			

				elif len(rows)==0:
					self.menu_right.tk_popup(event.x_root,event.y_root)
			else:
				messagebox.showinfo('Alerta','Seleccione un consultorio!')

		finally:
			self.menu_right.grab_release()
	def evento_agregar(self):
		date=datetime.date.today()
		obj_TopTriaje=None
		if self.calendario.selection_get()>=date:
			obj_TopTriaje=Top_Triaje.Triaje()
			obj_TopTriaje.Top_Agregar(globals()['self.cupo%s'%self.cupo_],self.servicio,self.Medico_Datos,self.Usuario,self.calendario.selection_get(),self.turno)		
		else:
			messagebox.showinfo('Alerta','No se puede programar para esta fecha!')
		#globals()['self.cupo%s'%self.cupo_].configure(bg='green')	
	def evento_EliminarCupo(self):
		result=messagebox.askquestion('Alerta','Estas seguro que desea Eliminar')
		if result=='yes':
			consultorio_Total=self.Lista_Menu.get(self.Lista_Menu.curselection()[0])
			consultorio=consultorio_Total[consultorio_Total.find('_')+1:]
			if int(self.cupo_)<21:				
				self.obj_QueryTriaje.Eliminar_Cita(self.cupo_,self.calendario.selection_get(),consultorio,self.Medico_Datos,self.turno)
				globals()['self.cupo%s'%self.cupo_].configure(bg='#185522',fg='white')
			else:
				self.obj_QueryTriaje.Eliminar_Cita(self.cupo_,self.calendario.selection_get(),consultorio,self.Medico_Datos,self.turno)
				globals()['self.cupo%s'%self.cupo_].configure(fg='white')
		#self.obj_ConsultaTriaje
	def Frame_NewPaquete(self):		
		obj_framePaquete=Frame_Paquete.Paquetes()
		obj_framePaquete.NuevoPaquete(self.Frame_PackNew)
	def Frame_DetaPaquete(self):
		obj_framePaquete=Frame_Paquete.Paquetes()
		obj_framePaquete.DetallePaquete(self.Frame_PackDeta)
		
	def evento_ConsultaCupo(self):
		consultorio_Total=self.Lista_Menu.get(self.Lista_Menu.curselection()[0])
		consultorio=consultorio_Total[int(consultorio_Total.find('_'))+1:]
		rows=self.obj_QueryTriaje.query_DataTriaje(self.calendario.selection_get(),consultorio,self.cupo_,self.Medico_Datos,self.turno)		
		for val in rows:
			dni=val.dni
			fuente=val.fuente
			cupo=val.Nro_Cupo
			medico=val.Medico
			consultorio=val.Especialidad
			nro_Referencia=val.Nro_Referencia
			establecimiento=val.P_C
			Historia=val.Historia
			fecha_A=val.Fecha_Atencion
			turno=val.Turno
		
		self.obj_Impresion.imprimir_Cupo(dni,fuente,cupo,medico,consultorio,nro_Referencia,fecha_A,Historia,establecimiento,turno)
		obj_TopReporte=Top_Reporte.Reporte()
		obj_TopReporte.top_ConsultaCupo()

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

		try:
			Nro_Cupo=0
			for i in range(4):			
				globals()['self.cupo%s'%Nro_Cupo]=Label(self.Frame_PackLeft,text=f"PAQUETE NUMERO: {Nro_Cupo}",width=40,bg='green',fg='white',borderwidth=2)
				globals()['self.cupo%s'%Nro_Cupo].bind('<Button-3>',self.evento_clickRight)
				globals()['self.cupo%s'%Nro_Cupo].grid(row=i+1,column=0,ipady=20,padx=7,pady=5)							
				Nro_Cupo+=1			
		except Exception as e:
			print(e)
		btn=ttk.Button(self.Frame_PackLeft,text='Boton')
		btn['command']=self.Frame_DetaPaquete
		btn.grid(row=5,column=0)	

	
	
obj=Ventana_Principal('usuario','jaime')
