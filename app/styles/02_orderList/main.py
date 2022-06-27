import kivy
from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput 
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
#set up the mygrid before the myapp
#make sure all the objects are created before the app is, which runs them
#keyword arguments is kwargs

class MyGrid(GridLayout):
    orders = ObjectProperty(None)
    menu = ObjectProperty(None)
    update = ObjectProperty(None)
    remove = ObjectProperty(None)

    def pressed(self):
        ordertext = self.orders.text
        menutext = self.menu.text
        updatetext = self.update.text
        removetext = self.remove.text
        print(ordertext)
        print(menutext)
        print(updatetext)
        print(removetext)
        
class MyApp(App):
    def build(self):
        return MyGrid()

if __name__=="__main__":
    MyApp().run() 