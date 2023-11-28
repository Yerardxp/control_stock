# Importación de módulos necesarios
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

# Importación de la clase QueriesSQLite del archivo sqlqueries.py
from sqlqueries import QueriesSQLite

# Importación de las ventanas específicas de la aplicación
from signin.signin import SigninWindow
from admin.admin import AdminWindow
from ventas.ventas import VentasWindow

# Definición de la ventana principal de la aplicación
class MainWindow(BoxLayout):
    # Creación de las tablas de la base de datos al iniciar la aplicación
	QueriesSQLite.create_tables()
	def __init__(self, **kwargs):
		super().__init__(*kwargs)
  		# Creación de instancias de las ventanas específicas
		self.admin_widget=AdminWindow()
		self.ventas_widget=VentasWindow(self.admin_widget.actualizar_productos)
		self.signin_widget=SigninWindow(self.ventas_widget.poner_usuario)
		# Adición de las instancias de ventanas a las pantallas correspondientes
		self.ids.scrn_signin.add_widget(self.signin_widget)
		self.ids.scrn_ventas.add_widget(self.ventas_widget)
		self.ids.scrn_admin.add_widget(self.admin_widget)

# Definición de la aplicación principal (hereda de la clase App de Kivy)
class MainApp(App):
	def build(self):
		return MainWindow()

# Verificación si este archivo es ejecutado directamente
if __name__=="__main__":
     # Creación de una instancia de la aplicación y ejecución de la interfaz
	MainApp().run()
