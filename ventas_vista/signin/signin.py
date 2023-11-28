from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

from sqlqueries import QueriesSQLite

# Cargar el archivo kv asociado con esta ventana de inicio de sesión
Builder.load_file('signin/signin.kv')

class SigninWindow(BoxLayout):
	def __init__(self, poner_usuario_callback, **kwargs):
		super().__init__(*kwargs)
		self.poner_usuario=poner_usuario_callback

	def verificar_usuario(self, username, password):
		# Establecer una conexión a la base de datos SQLite
		connection = QueriesSQLite.create_connection("pdvDB.sqlite")
		# Obtener la lista de usuarios desde la base de datos
		users=QueriesSQLite.execute_read_query(connection, "SELECT * from usuarios")
		if users:
			# Verificar si el nombre de usuario y la contraseña están proporcionados
			if username=='' or password=='':
				self.ids.signin_notificacion.text='Falta nombre de usuario y/o contraseña'
			else:
				usuario={}
				# Buscar el usuario en la lista de usuarios
				for user in users:
					if user[0]==username:
						usuario['nombre']=user[1]
						usuario['username']=user[0]
						usuario['password']=user[2]
						usuario['tipo']=user[3]
						break
				# Verificar si se encontró un usuario con el nombre de usuario proporcionado
				if usuario:
					# Verificar si la contraseña coincide
					if usuario['password']==password:
						self.ids.username.text=''
						self.ids.password.text=''
						self.ids.signin_notificacion.text=''
						# Determinar si el usuario es un trabajador o un administrador
						if usuario['tipo']=='trabajador':
							self.parent.parent.current='scrn_ventas'
						else:
							self.parent.parent.current='scrn_admin'
						# Llamar a la función proporcionada para poner al usuario en la aplicación
						self.poner_usuario(usuario)
					else:
						self.ids.signin_notificacion.text='Usuario o contraseña incorrecta'
				else:
					self.ids.signin_notificacion.text='Usuario o contraseña incorrecta'
		# Si no hay usuarios en la base de datos, crear un usuario administrador por defecto
		else:
		    usuario_tuple=('usuario', 'Usuario Inicio', '123', 'admin')
		    crear_usuario = "INSERT INTO usuarios (username, nombre, password, tipo) VALUES (?,?,?,?);"
		    QueriesSQLite.execute_query(connection, crear_usuario, usuario_tuple)
		    self.ids.signin_notificacion.text='Se creo primer usuario. usuario 123'



class SigninApp(App):
	def build(self):
		return SigninWindow()

if __name__=="__main__":
	SigninApp().run()
