import os, sys
from kivy.config import Config
Config.set('graphics', 'width', '730')
Config.set('graphics', 'height', '980')
from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty,StringProperty,NumericProperty
from kivy.resources import resource_add_path, resource_find
from kivymd.uix.snackbar import Snackbar
from kivy.metrics import dp
from kivy.core.window import Window
from kivymd.uix.snackbar import BaseSnackbar
from kivy.lang import Builder
import sqlite3

#Builder.load_file('test.kv')
#Define our different screens
class CustomSnackbar(BaseSnackbar):
    text = StringProperty(None)
    icon = StringProperty(None)
    font_size = NumericProperty("15sp")
    
class MainLayout(FloatLayout):
    screen_mngr = ObjectProperty(None)
    
    def open_custom_snackbar(self):
        #Snackbar - create popup message after successful posting
        snackbar = Snackbar(
            text="[color=#ffffff]Yo! this is a custom snackbar![/color]",
            font_size="16dp",
            snackbar_x="10dp",
            snackbar_y="10dp",
            size_hint_x= (Window.width - (dp(10) * 2)) / Window.width,
            bg_color="#FF9800"
        )
        snackbar.open()

        
    
    def open_icon_snackbar(self):
        snackbar = CustomSnackbar(
            text="This is a sample snackbar error!",
            icon= "close-circle",
            snackbar_x="10dp",
            snackbar_y="10dp",
            size_hint_x= (Window.width - (dp(10) * 2)) / Window.width,
            bg_color="#B71C1C"
            #buttons=[MDFlatButton(text="ACTION", text_color=(1, 1, 1, 1))]
        )
        snackbar.open()

    def login(self):
         
        inp_username = self.ids.log_username.text
        inp_password = self.ids.log_password.text

        dbconn = sqlite3.connect('kivysql.db',
                                 detect_types=sqlite3.PARSE_DECLTYPES | 
                                 sqlite3.PARSE_COLNAMES)
        dbcursor = dbconn.cursor()
        dbcursor.execute ("SELECT * FROM mstuser WHERE mstuser.username = :var_username AND mstuser.password = :var_password",
            {
            'var_username': inp_username,
            'var_password': inp_password
            })
        records = dbcursor.fetchall()
        
        if not records:
            print ("WALA KANG REKORD")
            return False
        else:
            for user in records:
                print(f"username:{user[1]}\nfirstname:{user[2]}\nlastname:{user[3]}")
                self.store.put('UserInfo',code=user[0],firstname=user[2],lastname=user[3],username=user[1])
            dbconn.commit()
            dbconn.close()
            self.ids.screen_manager1.current = 'dashboard_screen'
            self.ids.screen_manager1.transition.direction = 'left'
            return True
        
        



class screenManagerApp(MDApp):
    def build(self):
            self.theme_cls.material_style = "M3"    
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette= "Blue"
            self.theme_cls.accent_palette= "Teal"
            return MainLayout()  
      
      
if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    screenManagerApp().run()
