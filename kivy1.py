import os, sys
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.resources import resource_add_path, resource_find
from kivy.lang import Builder

#Builder.load_file('kivymd.kv')

class MainLayout(MDBoxLayout):
    def func (self,app):
        if  app.theme_cls.theme_style == "Dark":
            app.theme_cls.theme_style = "Light"
            app.theme_cls.primary_style = "Teal"
            app.theme_cls.accent_style = "Blue"
        else:
            app.theme_cls.theme_style = "Dark"
            app.theme_cls.primary_style = " Blue"
            app.theme_cls.accent_style = "Teal"
            
            
class mdAppComponents(MDApp):
    def  build (self):
        self.theme_cls.material_style = "M3"    
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette= "Blue"
        self.theme_cls.accent_palette= "Teal"
        return MainLayout()  
     
      
if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    mdAppComponents().run()